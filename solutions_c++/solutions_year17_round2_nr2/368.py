#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		int n,r,o,y,g,b,v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		printf("Case #%d: ", i);
		if ((r<=g && g!=0 && r+g<n)||(y<=v && v!=0 && y+v<n)||(b<=o && o!=0 && b+o<n)) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		else if ((r==g && r+g==n)||(y==v && y+v==n)||(b==o && b+o==n)) {
			for (int j=0; j<r; j++) {
				printf("RG");
			}
			for (int j=0; j<y; j++) {
				printf("YV");
			}
			for (int j=0; j<b; j++) {
				printf("BO");
			}
			printf("\n");
			continue;
		}
		r-=g==0 ? 0 : g+1; 
		y-=v==0 ? 0 : v+1;
		b-=o==0 ? 0 : o+1;
		bool zero=g==0 && v==0 && o==0;
		int tot=r+y+b; int hf=(tot+1)/2;
		//printf("%d\n", tot);
		if (r>hf||y>hf||b>hf) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		else if (tot%2==1 && (r==hf||y==hf||b==hf) && zero) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int prev=-1;
		string s="";
		for (int j=0; j<tot; j++) {
			if (prev==0) {
				if (b>=y) {
					s+="B";
					b--;
					prev=1;
				}
				else {
					s+="Y";
					y--;
					prev=2;
				}
			}
			else if (prev==1) {
				if (r>=y) {
					s+="R";
					r--;
					prev=0;
				}
				else {
					s+="Y";
					y--;
					prev=2;
				}
			}
			else {
				if (r>=b) {
					s+="R";
					r--;
					prev=0;
				}
				else {
					s+="B";
					b--;
					prev=1;
				}
			}
			//printf("%d %d %d %s\n", r, b, y, s.c_str());
		}
		int ord[3];
		if (s.length()==0 || s[0]==0) {
			if (prev!=1) {
				ord[0]=1; ord[1]=0; ord[2]=2;
			}
			else {
				ord[0]=2; ord[1]=0; ord[2]=1;
			}
		}
		else if (s[0]==1) {
			if (prev!=0) {
				ord[0]=0; ord[1]=1; ord[2]=2;
			}
			else {
				ord[0]=2; ord[1]=1; ord[2]=0;
			}
		}
		else {
			if (prev!=0) {
				ord[0]=0; ord[1]=2; ord[2]=1;
			}
			else {
				ord[0]=1; ord[1]=2; ord[2]=0;
			}
		}
		for (int j=0; j<3; j++) {
			if (ord[j]==0) {
				if (g==0) continue;
				for (int k=0; k<g; k++) {
					s+="RG";
				}
				s+="R";
			}
			else if (ord[j]==1) {
				if (o==0) continue;
				for (int k=0; k<o; k++) {
					s+="BO";
				}
				s+="B";
			}
			else {
				if (v==0) continue;
				for (int k=0; k<v; k++) {
					s+="YV";
				}
				s+="Y";
			}
		}
		printf("%s\n", s.c_str());
	}
}
