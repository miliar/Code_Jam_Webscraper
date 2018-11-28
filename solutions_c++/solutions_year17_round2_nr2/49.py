#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

int main() {
	int T,t,n,r,o,y,g,b,v,first,i,j,p;
	double my,mx;
	cin>>T;
	for (t=1;t<=T;t++){
		cin>>n>>r>>o>>y>>g>>b>>v;
		printf("Case #%d: ",t);
		//only have o and b, or g and r, or v and y
		if (o+b==n || g+r==n || v+y==n) {
			if (o+b==n) {
				if (o==b) {
					for (i=0;i<o;i++) {
						printf("OB");
					}
				}
				else printf("IMPOSSIBLE");
			}
			else if (g+r==n) {
				if (g==r) {
					for (i=0;i<g;i++) {
						printf("GR");
					}
				}
				else printf("IMPOSSIBLE");
			}
			else {
				if (v==y) {
					for (i=0;i<v;i++) {
						printf("VY");
					}
				}
				else printf("IMPOSSIBLE");
			}
			printf("\n");
			continue;
		}
		//else b>=o+1,r>=g+1,y>=v+1
		if ((o>0 && b<=o) || (g>0 && r<=g) || (v>0 && y<=v)) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		b-=o;
		r-=g;
		y-=v;
		//the rest
		if (r+y<b || r+b<y || b+y<r) {
			printf("IMPOSSIBLE");
		}
		else {
			first = 0;
			while (r+y+b>0) {
				if (first ==0) {
					if (r>=y && r>=b) {
						first=1;
					}
					else if (y>=r && y>=b) {
						first = 2;
					}
					else first = 3;
					j=first;
				}
				else {
					if (p==1) {
						if (y>b) {
							j=2;
						}
						else if (y<b) {
							j=3;
						}
						else if (first==2) {
							j=2;
						}
						else j=3;
					}
					else if (p==2) {
						if (r>b) {
							j=1;
						}
						else if (r<b) {
							j=3;
						}
						else if (first==1) {
							j=1;
						}
						else j=3;
					}
					else {
						if (r>y) {
							j=1;
						}
						else if (r<y) {
							j=2;
						}
						else if (first==1) {
							j=1;
						}
						else j=2;
					}
				}
				if (j ==1) {
					r--;
					if (g>0) {
						for (;g;g--) {
							printf("RG");
						}
					}
					printf("R");
				}
				else if (j==2) {
					y--;
					if (v>0) {
						for (;v;v--) {
							printf("YV");
						}
					}
					printf("Y");
				}
				else {
					b--;
					if (o>0) {
						for (;o;o--) {
							printf("BO");
						}
					}
					printf("B");
				}
				p=j;
			}
		}
		printf("\n");
	}
    return 0;
}
