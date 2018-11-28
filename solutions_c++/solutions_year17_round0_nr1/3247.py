#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

string aim;
int len;
map<string, bool> mem;

int main() {
	int T;
	cin >> T;
	for (int k = 1; k <= T; k++) {
		mem.clear();
		cout << "Case #" << k << ": ";
		cin >> aim >> len;
		string cur = aim;
		for (int i = 0; i < aim.length(); i++)
			cur[i] = '+';
		queue<string> p;
		p.push(cur);
		mem[cur] = true;
		bool flag = false;
		int c = -1;
		while (!p.empty() && !flag) {
			int s = p.size();
			while (s--) {
				cur = p.front();
				if (cur == aim) {
					flag = true;
					break;
				}
				p.pop();
				for (int i = 0; i < len; i++)
					cur[i] = 88 - cur[i];
				if (!mem[cur]) {
					mem[cur] = true;
					p.push(cur);
				}
				for (int l = 0, r = len; r < cur.length(); l++, r++) {
					cur[l] = 88 - cur[l];
					cur[r] = 88 - cur[r];
					if (!mem[cur]) {
						mem[cur] = true;
						p.push(cur);
					}
				}
			}
			c++;
		}
		if (flag) cout << c << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
