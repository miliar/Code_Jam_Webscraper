#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;
const double pi = acos(-1);

void solve(){
	int n, k;
	cin >> n >> k;

	vector<pii> pankcake(n);

	for (int i = 0; i < n; ++i){
		cin >> pankcake[i].first >> pankcake[i].second;
	}

	sort( pankcake.begin(), pankcake.end() );

	double answer = 0;

	for (int i = k - 1; i < n; ++i){
		priority_queue<int64> pq;

		for (int j = 0; j < i; ++j){
			pq.push( -1LL * pankcake[j].first * pankcake[j].second );
			if (pq.size() > k - 1)
				pq.pop();
		}

		double cur = 0;

		while (!pq.empty()){
			cur -= pq.top(); pq.pop(); 
		}

		cur += 1LL * pankcake[i].first * pankcake[i].second;
		cur *= 2;
		cur = pi * (cur + 1LL * pankcake[i].first * pankcake[i].first);

		answer = max( answer, cur );
	}

	cout.precision(10);
	cout << fixed << answer << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

#ifdef MARX
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	int t; cin >> t;

	int tc = 1;

	while (t--){
		cout << "Case #" << tc++ << ": ";
		solve();
	}

	return 0;
}