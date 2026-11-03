"""Rewrite the base URL in all generated IIIF manifests/collections and metadata.
Usage: python3 set_base_url.py https://your.host/path/   (run inside the release folder)
The generated NLA manifests and the collections use the placeholder https://example.org/bladwijzers/
until you publish the folder somewhere (GitHub Pages, a university web space, ...)."""
import sys, os, glob
old='https://jelmerdat.github.io/bladwijzers/'; new=sys.argv[1].rstrip('/')+'/'
n=0
for f in glob.glob('**/*.json', recursive=True)+glob.glob('*.csv'):
    t=open(f,encoding='utf-8-sig' if f.endswith('.csv') else 'utf-8').read()
    if old in t:
        open(f,'w',encoding='utf-8-sig' if f.endswith('.csv') else 'utf-8').write(t.replace(old,new)); n+=1
print(f'updated {n} files -> {new}')
