#include <bits/stdc++.h>

using namespace std;

int n,r,o,y,g,b,v; 

bool rf,yf,bf;

void pr(){
	if (rf) {
		for(int i=0; i<g; ++i){
			putchar('R');
			putchar('G');
		}
		rf = false;
	}
	putchar('R');		
}
void py(){
	if (yf) {
		for(int i=0; i<v; ++i){
			putchar('Y');
			putchar('V');
		}
		yf = false;
	}
	putchar('Y');		
}
void pb(){
	if (bf) {
		for(int i=0; i<o; ++i){
			putchar('B');
			putchar('O');
		}
		bf = false;
	}
	putchar('B');		
}


int main(){
	int t; scanf("%d", &t);
	for (int i=1; i<=t; ++i){
		printf("Case #%d: ", i);
		
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		if (o==b && o+b==n){
			for (int j=0; j<o; ++j) printf("BO");
			printf("\n");
			continue;
		}
		if (g==r && g+r==n){
			for (int j=0; j<g; ++j) printf("RG");
			printf("\n");
			continue;
		}
		if (v==y && v+y==n){
			for (int j=0; j<v; ++j) printf("YV");
			printf("\n");
			continue;
		}
		
		if (o>0&&o>=b || g>0&&g>=r || v>0&&v>=y){
			printf("IMPOSSIBLE\n");
			continue;
		} 
		
		if (o>0) b=b-o;
		if (g>0) r=r-g;
		if (v>0) y=y-v;
		
		rf=yf=bf=true;
		
		if (b>=r && b>=y){
			if (b>r+y) printf("IMPOSSIBLE\n");
			else {
				while (b<r+y) {
					pb();
					pr();
					py();
					--b,--r,--y;
				}
				while (r>0){
					pb();
					pr();
					--b,--r;
				}
				while (y>0){
					pb();
					py();
					--b,--y;
				}
				putchar('\n');
			}
		}
		else if(r>=b && r>=y){
			if (r>b+y) printf("IMPOSSIBLE\n");
			else {
				while (r<b+y) {
					pr();
					pb();
					py();
					--b,--r,--y;
				}
				while (b>0){
					pr();
					pb();
					--b,--r;
				}
				while (y>0){
					pr();
					py();
					--r,--y;
				}
				putchar('\n');
			}
		}
		else{
			if (y>r+b) printf("IMPOSSIBLE\n");
			else {
				while (y<r+b) {
					py();
					pr();
					pb();
					--b,--r,--y;
				}
				while (r>0){
					py();
					pr();
					--y,--r;
				}
				while (b>0){
					py();
					pb();
					--b,--y;
				}
				putchar('\n');
			}
		}
		
	}
}
