//Franciszek Budrowski

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

char a[6969];

main(){
	int test;scanf("%d",&test);
	FOR(casenr,1,test){
		scanf("%s",a+1);
		int n=0;while(a[n+1]>0) n++;
		FORD(i,n-1,1){
			if(a[i]>a[i+1]){
				a[i]--;
				FOR(j,i+1,n) a[j]='9';
			}
		}
		bool ok=false;
		printf("Case #%d: ",casenr);
		FOR(i,1,n){
			if(a[i]!='0') ok=true;
			if(ok) printf("%c",a[i]);
		}
		puts("");
	}
}
