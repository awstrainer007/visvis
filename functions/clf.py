# -*- coding: utf-8 -*-
# Copyright (c) 2010, Almar Klein
#
# Visvis is distributed under the terms of the (new) BSD License.
# The full license can be found in 'license.txt'.

import visvis as vv

def clf():
    """ clf()
    
    Clear current figure. 
    
    """
    f = vv.gcf()
    f.Clear()
    return f
