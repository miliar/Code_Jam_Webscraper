"""
(a->y), (b->h) ,(c->e), (d->s),(e->o), (f->c) , (g->v) , (h->x) ,(i->d),(j->u),  (k->i), (l->g) , (m->l),(n->b),(o->k),
 (p->r), (q->z) , (r->t) ,(s->n) ,(t->w), (u->j) , (v->p) , (w->f) ,(x->m),(y->a),(z->q)
"""
dict = {'a':'y','b':'h','c':'e', 'd':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u', 
 'k':'i', 'l':'g', 'm':'l','n':'b','o':'k','p':'r','q':'z','r':'t' ,'s':'n','t':'w',
  'u':'j','v':'p', 'w':'f','x':'m','y':'a','z':'q'
}
def googlers():
	input=open("A-small-attempt0.in","r")
	output=open("op.txt","w")
	numb = input.readline()
	numb = int(numb)
	for i in range(0,numb):
		stri = ''
		st = input.readline()
		for each in st:
			if each!=' ':
				if each in dict:
					stri += dict[each]
			else:
				stri += each
			d = str(i+1)
		output.write("Case #"+d+": "+stri+"\n")
googlers()