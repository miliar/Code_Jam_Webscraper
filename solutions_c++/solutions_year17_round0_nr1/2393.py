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


main(){
	int test;scanf("%d",&test);
	FOR(casenr,1,test){
		string s;int k;cin>>s>>k;
		int n=(int)s.size();
		int ans=0;
		FOR(i,0,n-k){
			if(s[i]=='+') continue;
			ans++;
			FOR(j,0,k-1){
				if(s[i+j]=='+') s[i+j]='-';
				else s[i+j]='+';
			}
		}
		FOR(i,n-k+1,n) if(s[i]=='-') ans=-1;
		printf("Case #%d: ",casenr);
		if(ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
}
		
			
