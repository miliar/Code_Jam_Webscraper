
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <unordered_map>
#include <climits>
#include <cassert>
#include <unordered_set>
#include <iostream>
#define fo(x) for(int i=0; i<x; i++)
#define ii pair<int,int>
#define ll unsigned long long

using namespace std;

FILE *out = fopen("output.txt", "w");

bool tuttizero(int a, int b, int c, int d, int e) {
	if(a!=0)
		return false;
	if(b!=0)
		return false;
	if(c!=0)
		return false;
	if(d!=0)
		return false;
	if(e!=0)
		return false;
	return true;
}

void risoluzione(int y, int b, int r, int g, int v, int o) {
	char stringa[2000];
	int l = 0;
	y-=v;
	r-=g;
	b-=o;
	
	if(tuttizero(y,o,g,r,b) && v>0) {
		for(int j=0; j<v; j++) {
			fprintf(out,"YV");
		}
		return ;
	}
	if(tuttizero(y,g,r,b,v) && o>0) {
		for(int j=0; j<o; j++) {
			fprintf(out,"BO");
		}
		return ;
	}
	if(tuttizero(y,o,v,r,b) && g>0) {
		for(int j=0; j<g; j++) {
			fprintf(out,"RG");
		}
		return ;
	}
	if((y<=0 && v>0) || (r<=0 && g>0) || (b<=0 && o>0)) {
		fprintf(out,"IMPOSSIBLE");
		return ;
	}
	if(y>=r && y>=b) {
		stringa[l++] = 'Y';
		y--;
	} else if (r>=y && r>=b) {
		stringa[l++] = 'R';
		r--;
	} else  {
		stringa[l++] = 'B';
		b--;
	}
	while(y+r+b>0) {
		if(stringa[l-1] == 'Y') {
			if(stringa[0] == 'R') {
				if(r>=b) {
					stringa[l++] = 'R';
					r--;
				} else {
					stringa[l++] = 'B';
					b--;
				}
			} else {
				if(b>=r) {
					stringa[l++] = 'B';
					b--;
				} else {
					stringa[l++] = 'R';
					r--;
				}
			}
		} else if(stringa[l-1] == 'R') {
			if(stringa[0] == 'Y') {
				if(y>=b) {
					stringa[l++] = 'Y';
					y--;
				} else {
					stringa[l++] = 'B';
					b--;
				}
			} else {
				if(b>=y) {
					stringa[l++] = 'B';
					b--;
				} else {
					stringa[l++] = 'Y';
					y--;
				}
			}
		} else {
			if(stringa[0] == 'R') {
				if(r>=y) {
					stringa[l++] = 'R';
					r--;
				} else {
					stringa[l++] = 'Y';
					y--;
				}
			} else {
				if(y>=r) {
					stringa[l++] = 'Y';
					y--;
				} else {
					stringa[l++] = 'R';
					r--;
				}
			}
		}
	}
	
	if(r<0 || b<0 || y<0 || stringa[0]==stringa[l-1]) {
		fprintf(out,"IMPOSSIBLE");
		return ;
	}
	bool re=false,bl=false,ye=false;
	for(int i=0; i<l; i++){
		fprintf(out,"%c",stringa[i]);
		if(stringa[i] == 'R' && !re) {
			re = true;
			for(int j=0; j<g; j++) {
				fprintf(out,"GR");
			}
		}
		if(stringa[i] == 'Y' && !ye) {
			ye = true;
			for(int j=0; j<v; j++) {
				fprintf(out,"VY");
			}
		} 
		
		if(stringa[i] == 'B' && !bl) {
			bl = true;
			for(int j=0; j<o; j++) {
				fprintf(out,"OB");
			}
		} 
	}
}

int main() {
	int t;
	int y,b,r,g,v,o,n;
	FILE *in = fopen("input.txt", "r");
	
	fscanf(in,"%d", &t);
	for(int j=0; j<t; j++) {
		fscanf(in,"%d %d %d %d %d %d %d", &n,&r,&o,&y,&g,&b,&v);
		fprintf(out, "Case #%d: ",j+1);
		risoluzione(y,b,r,g,v,o);
		fprintf(out,"\n");
	}
	return 0;
}
