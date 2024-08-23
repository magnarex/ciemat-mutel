"""
Translate a file from lines of bytes to a tabular format (.parquet).
"""
import sys
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('src_path'      , 
    help        = 'output file that will have table format (.parquet).'
)
parser.add_argument('out_path'      ,
    help        = 'which file structured in lines of bytes to translate.'
)
parser.add_argument('--lang', '-l'  , 
    dest        = 'language'        ,
    required    = True              ,
    help        = 'language from which the input file will be translate.'
)
parser.add_argument('--cfg'         ,
    dest        = 'cfg_path'        ,
    required    = True              ,
    help        = 'configuration file (.yaml) that will be used for the translation.'
)
parser.add_argument('--buffer-size' ,
    dest        = 'buffer_size'     ,
    default     = 1e5               ,
    help        = 'maximum size for the buffer (in lines). By default, 1e5.'

)
parser.add_argument('--debug'       ,
    dest        = 'debug'           ,
    action      = 'store_true'      ,
    help        = """
                    flag used to enable the debugging features. If `alive_progress` is installed,
                    this will make a progress bar appear in terminal.
                  """
)
parser.add_argument('--verbose', '-v',
    dest        = 'verbose'          ,
    action      = 'store_true'       ,
    help        = 'flag used to enable verbosity'
)


# Importing the muTel package from wherever.
import platform
parent = '/'.join(str(Path(__file__).resolve()).split('/')[:-3]) # [:-3] because this is 3 levels under the src folder
loc = parent+'/src/muTel/__init__.py'

if int(platform.python_version_tuple()[0]) == 2:
    import sys
    sys.path.insert(1, parent+'/src/')
    import muTel
    exit()  
elif int(platform.python_version_tuple()[0]) == 3:
    from pathlib import Path
    import importlib.util
    # Importing muTel package from anywhere
    parent = '/'.join(str(Path(__file__).resolve()).split('/')[:-3]) # [:-3] because this is 3 levels under the src folder
    loc = parent+'/src/muTel/__init__.py'
    src = 'muTel'
    spec = importlib.util.spec_from_file_location(src, loc)
    foo = importlib.util.module_from_spec(spec)
    sys.modules[src] = foo
    spec.loader.exec_module(foo)



args = parser.parse_args()




from muTel.daq import Translator


# Running the translator
if args.language.lower() == 'it': transr = Translator.from_it(args.cfg_path)

transr.translate(args.src_path, args.out_path,
    max_buffer  = args.buffer_size  ,
    debug       = args.debug        ,
    verbose     = args.verbose
)