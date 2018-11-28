
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

main(){
	int test;scanf("%d",&test);
	FOR(casenr,1,test){
		int n,p;scanf("%d%d",&n,&p);
		int zl[5];FOR(i,0,p) zl[i]=0;
		FOR(i,1,n){
			int a;scanf("%d",&a);
			a%=p;
			zl[a]++;
		}
		int wyn=zl[0];
		if(p==2){
			wyn+=zl[1]/2+zl[1]%2;
		}
		else if(p==3){
			int k=min(zl[1],zl[2]);
			wyn+=k;
			zl[1]-=k,zl[2]-=k;
			wyn+=(zl[1]+2)/3;
			wyn+=(zl[2]+2)/3;
		}
		else{
			wyn+=zl[2]/2;
			zl[2]%=2;
			int k=min(zl[1],zl[3]);
			wyn+=k;
			zl[1]-=k,zl[3]-=k;
			//teraz zl[2]<=1, zl[1]=0 lub zl[3]=0;
			if(zl[2]==0){
				wyn+=(zl[1]+zl[3]+3)/4;
			}
			else{
				wyn+=(zl[1]+zl[3]+5)/4;
			}		
		}
		printf("Case #%d: %d\n",casenr,wyn);
	}
}
		
