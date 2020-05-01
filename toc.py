#!/usr/bin/python3

from re import *
import os

with open('creche.toc', 'r') as f:
    toc = f.read()
    f.closed

p = compile('.*\{Preface\}.*')
toc = p.sub('*  **Preface**', toc)
p = compile('.*contentsfinish\s\n')
toc = p.sub('', toc)

p = compile('\\\\contentsline\s\{chapter\}\{\\\\numberline\s\{\d*\}')
toc = p.sub('*  **', toc)
p = compile('\\\\contentsline\s\{section\}\{\\\\numberline\s\{\d*\}')
toc = p.sub('   * ', toc)
p = compile('\}\{\d*\}\{chapter.*')
toc = p.sub('**', toc)
p = compile('\}\{\d*\}\{.*')
toc = p.sub('', toc)
toc = toc.replace(r'\contentsline {chapter}{Preface}{4}{chapter*.2}\n', '')


p = compile('\\\\IeC\s\{\\\\"o\}')
toc = p.sub('&ouml;', toc)

p = compile('\\\\IeC\s\{\\\\"i\}')
toc = p.sub('&iuml;', toc)

p = compile('\\\\"i')
toc = p.sub('&iuml;', toc)

p = compile('\\\\IeC\s\{\\\\\'e\}')
toc = p.sub('&eacute;', toc)


with open('README.md', 'r') as f:
    readme = f.read()
    f.closed
p = compile('##\sTable\sof\scontents.*', DOTALL)
readme = p.sub('', readme)
readme = readme + '## Table of contents\n\n' + toc

with open('README.md', 'w') as f:
    f.write(readme)
    f.closed
