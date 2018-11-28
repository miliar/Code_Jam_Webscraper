#include <bits/stdc++.h>

#define x first
#define y second

#ifdef ONLINE_JUDGE
#define DEBUG(x)
#else
#define DEBUG(x) cerr << #x << ": " << x << endl;
#endif

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

int T,N,ct[4],P;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N >> P;
		fill(ct,ct+4,0);
		for (int i=0;i<N;i++) {
			int g;
			cin >> g;
			ct[g%P]++;
		}

		int r=0;
		r+=ct[0];
		ct[0]=0;

		for (int i=1;i<P;i++) {
			while (ct[i] && ct[P-i] && (2*i!=P || ct[i]>1)) {
				ct[i]--;
				ct[P-i]--;
				r++;
			}
		}

		for (int i=1;i<P;i++) {
			while (ct[i]>2 && 3*i%P==0) {
				ct[i]-=3;
				r++;
			}
		}

		for (int i=1;i<P;i++) for (int j=1;j<P;j++) if (i!=j && (2*i+j)%P==0) {
			while (ct[i]>1 && ct[j]) {
				ct[i]-=2;
				ct[j]--;
				r++;
			}
		}

		r+=(accumulate(ct,ct+P,0)>0);
		printf("Case #%d: %d\n",cas,r);
	}
}
