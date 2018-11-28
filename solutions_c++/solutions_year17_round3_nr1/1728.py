#include <bits/stdc++.h>
using namespace std;
typedef pair<long double,long double> dd;
typedef vector<dd> vdd;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
const long double PI = acos(-1.0);

int main() {
	vdd pancakes;
	ifstream in("input.txt");
	ofstream out("output.txt");
	out << fixed;
	out << setprecision(12);
	int case_num, n, k, tmpr, tmph;
	long double tmpd, total, mx;
	in >> case_num;
	rep(i, 1, case_num + 1) {
		pancakes.clear();
		in >> n >> k;
		rep(j, 0, n) {
			in >> tmpr >> tmph;
			pancakes.push_back(make_pair((long double)tmpr, (long double)tmph));
		}
		sort(pancakes.rbegin(), pancakes.rend());
		rep(j, 0, n) {
			tmpd = 2.0 * PI * pancakes[j].first * pancakes[j].second;
			pancakes[j].first = PI * pancakes[j].first * pancakes[j].first;
			pancakes[j].second = tmpd;
		}
		mx = 0.0;
		rep(j, 0, n - k + 1) {
			total = pancakes[j].first + pancakes[j].second;
			vector<long double> q;
			rep(t, j + 1, n) {
				q.push_back(pancakes[t].second);
			}
			sort(q.rbegin(), q.rend());
			rep(t, 0, k - 1) {
				total += q[t];
			}
			mx = max(mx, total);
			cout << total << endl;
		}
		cout << endl;
		out << "Case #" << i << ": " << mx << endl;
	}
}