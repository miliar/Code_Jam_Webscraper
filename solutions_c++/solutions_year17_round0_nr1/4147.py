#include<bits/stdc++.h>
using namespace std;
#define REP(_x,_y) for(int (_x)=0;(_x)<(_y);(_x)++)
#define FOR(_x,_y,_z) for(int (_x)=(_y);(_x)<=(_z);(_x)++)
#define FORD(_x,_y,_z) for(int (_x)=(_y);(_x)>=(_z);(_x)--)
#define RESET(_x,_y) memset((_x),(_y),sizeof(_x))
#define SZ(_x) ((int)(_x).size())
#define LEN(_x) strlen(_x)
#define ALL(_x) (_x).begin(),(_x).end()
#define LL long long
#define ULL unsigned LL
#define PII pair<int,int>
#define VI vector<int>
#define VII vector< PII >
#define VVI vector< VI >
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
const int INF=1e9;
const int MOD=1e9+7;
// >.<
int t,tc=1,n,k;
char s[1001];
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%s %d",&s,&k);
		n=LEN(s);
		int an=0;
		FOR(i,0,n-k){
			if(s[i]=='+')continue;
			an++;
			FOR(j,i,i+k-1){
				if(s[j]=='-')s[j]='+';
				else s[j]='-';
			}
		}
		bool can=1;
		REP(i,n){
			if(s[i]=='-')can=0;
		}
		printf("Case #%d: ",tc++);
		if(!can)puts("IMPOSSIBLE");
		else printf("%d\n",an);
	}
	return 0;
}