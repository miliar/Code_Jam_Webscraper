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
int t,tc=1,len;
char num[21];
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%s",&num);
		len=LEN(num);
		bool ok=1;
		FOR(i,1,len-1){
			if(num[i]<num[i-1])ok=0;
		}
		if(!ok){
			FORD(i,len-1,0){
				if(num[i]!='0'){
					bool can=1;
					num[i]--;
					FOR(j,1,i){
						if(num[j]<num[j-1])can=0;
					}
					if(can){
						FOR(j,i+1,len-1){
							num[j]='9';
						}
						break;
					}
					num[i]++;
				}
			}
		}
		printf("Case #%d: ",tc++);
		bool b=0;
		REP(i,len){
			if(num[i]!='0')b=1;
			if(b)printf("%c",num[i]);
		}
		puts("");
	}
	return 0;
}