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
VII v;
void go(int l,int r){
	if(l<=r){
		int m=(l+r)/2;
		int x=min(m-l,r-m);
		int y=max(m-l,r-m);
		v.PB({x,y});
		go(l,m-1);
		go(m+1,r);
	}
}
bool cmp(const PII &x,const PII &y){
	return (x.FI==y.FI)?(x.SE>y.SE):(x.FI>y.FI);
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&k);
		v.clear();
		go(1,n);
		sort(ALL(v),cmp);
		printf("Case #%d: %d %d\n",tc++,v[k-1].SE,v[k-1].FI);
	}
	return 0;
}