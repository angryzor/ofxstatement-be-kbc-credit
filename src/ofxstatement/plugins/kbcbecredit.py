from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import StatementLine, BankAccount
from ofxstatement.exceptions import ParseError
import csv
import re


LINELENGTH = 17
HEADER_START = "kredietkaart"

class KbcBeCreditPlugin(Plugin):
    """Belgian KBC Bank plugin for ofxstatement
    """

    def get_parser(self, filename):
        f = open(filename, 'r', encoding='latin1')
        parser = KbcBeCreditParser(f)
        return parser


class KbcBeCreditParser(CsvStatementParser):

    date_format = "%d/%m/%Y"

    mappings = {
        'memo': 15,
        'date': 4,
        'amount': 10,
        'payee': 12,
    }

    line_nr = 0

    def parse_float(self, value):
        """Return a float from a string with ',' as decimal mark.
        """
        return float(value.replace(',','.'))

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        return csv.reader(self.fin, delimiter=';', skipinitialspace=True)

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """
        self.line_nr += 1
        if line[0] == HEADER_START:
            return None
        elif len(line) != LINELENGTH:
            raise ParseError(self.line_nr,
                             'Wrong number of fields in line! ' +
                             'Found ' + str(len(line)) + ' fields ' +
                             'but should be ' + str(LINELENGTH) + '!')

        stmt_ln = super(KbcBeCreditParser, self).parse_record(line)

        return stmt_ln
