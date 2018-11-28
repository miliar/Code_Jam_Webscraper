#include<bits/stdc++.h>
#define FOR(i,s,e) for(int i=(s);i<=(e);i++)
#define FORD(i,s,e) for(int i=(s);i>=(e);i--)
#define ALL(k) (k).begin(),(k).end()
#define e1 first
#define e2 second
#define mp make_pair
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;
const bool print=false;
const int MAXN=1111;
int zl[MAXN][MAXN];

int pyta(int n,int c,int ll){
	int wolne=0,wynik=0;
	FOR(i,1,n){
		int ob=ll;
		FOR(j,1,c)
			ob-=zl[i][j];
		if(ob<0){
			wynik+=-ob;
		}
		wolne+=ob;
		if(wolne<0) return -1;
	}
	
	return wynik;
}


main(){
	int test;scanf("%d",&test);
	FOR(casenr,1,test){
		int n,c,m;scanf("%d%d%d",&n,&c,&m);
		FOR(i,1,n) FOR(j,1,c) zl[i][j]=0;
		FOR(i,1,m){
			int po,cu;scanf("%d%d",&po,&cu);
			zl[po][cu]++;
		}
		int lw=1,pw=m+2;
		FOR(i,1,c){
			int ss=0;
			FOR(j,1,n) ss+=zl[j][i];
			lw=max(lw,ss);
		}
		
		while(lw<pw){
			int sr=(lw+pw)/2;
			
			int ans=pyta(n,c,sr);
			if(ans!=-1) pw=sr;
			else lw=sr+1;
		}
		int odp=pyta(n,c,lw);
		FOR(i,1,n) FOR(j,1,c) zl[i][j]=0;
		printf("Case #%d: %d %d\n",casenr,lw, odp);
	}
}
			
