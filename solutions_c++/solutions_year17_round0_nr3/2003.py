#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;

void solve(int64 n, int64 k){
	map<int64,int64> freq;
	freq[n] = 1;

	while (true){
		auto cur = *freq.rbegin();

		int64 a = cur.first / 2;
		int64 b = cur.first - a - 1;

		if (cur.second >= k){
			cout << a << " " << b << endl;
			return;
		}

		k -= cur.second;

		freq.erase( cur.first );
		freq[ a ] += cur.second;
		freq[ b ] += cur.second;
	}
}

int main(){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);

	int t; cin >> t;
	int tc = 1;

	while (t--){
		int64 n, k;
		cin >> n >> k;

		cout << "Case #" << tc++ << ": ";
		solve(n, k);
	}
}