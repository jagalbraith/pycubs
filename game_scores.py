#!/usr/bin/env python

import subprocess

def scores():
    command = 'lynx -nonumbers -dump http://www.baseball-reference.com/boxes/ | grep Final -A 1 | grep -A 1 -B 1 Cubs | xargs'
    bark = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    moo = bark.communicate()
    dict = {}
    moo = moo[0].replace('-- ', '').replace('\n', '').split(' ')
    if 'Final' in moo:
        #print moo
        dict['status'] = 'Final'
        moo.pop(moo.index('Final'))
    else:
        dict['status'] = 'In Progress'

    tb = []
    for item in moo:
        if item is not 'Final' and item.isalpha():
           tb.append(item)
        elif item.isdigit():
            dict['{city} {name}'.format(city=tb[0], name=tb[1])] = int(item)
            tb = []
    return dict


def main():
    scored = scores()
    for key in scored.keys():
        if key is 'status':
            print 'Game Status: {}'.format(scored[key])
        else:
            print '{team}: {score}'.format(team=key, score=scored[key])


if '__main__' in __name__:
    main()

