#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define pb2 pop_back
#define mp make_pair
#define REP(i,l,r) for (int i=l;i<r;i++)
#define REPS(i,l,r) for (int i=l;i<=r;i++)
#define REPD(i,l,r) for (int i=r-1;i>=l;i--)
#define REPDS(i,l,r) for (int i=r;i>=l;i--)
#define test puts("test")
#define line puts("")
#define print(x) cout<<x<<"\n"
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;

const int INF=1901486712;
const int MOD=1000000007;
const double PI=acos(-1);
const double EPS=1E-9;

bool between(int x,int l,int r) {
	return (l<=x && x<=r);
}

string tostring(int x) {
	char dum[20]; sprintf(dum,"%d",x);
	string ret(dum); return ret;
}

char S[20];

LL pangkat(LL a,LL b) {
	LL ret=1;
	REP(i,0,b) ret*=a;
	return ret;
}

bool cek(LL x) {
	char dum[20];
	sprintf(dum,"%lld",x); int p=strlen(dum);
	REP(i,1,p) if (dum[i]<dum[i-1]) return false;
	return true;
}

int main() {
	int kasus; scanf("%d",&kasus);
	REPS(ik,1,kasus) {
		LL x; scanf("%lld",&x);
		LL idx=0;
		while (true) {
			if (cek(x)) break;
			x-=pangkat(10,idx);
			sprintf(S,"%lld",x); int n=strlen(S);
			if (S[n-idx-1]=='9') idx++;
//			printf("%lld\n",x); getchar();
		}
		printf("Case #%d: %lld\n",ik,x);
	}
	return 0;
}
