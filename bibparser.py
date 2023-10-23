from pybtex.database.input import bibtex

parser = bibtex.Parser()
bib_data = parser.parse_file('john.bib')

## Helpers
def fix_string(s):
	return s.replace(r"{\'e}", "é").replace(r"{\`e}", "è").replace(r"{\^e}", "ê").replace(r"{\^o}", "ô").replace("{", "").replace("}", "")


## Runner

cur_year = 2050
n_paper_in_year = 1
for i, k in enumerate(bib_data.entries.keys()):
	
	#print([str(e) for e in bib_data.entries[k].persons['author']])
	
	trs = ''
	author = fix_string('; '.join([str(e) for e in bib_data.entries[k].persons['author']]))
	title = fix_string(bib_data.entries[k].fields['title'])
	pdf = bib_data.entries[k].fields['url']
	year = bib_data.entries[k].fields['year']
	basepath = './assets/docs/'
	filename = f'{basepath}aoga_{year}_{n_paper_in_year}'
	
	if cur_year != year :
		trs = f'<tr class="yearrow">\n\t<td colspan="3">{year}</td>\n</tr>\n\n'
		cur_year = year
		n_paper_in_year = 0
	
	try:
		pub = bib_data.entries[k].fields['booktitle']
		type = 'conference'
	except KeyError:
		pub = bib_data.entries[k].fields['journal']
		type = 'journal'
		
	
	
	try:
		slideurl = bib_data.entries[k].fields['slide']
		if slideurl == '1':
			a1 = f'<a href="{filename}.pdf" class="style3" download><span class="icon solid fa-file-powerpoint"></span></a>'
		else:
			a1 = f'<a href="{slideurl}" class="style3" download><span class="icon solid fa-file-powerpoint"></span></a>'
	except KeyError:
		a1 = ''
		
	try:
		videourl = bib_data.entries[k].fields['video']
		if videourl == '1':
			a2 = f'<a href="{filename}.m4v" class="style3" download><span class="icon solid fa-file-powerpoint"></span></a>'
		else:
			a2 = f'<a href="{videourl}" class="style3" download><span class="icon solid fa-file-video"></span></a>'
	except KeyError:
		a2 = ''
	
	td1 = f'<td>{author}:<br /> <b>{title}</b>. <i>{pub}</i> <em>({type} paper)</em> </td>'
	td2 = f'<td class="pub"><a href="{pdf}" class="style1" download><strong class="icon solid fa-file-pdf"></strong></a> {a1} {a2}</td>'
	trs += f'<tr class="rowpub {type}pub">\n\t<td></td>\n\t{td1}\n\t{td2}\n</tr>\n'
	
	n_paper_in_year += 1
	
	print(trs)
	