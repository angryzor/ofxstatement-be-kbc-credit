~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Belgian KBC Bank plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides an `ofxstatement`_ plugin for converting the Belgian KBC
bank's CSV format statements to OFX.

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugins for ofxstatement parse a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

Users of ofxstatement have developed several plugins for their banks. They are
listed on main `ofxstatement`_ site. If your bank is missing, you can develop
your own plugin.

.. _ofxstatement: https://github.com/kedder/ofxstatement

Usage
=====
  $ ofxstatement convert -t kbcbe input.csv output.ofx
