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
	cout << fixed << setprecision(6);

	int T, N;
	ll D, K, S;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> D >> N;
		double time = 0.0;
		for(int i = 0; i < N; i++) {
			cin >> K >> S;
			time = max(time, (D - K) * 1.0 / S);
		}
		cout << "Case #" << t << ": " << (D / time) << endl;
	}

	return 0;
}
