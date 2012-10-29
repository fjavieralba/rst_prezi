rst_prezi
#########

This small piece of code is an rst directive that allows you to embed prezi_ presentations in your rst_ docs. This can be used in Pelican_ blog generator since it uses rst as it source for generating pages.

Usage
-----

::

	.. prezi:: <PREZI_ID>
 	  :width: 640
 	  :height: 480
 	  :text-align: center


To know your ``PREZI_ID`` simply go to your presentation in prezi_ and click on *"share"* option. The URL you see contains your ``PREZI_ID``: http://prezi.com/PREZI_ID/some_title/

Install on Pelican
------------------

If you want to easily embed prezi presentations in your pelican blog, all you have to do is:

 - Download the prezidirective.py file
 - Download the pelican code
 - Add prezidirective.py to the ``pelican/pelican`` folder
 - Modify the file ``pelican/pelican/readers.py`` and add the following import:

    ::

	   from pelican import prezidirective

 - Install pelican from source:

    ::

	   $ cd <pelican_home>
	   $ python setup.py install

And voilà, you can use the ``prezi`` directive to embed your presentations.

.. _prezi: http://prezi.com/
.. _rst: http://docutils.sourceforge.net/rst.html
.. _Pelican: http://blog.notmyidea.org/pelican-a-simple-static-blog-generator-in-python.html

