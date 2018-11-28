#include <bits/stdc++.h>
#define M 1000
using namespace std;
int r,o,y,g,b,v,n;
bool cr,cy,cb;

void pr(void){
	if(cr)printf("R");
	else{
		while(g--)printf("RG");
		printf("R");
		cr=true;
	}
}

void py(void){
	if(cy)printf("Y");
	else{
		while(v--)printf("YG");
		printf("Y");
		cy=true;
	}
}

void pb(void){
	if(cb)printf("B");
	else{
		while(o--)printf("BO");
		printf("B");
		cb=true;
	}
}
int main(){
	freopen("input.txt","r",stdin);

	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
		cr=cy=cb=false;
		if(n==r+g){
			if(r!=g){printf("IMPOSSIBLE\n"); continue;}
			while(r--){printf("RG");}
			printf("\n");
			continue;
		}
		if(n==y+v){
			if(y!=v){printf("IMPOSSIBLE\n"); continue;}
			while(y--){printf("YV");}
			printf("\n");
			continue;
		}
		if(n==b+o){
			if(b!=o){printf("IMPOSSIBLE\n"); continue;}
			while(b--){printf("BO");}
			printf("\n");
			continue;
		}
		if(r<g || y<v || b<o){printf("IMPOSSIBLE\n"); continue;}
		if(r+g==0){
			if(y<=v || b<=o){printf("IMPOSSIBLE\n"); continue;}
			if(y-v!=b-o){printf("IMPOSSIBLE\n"); continue;}
			y-=v;
			while(y--){py();pb();}
			printf("\n");
			continue;
		}
		if(y+v==0){
			if(r<=g || b<=o){printf("IMPOSSIBLE\n"); continue;}
			if(r-g!=b-o){printf("IMPOSSIBLE\n"); continue;}
			r-=g;
			while(r--){pr();pb();}
			printf("\n");
			continue;
		}
		if(b+o==0){
			if(r<=g || y<=v){printf("IMPOSSIBLE\n"); continue;}
			if(r-g!=y-v){printf("IMPOSSIBLE\n"); continue;}
			r-=g;
			while(r--){pr();py();}
			printf("\n");
			continue;
		}
		r-=g; y-=v; b-=o;
		if(r>=y && r>=b){
			if(r>y+b){printf("IMPOSSIBLE\n");continue;}
			while(y+b-r){pr();py();pb();r--;y--;b--;}
			while(y--){pr();py();}
			while(b--){pr();pb();}
			printf("\n");
			continue;
		}
		if(y>=r && y>=b){
			if(y>r+b){printf("IMPOSSIBLE\n");continue;}
			while(r+b-y){py();pr();pb();y--;r--;b--;}
			while(r--){py();pr();}
			while(b--){py();pb();}
			printf("\n");
			continue;
		}
		if(b>=r && b>=y){
			if(b>r+y){printf("IMPOSSIBLE\n");continue;}
			while(r+y-b){pb();pr();py();b--;r--;y--;}
			while(r--){pb();pr();}
			while(y--){pb();py();}
			printf("\n");
			continue;
		}
	}
}
