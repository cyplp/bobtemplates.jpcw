.. contents::

Introduction
============

**mr.bob** templates : http://mrbob.readthedocs.org/en/latest/

+ basic_namespace : provide a zopeskel-like (basic_namespace) template


Installation
---------------

::
 
  - git clone -b master https://github.com/jpcw/mr.bob.git
  - cd mr.bob
  - python setup.py install
  - cd ../
  - git clone -b master https://github.com/jpcw/bobplugins.jpcw.git
  - cd bobplugins.jpcw
  - python setup.py install
  - git clone -b master https://github.com/jpcw/bobtemplates.jpcw.git
  - cd ../bobtemplates.jpcw/
  - python setup.py develop
  - easy_install . bobtemplates.jpcw[test]
  

Templates
------------

basic_namespace
++++++++++++++++++

:: 
   
 --> Namespace Package Name [paulla]:
 --> Package Name [paste]:
 --> Description:
 --> Author: 
 --> Author Email:
 --> Keywords ['']:
 --> Project URL ['']: 
 --> Project License [BSD|GPL] [BSD]:
 --> Zip-Safe [true/false] [false]:

pkg_ns (namespace) and pkg_project (package name) are guessed from -O option 

::
 
 mrbob -O paulla.paste bobtemplates.jpcw:basic_namespace

return ::
 
 --> Namespace Package Name [paulla]:
 --> Package Name [paste]:


Tests
=====

bobtemplates.jpcw is continuously 

+ tested on Travis |travisstatus|_ 

+ coverage tracked on coveralls.io |coveralls|_.

.. |travisstatus| image:: https://api.travis-ci.org/jpcw/bobtemplates.jpcw.png
.. _travisstatus:  http://travis-ci.org/jpcw/bobtemplates.jpcw


.. |coveralls| image:: https://coveralls.io/repos/jpcw/bobtemplates.jpcw/badge.png
.. _coveralls: https://coveralls.io/r/jpcw/bobtemplates.jpcw

