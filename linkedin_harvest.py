#!/usr/bin/python

import re
import sys
#import urllib

if len(sys.argv) != 4:
    print "\n*************************************************"
    print "**  LinkedIn Email Harvester                   **"
    print "**  by H@ck1tHu7ch (Justin Hutchens)           **"
    print "**  little changes by vibrio (Ricardo Almeida) **"
    print "**  ...GONE PHISHING!!!                        **"
    print "*************************************************\n\n"
    print "First browse LinkedIn through Burp, save all responses to a file and after that run this\n"
    print "Usage - ./linkedin_harvest.py [Filename] [Format num] [suffix]"
    print "\nFORMATS:"
    print "1 - [first].[last]@[suffix]"
    print "2 - [first][last]@[suffix]"
    print "3 - [first_initial][last]@[suffix]\n"
    print "Example - ./linkedin_harvest.py input.txt 1 company.com"
    print "Example will create emails in the form of john.smith@company.com from the input.txt file"
    sys.exit()

in_file = str(sys.argv[1])
format = int(sys.argv[2])
suffix = str(sys.argv[3]).lower()

def get_names(in_file):

    ##########################################################################################################
    #with open(in_file) as f:
    #    st = urllib.unquote_plus(f.read())
    #    print st
    ##########################################################################################################

    # Getting All Contacts from the linkedin advanced search (first name, middle & last name)
    # NOTE: Doesn't handle fucky string encoding very well :P
    f = open(in_file,'r')
    strings = re.findall(r'(profileName\=)(\w*\+\w*)',f.read(), re.UNICODE)
    f = open(in_file,'r')
    strings = strings + re.findall(r'(profileName\=)(\w*\+\w*\+\w*)',f.read(), re.UNICODE)
    # Create List of Names
    names = []
    for x in set(strings):
        names.append((str(x[1]).replace("+", " ")))
    return names

    ##########################################################################################################
    # Old stuff
    # Getting 1st Degree Contacts (first name, middle & last name)
    #f = open(in_file,'r')
    #strings = re.findall(r'"(\w*\s\w*)(\sis\syour\sconnection)',f.read())
    #f = open(in_file,'r')
    #strings = re.findall(r'"(\w*\s\w*\s\w*)(\sis\syour\sconnection)',f.read())

    # Getting 2nd Degree Contacts (first name, middle & last name)
    #f = open(in_file,'r')
    #strings = strings + re.findall(r'"(\w*\s\w*)(\sis\sa\s2nd\sdegree\scontact)',f.read())
    #f = open(in_file,'r')
    #strings = strings + re.findall(r'"(\w*\s\w*\s\w*)(\sis\sa\s2nd\sdegree\scontact)',f.read())

    # Getting 3rd Degree Contacts (first name, middle & last name)
    #f = open(in_file,'r')
    #strings = strings + re.findall(r'"(\w*\s\w*)(\sis\sa\s3rd\sdegree\scontact)',f.read())
    #f = open(in_file,'r')
    #strings = strings + re.findall(r'"(\w*\s\w*\s\w*)(\sis\sa\s3rd\sdegree\scontact)',f.read())

    # Create List of Names
    #names = []
    #for x in strings:
    #    names.append(str(x[0]))
    #return names

def format_1(names,suffix):
    emails = []
    for x in names:
        first = x.split(' ')[0].lower()
        last = x.split(' ')[-1].lower()
        emails.append(first + '.' + last + '@' + suffix)
    print '----------------------------------'
    print 'Number of names extracted: ' + str(len(names))
    print '----------------------------------'
    return emails

def format_2(names,suffix):
    emails = []
    for x in names:
        first = x.split(' ')[0].lower()
        last = x.split(' ')[-1].lower()
        emails.append(first + last + '@' + suffix)
    print '----------------------------------'
    print 'Number of names extracted: ' + str(len(names))
    print '----------------------------------'
    return emails

def format_3(names,suffix):
    emails = []
    for x in names:
        first = x.split(' ')[0].lower()
        last = x.split(' ')[-1].lower()
        emails.append(first[0] + last + '@' + suffix)
    print '----------------------------------'
    print 'Number of names extracted: ' + str(len(names))
    print '----------------------------------'
    return emails

names = get_names(in_file)

if format == 1:
    emails = format_1(names,suffix)
elif format == 2:
    emails = format_2(names,suffix)
elif format == 3:
    emails = format_3(names,suffix)

outfile = open('linkedin_emails.txt','w')
for x in emails:
    outfile.write(str(x) + '\n')
    print x
outfile.close()
