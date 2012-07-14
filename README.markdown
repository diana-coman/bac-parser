This is a scraping script for extracting the results of the
[Romanian Baccalaureate][1] from http://bacalaureat.edu.ro for the years
2006 - 2011.

[1]: http://en.wikipedia.org/wiki/Romanian_Baccalaureate

Installation and Requirements
=============================

 - python 2.7
 - [python-lxml](http://lxml.de/)
 - [PylibLZMA](https://launchpad.net/pyliblzma) (for LZMA/XZ compressed files)
 - python-argparse (on Python 2.6)

Fedora 15
---------

    yum install python-lxml pyliblzma

Enterprise Linux 6
------------------

    yum install python-lxml pyliblzma python-argparse


Usage
=====

First you need to get the HTML pages that will be parsed. You can download them
with a browser or you can use a spider, whatever fits you. Then you can parse
them.


Basic usage
-----------

    ./main.py data/alfabetic_page_4.html

outputs:

    Elev(nume=u'John Doe', scoala=u'Summer school', judet=u'B', promotie_anterioara=u'NU', forma_invatamant=u'Zi', specializare=u'Tehnician in activitati economice', d_romana_competente=u'Utilizator avansat', d_romana_scris_nota=u'5.45', d_romana_scris_nota_contestatie=u'', d_romana_scris_nota_finala=u'5.45', d_limba_materna_nume=u'', d_limba_materna_competente=u'', d_limba_materna_scris_nota=u'', d_limba_materna_scris_nota_contestatie=u'', d_limba_materna_scris_nota_finala=u'', d_limba_moderna_nume=u'Limba engleza', d_limba_moderna_nota=u'B2-A2-B2-B1-B1', d_profil_scris_nume=u'Matematica T2', d_profil_scris_nota=u'5', d_profil_scris_nota_contestatie=u'', d_profil_scris_nota_finala=u'5', d_alegere_scris_nume=u'Economie', d_alegere_scris_nota=u'8.05', d_alegere_scris_nota_contestatie=u'', d_alegere_scris_nota_finala=u'8.05', d_competente_digitale=u'Utilizator experimentat', rezultat_final=u'Reu\u015fit')
    #######################################################################
    ...
    #######################################################################
    Elev(nume=u'Joahna Doe', scoala=u'Winter school', judet=u'B', promotie_anterioara=u'NU', forma_invatamant=u'Zi', specializare=u'Tehnician in activitati economice', d_romana_competente=u'Utilizator avansat', d_romana_scris_nota=u'5.45', d_romana_scris_nota_contestatie=u'', d_romana_scris_nota_finala=u'5.45', d_limba_materna_nume=u'', d_limba_materna_competente=u'', d_limba_materna_scris_nota=u'', d_limba_materna_scris_nota_contestatie=u'', d_limba_materna_scris_nota_finala=u'', d_limba_moderna_nume=u'Limba engleza', d_limba_moderna_nota=u'B2-A2-B2-B1-B1', d_profil_scris_nume=u'Matematica T2', d_profil_scris_nota=u'5', d_profil_scris_nota_contestatie=u'', d_profil_scris_nota_finala=u'5', d_alegere_scris_nume=u'Economie', d_alegere_scris_nota=u'8.05', d_alegere_scris_nota_contestatie=u'', d_alegere_scris_nota_finala=u'8.05', d_competente_digitale=u'Utilizator experimentat', rezultat_final=u'Reu\u015fit')

You can parse multiple files in one run. In order to save disk space, reading
from compressed files is supported (formats: gzip, bzip2, lzma/xz).

You can specify the year of the exam with the `--year` parameter. By the
default it's the last year supported.

Other output formats
--------------------

If you're planning to analyze the results, you can dump them in the
**[pickle]** format. Then either read the pickle file from Python or convert it
to a **CSV** file using `pickle2csv.py`. From there on, the sky's the limit.
Here's an example:

    ./main.py --format pickle data/alfabetic_page_4.html.xz | xz --best > results.pickle.xz
    ./pickle2csv.py results.pickle.xz > results.csv

The pickle file is actually composed of multiple pickle dumps in order to
minimize the memory usage, so you'll need to load pickles from it until `EOF`.

As you can see, `pickle2csv` supports compressed files, too.

The `--year` parameter works in the same way as for `main`.

If you don't need the pickle files, you can do it in a single step:

    ./main.py --format pickle data/alfabetic_page_4.html.xz | ./pickle2csv.py - > results.csv

[pickle]: http://docs.python.org/library/pickle.html


Copyright and License
=====================

The code is too simple and too ugly to require legal paperwork, so I declare
it public domain.


Credits
=======

This wouldn't have been possible without the [Sothink SWF Decompiler][2]. Shame
on Siveco for using Flash even if it wasn't really needed.

[2]: http://www.sothink.com/product/flashdecompiler/
