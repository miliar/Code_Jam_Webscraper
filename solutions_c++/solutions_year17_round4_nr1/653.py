#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;

int solve(){
	int n, p;
	cin >> n >> p;

	vector<int> v(p);
	for (int i = 0; i < n; ++i){
		int U; cin >> U; U %= p;
		v[U]++;
	}

	if (p == 2){
		int answer = v[0];
		answer += v[1] / 2 + (v[1] & 1);
		return answer;

	}
	else if (p == 3){
		int answer = v[0] + min(v[1], v[2]);
		int k = min(v[1], v[2]); v[1] -= k; v[2] -= k;
		k = max(v[1], v[2]);
		answer += k / 3 + (k % 3 > 0);
		return answer;
	}
	else if (p == 4){
		int answer = v[0] + min(v[1], v[3]) + v[2] / 2;
		int k = min(v[1], v[3]); v[1] -= k; v[3] -= k;
		v[2] %= 2;
		k = max(v[1], v[3]);

		if (v[2] && k >= 2){
			answer++;
			v[2]--;
			k -= 2;
		}

		answer += k / 4 + ((k % 4 > 0) || v[2]);
		return answer;
	}
	return -1;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	freopen("test.in", "r", stdin);
	// freopen("test.out", "w", stdout);

	int t; cin >> t;
	int tc = 1;

	while (t--){
		cout << "Case #" << tc++ << ": " << solve() << endl;
	}
	
}