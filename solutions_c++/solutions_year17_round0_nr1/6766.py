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

int n,m;
char S[1010];

int main() {
	int kasus; scanf("%d",&kasus);
	REPS(ik,1,kasus) {
		scanf("%s %d",S,&m); n=strlen(S);
		int ans=0;
		REPS(i,0,n-m) {
			if (S[i]=='-') {
				ans++;
				REP(j,i,i+m) {
					if (S[j]=='-') S[j]='+';
					else S[j]='-';
				}
			}
//			printf("%s\n",S);
		}
		bool cek=false;
		REP(i,0,n) if (S[i]=='-') {
			cek=true; break;
		}
		if (cek) {
			printf("Case #%d: IMPOSSIBLE\n",ik);
		}
		else {
			printf("Case #%d: %d\n",ik,ans);
		}
	}
	return 0;
}
