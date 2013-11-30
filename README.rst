.. contents::

Introduction
============

**mr.bob** templates : http://mrbob.readthedocs.org/en/latest/

+ basic_namespace : provide a zopeskel-like (basic_namespace) template


Installation
---------------

::
 
 easy_install bobtemplates.jpcw

or simply add bobtemplates.jpcw to your eggs zc.buildout section 

or with pip

:: 
 
 pip install bobtemplates.jpcw


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

