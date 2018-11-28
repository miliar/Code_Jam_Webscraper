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
const double INFD=10000000000000.0;
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

int n;
double d;
double X[1010], V[1010];

bool cek(double cur) {
//	printf("%lf",cur); line;
	REP(i,0,n) {
		if (X[i]>=d-EPS) continue;
		double temp=X[i]/(cur-V[i]);
		if (cur-V[i]<EPS) return true;
//		printf("Cek : %.10lf %.10lf %.20lf",X[i],cur-V[i],X[i]/(cur-V[i])); line;
		double fak=(X[i]*cur/(cur-V[i]));
		if (fak<d-EPS) return false;
	}
	return true;
}

int main() {
	int kasus; scanf("%d",&kasus);
	REPS(ik,1,kasus) {
		scanf("%lf%d",&d,&n);
		double miskin=INFD, kaya=-INFD;
		REP(i,0,n) {
			scanf("%lf%lf",X+i,V+i); miskin=min(miskin,V[i]); kaya=max(kaya,V[i]);
		}
		double l,r,mid,ans; l=miskin; r=INFD; ans=miskin;
		REP(i,0,100) {
			if (l>r-EPS) break;
			mid=(l+r)/2;
			if (cek(mid)) ans=max(ans,mid), l=mid;
			else r=mid;
		}
		printf("Case #%d: %.6lf\n",ik,ans);
	}
	return 0;
}
/*
1
1000000000 1
999999999 100000
*/
