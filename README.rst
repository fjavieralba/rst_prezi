Pelican-Prezi
#############

This small piece of code is an rst directive that allows you to embed prezi_ presentations in your rst docs. This can be used in Pelican blog generator since it uses rst as it source for generating pages.

Usage
-----

.. code-block: rst

	.. prezi:: <PREZI_ID>
 	  :width: 640
 	  :height: 480
 	  :text-align: center

Install
-------

If you want to easily embed prezi presentations in your pelican blog, all you have to do is:

 - Download the prezidirective.py file
 - Download the pelican code
 - Add prezidirective.py to the ``pelican/pelican`` folder
 - Modify the file ``pelican/pelican/readers.py`` and add the following import:

.. code-block:: python

	from pelican import prezidirective

 - Install pelican from source:

.. code-block:: bash

	$ cd <pelican_home>
	$ python setup.py install

And voilà, you can use the ``prezi`` directive to embed your presentations.


