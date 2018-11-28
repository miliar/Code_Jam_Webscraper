#include <bits/stdc++.h>
using namespace std;

int t;
int n, m;
set<int> r, c, d1, d2;
char orig[1234][1234], add[1234][1234];

int main()
{
scanf("%d\n", &t);
for(int q=1; q<=t; q++) {
	scanf("%d %d\n", &n, &m);
	for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) orig[i][j]=add[i][j]=0;
	r.clear();
	c.clear();
	d1.clear();
	d2.clear();
	int score=0;
	for(int i=1; i<=n; i++) {
		r.insert(i);
		c.insert(i);
	}
	for(int i=1; i<=2*n-1; i++) {
		d1.insert(i+1);
		d2.insert(i);
	}
	for(int i=0; i<m; i++) {
		char s;
		int ro, co;
		scanf("%c %d %d\n", &s, &ro, &co);
		orig[ro][co]=s;
		score++;
		score+=(s=='o');
		if(s=='+' || s=='o') {
			d1.erase(ro+co);
			d2.erase(ro-co+n);
		}
		if(s=='x' || s=='o') {
			r.erase(ro);
			c.erase(co);
		}
	}
	while(r.size()>0 && c.size()>0) {
		int cr=*r.begin(), cc=*c.begin();
		r.erase(r.begin());
		c.erase(c.begin());
		score++;
		if(orig[cr][cc]=='+') {
			add[cr][cc]='o';
		} else {
			add[cr][cc]='x';
		}
	}
	while(d1.size()>0) {
		int cd1=*d1.begin();
		d1.erase(d1.begin());
		for(int i=min(cd1, 2*n+2-cd1)-2; i>=0; i--) {
			int cd2=n+i;
			if(d2.find(cd2)!=d2.end()) {
				d2.erase(cd2);
				int cr=(cd1+cd2-n)/2, cc=(cd1-cd2+n)/2;
				score++;
				if(orig[cr][cc]=='x' || add[cr][cc]=='x') {
					add[cr][cc]='o';
				} else {
					add[cr][cc]='+';
				}
				break;
			}
			cd2=n-i;
			if(d2.find(cd2)!=d2.end()) {
				d2.erase(cd2);
				int cr=(cd1+cd2-n)/2, cc=(cd1-cd2+n)/2;
				score++;
				if(orig[cr][cc]=='x' || add[cr][cc]=='x') {
					add[cr][cc]='o';
				} else {
					add[cr][cc]='+';
				}
				break;
			}
		}
	}
	int addcnt=0;
	for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) addcnt+=(add[i][j]!=0);
	printf("Case #%d: %d %d\n", q, score, addcnt);
	for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) {
		if(add[i][j]) {
			printf("%c %d %d\n", add[i][j], i, j);
		}
	}
}

	return 0;
}
