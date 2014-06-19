SoapUI Runner
=============
Convenience script for running soapUI test cases.

Downloads all dependencies to run a Test Suite from command line.

Installation
------------
1. Clone repo to prefered location
2. Run download.py
3. Add environment variable SOAPUI_RUNNER pointing to repo directory (i.e. /Users/john/soapui)
4. Add scripts folder to path ($SOAPUI_RUNNER/scripts)
5. Run CHMOD +x sui to be able to run from command line
6. Run sui -h in terminal to verify

Usage
-----
To use the script, go to a directory containing a testcases.sui file.

Run:
```
sui "Suite 1"
```
in /demo containing testcases.sui to run that suite as defined in the testcases.sui file.

Or:
```
sui "Suite 1" "Half Suite" ...
```
to run multiple suites.


Run:
```
sui --all
```
to run all suites in file, except groups of suites.

Output will be generated to the workspace directory
