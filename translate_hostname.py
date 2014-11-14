import re

#Global Dictionaries

ENV = {
    "d1": "dev1",
    "d2": "dev2",
    "p1": "prod1"
}

TYPES = {
    "sql": "SQL Server",
    "www": "Web Server",
    "ora": "Oracle Server"
}


#Function to Extra ENV and TYPES definitions from Global Dictionaries (It could be more universal by taking dictionaries as arguments, but just an example)
def translate_hostname(hostname):
    r = re.match(r'(\w\d+)(\w{3})\d+', hostname)
    env = str.lower(r.group(1))
    type = str.lower(r.group(2))

    if ENV.has_key(env):
        env = ENV[env]
    else:
        env = "undefined env"

    if TYPES.has_key(type):
        type = TYPES[type]
    else:
        type = "undefined type"

    host_params = {'env': env, 'type': type}

    return host_params




if __name__ == '__main__':

    host_params = {}

    RANDOMTEXT = """
    aipejofa;lkwejgiaD1SQL02a;slkdflakjwe;ifjd2sql03aw;iefiawejiafj
    T1SQL02awoejfpaoiwjefoiawjpD1www03fapwijfpawjefpaT2BIT03afwoejfaiw
    """

    #Search for Hostname amongst RANDOMTEXT
    hostnames = re.findall(r'\w\d+\w{3}\d+', RANDOMTEXT)

    #Extract definitions with function and populate a 2D dictionary
    for host in hostnames:
        host_params[host] = translate_hostname(host)

    #Iterate through 2D dictionary by hostname and print stuff out (Could have done that in previous step by just an example)
    for host in host_params:
        print "HOST:  " + host + "\n"
        print "ENV:   " + host_params[host]['env']
        print "TYPE:  " + host_params[host]['type']
        print "\n----------------------------\n"
