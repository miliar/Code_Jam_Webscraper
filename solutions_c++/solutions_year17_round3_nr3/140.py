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

	int T,N,K;
	double U;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> N >> K >> U;
		vector<double> p(N);
		for(int i = 0; i < N; i++) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		for(int i = 1; i < N; i++) {
			if( i * (p[i] - p[i-1]) <= U ) {
				for(int j = 0; j < i; j++) {
					U -= (p[i] - p[j]);
					p[j] = p[i];
				}
			} else {
				for(int j = 0; j < i; j++) {
					p[j] += U / i;
				}
				U = 0;
				break;
			}
		}
		for(int i = 0; i < N; i++) {
			p[i] += U/N;
		}

		double result = 1.0;
		for(int i = 0; i < N; i++) {
			result *= p[i];
		}

		cout << result << endl;
	}

	return 0;
}
