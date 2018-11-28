#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define debug(a) cerr<< #a << " = " << (a) << endl;
typedef long long ll;
typedef pair<int , int > pii;
typedef vector<int > vi;
typedef vector<vi > vvi;
template <typename T> ostream& operator <<( ostream& o, vector <T>& v) {
for (auto& a: v) o << a << ' ';
	return o;
}
int r[100];
int q[100][100];
pii ranges[100][100];

bool works(int required, int quantity, int serves) {
	return (required * serves * 9 <= 10 * quantity) && (10 * quantity <= required * serves * 11);
}

void do_case() {
	int ans = 0;

	int n, p;
	cin >> n >> p;

	for (int i = 0 ; i < n; i++) {
		cin >> r[i];
	}

	for (int i = 0 ; i < n; i++) {
		// debug(i)
		for (int j = 0; j < p ;j++) {
			cin >> q[i][j];
			// // make range
			// // binary search!
			// {
			// 	int best_so_far = -1;
			// 	int lo = 0;
			// 	int hi = q[i][j] * 2;
			// 	while (lo <= hi) {
			// 		int mid = (lo + hi) / 2;
			// 		if (r[i] * mid <= q[i][j])
			// 	}
			// }
			// debug(j)
			ranges[i][j].Y = (q[i][j] * 10 + 9 * r[i] - 1) / (9 * r[i]);
			// debug(ranges[i][j].Y);
			while ((!works(r[i], q[i][j], ranges[i][j].Y)) && ranges[i][j].Y >= ranges[i][j].X) {
				ranges[i][j].Y--;
			}
			
			ranges[i][j].X = (q[i][j] * 10) / (11 * r[i]);
			// debug(ranges[i][j].X);
			while ((!works(r[i], q[i][j], ranges[i][j].X)) && ranges[i][j].Y >= ranges[i][j].X) {
				ranges[i][j].X++;
			}
			// debug(ranges[i][j].Y);
			// debug(ranges[i][j].X);
			// cerr << endl;
		}
		// cerr << endl;
		sort(ranges[i], ranges[i] + p);
	}

	// greedily take 

	int cur_pos[n];
	fill(cur_pos, cur_pos+n, 0);

	// debug


	while (true) {
		// check whether cur_pos is bad
		{
			bool bad = false;
			for (int i = 0; i < n; i++) {
				if (cur_pos[i] >= p) {
					bad = true;
					break;
				}
			}
			if (bad) break;
		}
		// first find max range
		pii max_range;
		for (int i = 0; i < n; i++) {
			max_range = max(max_range, ranges[i][cur_pos[i]]);
		}

		// then check whether any need fixing
		{
			bool bad = false;
			for (int i = 0; i < n; i++) {
				if (max_range.X > ranges[i][cur_pos[i]].Y) {
					bad = true;
					cur_pos[i]++;
				}
			}
			if (!bad) {
				// take one
				ans++;
				for (int i = 0; i < n; i++) {
					cur_pos[i]++;
				}
			}
		}
	}

	cout << ans << endl;
}

int main () {
	ios::sync_with_stdio (0);cin.tie (0);
	int cases;
	cin >> cases;
	for (int c = 0; c < cases; c++) {
		cout << "Case #" << (c+1) << ": ";
		do_case();
	}
}

