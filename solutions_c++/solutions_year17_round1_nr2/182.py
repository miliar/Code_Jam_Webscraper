#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

const int mod=1000000000+7;

int addm(int& a,int b) {return (a+=b)<mod?a:a-=mod;}

template<class T,class U> bool smin(T& a,U b) {return a>b?(a=b,1):0;}
template<class T,class U> bool smax(T& a,U b) {return a<b?(a=b,1):0;}

ll T,N,P,R[50],Q[50][50];
//int ct[50][2000000];
typedef pair<pll,ll> tll;
int ct[51],used[50];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N >> P;
		//map<int,vi> ct;
		vector<tll> ivs;
		for (int i=0;i<N;i++) cin >> R[i];
		for (int i=0;i<N;i++) for (int j=0;j<P;j++) {
			cin >> Q[i][j];
			ll high=(10*Q[i][j])/(9*R[i]);
			ll low=(10*Q[i][j]+11*R[i]-1)/(11*R[i]);
			ivs.emplace_back(pll{low,high+1},i);
			//cerr << low << ' ' << high << ' ' << i << endl;
		}
		sort(ivs.begin(),ivs.end());
		ll r=0;
		for (int i=0;i<ivs.size();i++) {
			ll v=ivs[i].x.x;
			if (v<=0) continue;
			fill(ct,ct+N,0);
			for (tll &a:ivs) if (a.x.x<=v && v<a.x.y) ct[a.y]++;
			ll m=*min_element(ct,ct+N);
			r+=m;
			fill(ct,ct+N,m);
			for (tll &a:ivs) if (a.x.x<=v && v<a.x.y && ct[a.y]) {
				ct[a.y]--;
				a.y=N;
			}
		}

		printf("Case #%d: %lld\n",cas,r);
	}

}
