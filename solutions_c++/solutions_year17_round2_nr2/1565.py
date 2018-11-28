#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

typedef long long int ll;

const int MAXSIZE = 100*1000;
const int INF = 2000*1000*1000;

struct color {
	int cnt;
	char col;
};

char colors[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int m[256];

int main()
{
	ios_base::sync_with_stdio(0); cin.tie();
	for (int i=0; i<6; ++i)
		m[colors[i]] = i;
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		vector<color> v_i(6);
		int n;
		cin >> n;
		for(int i=0; i<6; ++i) {
			v_i[i].col = colors[i];
			cin >> v_i[i].cnt;
		}
		if (v_i[m['R']].cnt > v_i[m['Y']].cnt + v_i[m['B']].cnt || 
			v_i[m['Y']].cnt > v_i[m['B']].cnt + v_i[m['R']].cnt || 
			v_i[m['B']].cnt > v_i[m['Y']].cnt + v_i[m['R']].cnt) 
		{
			//cout << v_i[m['R']].cnt << ' ';
			//cout << v_i[m['Y']].cnt << ' ';
			//cout << v_i[m['B']].cnt << ' ';
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		} else {
			vector<color> v = v_i;
			sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
			
			string ans = "";
			ans += v[0].col;
			char prev = v[0].col;
			v[0].cnt--;
			
			for(int i=1; i<n; ++i) {
				int p = 0;
				while (v[p].col == prev) p++;
				ans += v[p].col;
				v[p].cnt--;
				prev = v[p].col;
				sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
			}
			//cout << ans << endl;
			if (prev == ans[0]) {

				v = v_i;
				sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
				swap(v[0], v[1]);
				ans = "";
				ans += v[0].col;
				prev = v[0].col;
				v[0].cnt--;
			
				for(int i=1; i<n; ++i) {
					int p = 0;
					while (v[p].col == prev) p++;
					ans += v[p].col;
					v[p].cnt--;
					prev = v[p].col;
					sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
				}
			}
			//cout << ans << endl;
			if (prev == ans[0]) {
				v = v_i;
				sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
				swap(v[0], v[2]);
				ans = "";
				ans += v[0].col;
				prev = v[0].col;
				v[0].cnt--;
			
				for(int i=1; i<n; ++i) {
					int p = 0;
					while (v[p].col == prev) p++;
					ans += v[p].col;
					v[p].cnt--;
					prev = v[p].col;
					sort(v.begin(), v.end(), [](const color& c1, const color& c2) {return c1.cnt > c2.cnt;});
				}
			}
			//cout << ans << endl;
			if (prev == ans[0]) {
				int l = ans.length();
				ans = ans.substr(0, l-2) + ans[l-1] + ans[l-2];
				prev = ans[l-1];
				if (ans[l-2] == ans[l-3]) prev = ans[0];
			}
			if (prev == ans[0]) {

				cout << "Case #" << t << ": IMPOSSIBLE!!!!!" << endl;
				continue;
			}
			cout << "Case #" << t << ": " << ans << endl;
		}
		
	}

	return 0;
}