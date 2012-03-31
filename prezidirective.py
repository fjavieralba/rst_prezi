from docutils.parsers.rst import directives, Directive
from docutils import nodes

class Prezi(Directive):
    """ Embed Prezi Presentations in posts.

        PREZI_ID is required, with / height are optional integer, 
        and text-align could be left / center / right.

        Usage:
          .. prezi:: PREZI_ID
             :width: 640
             :height: 480
             :text-align: center
    
    """

    def align(argument):
        """Conversion function for the "text-align" option."""
        return directives.choice(argument, ('left', 'center', 'right'))

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'width': directives.positive_int, 
        'height': directives.positive_int,
        'text-align': align
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        preziID = self.arguments[0].strip()
        width = 420
        height = 315
        align = 'left'
        
        if 'width' in self.options:
            width = self.options['width']

        if 'height' in self.options:
            height = self.options['height']

        if 'text-align' in self.options:
            align = self.options['text-align']

        embed_html_code = """
            <div class="prezi-player">
                <style type="text/css" media="screen">
                    .prezi-player { width: %spx; } 
                    .prezi-player-links { text-align: %s; }
                </style>
                <object id="prezi_%s" name="prezi_%s"  width="%s" height="%s">
                    <param name="movie" value="http://prezi.com/bin/preziloader.swf"/>
                    <param name="allowfullscreen" value="true"/>
                    <param name="allowscriptaccess" value="always"/>
                    <param name="bgcolor" value="#ffffff"/>
                    <param name="flashvars" value="prezi_id=%s&amp;lock_to_path=0&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0"/>

                    <embed id="preziEmbed_%s" name="preziEmbed_%s" src="http://prezi.com/bin/preziloader.swf" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="%s" height="%s" bgcolor="#ffffff" flashvars="prezi_id=%s;lock_to_path=0&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0">
                    </embed>
                </object>
            </div>
            """ % (width, align, preziID, preziID, width, height, preziID, preziID, preziID, width, height, preziID)

        return [ nodes.raw('', embed_html_code, format='html') ]

directives.register_directive('prezi', Prezi)