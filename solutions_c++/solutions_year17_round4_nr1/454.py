#include<bits/stdc++.h>
using namespace std;
const bool DBG = 1;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T, N, P, a;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> N >> P;
		vector<int> mod(4);
		for(int i = 0; i < N; i++) {
			cin >> a;
			mod[a % P]++;
		}
		if(P == 2) {
			int d = mod[1] / 2;
			mod[0] += d;
			mod[1] -= 2*d;
		} else if (P == 3) {
			int b = min(mod[1], mod[2]);
			mod[0] += b;
			mod[1] -= b;
			mod[2] -= b;
		} else {
			int d = mod[2] / 2;
			mod[0] += d;
			mod[2] -= 2*d;
			int b = min(mod[1], mod[3]);
			mod[0] += b;
			mod[1] -= b;
			mod[3] -= b;
		}
		int result = 0;
		result += mod[0];
		if(P == 2) {
			result += mod[1];
		} else if(P == 3) {
			int c = max(mod[1], mod[2]);
			result += (c+2) / 3;
		} else {
			int c = max(mod[1], mod[3]);
			if(mod[2]) {
				result++;
				result += (c+1) / 4;
			} else {
				result += (c+3) / 4;
			}
		}
		cout << result << endl;
	}

	return 0;
}
