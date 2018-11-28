#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

string res;

void solve()
{
	res = "";
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;

	priority_queue<pair<int, char> > q;

	int tot = N;

	q.push(make_pair(R, 'R'));
	//q.push(make_pair(O, 'O'));
	q.push(make_pair(Y, 'Y'));
	//q.push(make_pair(G, 'G'));
	q.push(make_pair(B, 'B'));
	//q.push(make_pair(V, 'V'));

	int idx = 0;
	while (tot > 0) {

		pair<int, char> p = q.top();
		q.pop();

		if (idx == 0) {
			res += p.second;
			q.push(make_pair(p.first - 1, p.second));
			idx++;
			tot--;
			continue;
		}

		if (res[idx - 1] != p.second) {
			pair<int, char> p2 = q.top();
			if (p2.first == p.first && res[0] == p2.second && p2.second != res[idx - 1]) {
				q.pop();
				q.push(make_pair(p.first, p.second));
				q.push(make_pair(p2.first - 1, p2.second));
				res += p2.second;
			} else {
				q.push(make_pair(p.first - 1, p.second));
				res += p.second;
			}
		} else {
			if (q.top().first == 0) {
				cout << "IMPOSSIBLE";
				return;
			}
			pair<int, char> p2 = q.top();
			q.pop();

			pair<int, char> p3 = q.top();
			if (p3.first == p2.first && res[0] == p3.second && p3.second != res[idx - 1]) {
				q.pop();
				q.push(make_pair(p2.first, p2.second));
				q.push(make_pair(p3.first - 1, p3.second));
				res += p3.second;
			} else {
				res += p2.second;
				q.push(make_pair(p2.first - 1, p2.second));
				q.push(make_pair(p.first, p.second));
			}
		}
		tot--;
		idx++;
	}

	if (res[0] == res[res.size() - 1]) cout << "IMPOSSIBLE";
	else cout << res;

}


int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
