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

const double PI = 4 * atan(1);

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T,N,K,R,H;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> N >> K;
		vector<pair<double, double>> pan(N);
		for(int i = 0; i < N; i++) {
			cin >> R >> H;
			pan[i].first = 2 * PI * R * H;
			pan[i].second = PI * R * R;
		}
		sort(pan.begin(), pan.end());
		double aa = 0.0;
		for(int j = 0; j < K; j++) aa += pan[N-j-1].first;
		double best = 0.0;
		for(int i = 0; i < N; i++) {
			double cur = aa + pan[i].second;
			if(N-i-1 >= K) {
				//cout << "add " << i << "; remove " << N-K << endl;
				cur += pan[i].first;
				cur -= pan[N-K].first;
			}
			//cout << i << " " << cur << endl;
			best = max(best, cur);
		}
		cout << best << endl;
	}

	return 0;
}
