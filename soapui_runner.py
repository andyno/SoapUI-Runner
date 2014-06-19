import ConfigParser
import argparse
import os
import subprocess


def get_soapui_home():
    try:  
        return os.environ["SOAPUI_RUNNER"]
    except KeyError: 
        print "Please set the environment variable SOAPUI_RUNNER"


def run_suite(suite):
    HOME = get_soapui_home()
    # DEFINE CLASSPATH
    CLASSPATH = HOME + '/sui/soapui-5.0.0.jar:' + HOME + '/sui/lib/*:'
    # DEFINE JAVA PART OF CMD
    JAVA_CMD = ['java', '-Xms128m', '-Xmx1024m', 
                '-Dsoapui.logroot=' + HOME + '/logs/',
                '-Dsoapui.ext.libraries=' + HOME + '/sui/ext',
                '-Dsoapui.ext.listeners=' + HOME + '/sui/listeners',
                '-Dsoapui.ext.actions=' + HOME + '/sui/actions',
                '-cp', CLASSPATH, 'com.eviware.soapui.tools.SoapUITestCaseRunner']
    # DEFINE SOAP UI PART OF CMD
    SOAP_UI_CMD = [suite['project'], '-s'+suite['suite'],'-r', '-a',
                   '-f'+suite['workspace'] + '/output/' + suite['name'],
                   '-GworkspaceDir'+suite['workspace']]
    # CALL PROCESS
    subprocess.call(JAVA_CMD + SOAP_UI_CMD)


def read_sui():
    sui = ConfigParser.RawConfigParser()
    sui.read('testcases.sui')
    return sui


def get_case(name, sui):
    try:
        case = {
            'name': name,
            'suite': sui.get(name, 'suite'),
            'project': sui.get(name, 'project'),
            'workspace': sui.get(name, 'workspace')
        }
    except ConfigParser.NoOptionError:
        case = {
            'name': name,
            'suites': sui.get(name, 'suites').split(',')
        }
    return case


def read_suites(arg_suites, include_sets, sui):
    suites = []
    for arg_suite in arg_suites:
        suite = get_case(arg_suite, sui)
        if suite.has_key('suites') and include_sets:
            for _suite in suite['suites']:
                case = get_case(_suite, sui)
                case['name'] = suite['name']
                suites.append(case)
        elif not suite.has_key('suites'):
            suites.append(get_case(arg_suite, sui))
    return suites


def main():
    parser = argparse.ArgumentParser(description='Run SUI tests')
    parser.add_argument('suites', metavar='Suite', nargs='*', help='suites to run')
    parser.add_argument('--all', action='store_true', help='run all suites')
    args = parser.parse_args()


    sui = read_sui()
    if args.all:
        suites = read_suites(sui.sections(), False, sui)
    else:
        suites = read_suites(args.suites, True, sui)

    for suite in suites:
        run_suite(suite)


if __name__ == "__main__": main()
