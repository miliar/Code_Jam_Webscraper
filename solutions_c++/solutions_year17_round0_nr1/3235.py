#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <algorithm>
#include <map>
using namespace std;


map<string, int> vis;

int solve(string f, int k) {
	vis.clear();
	string a;
	for (int i = 0; i < f.size(); ++i) {
		a += '+';
	}
	queue<pair<string, int> > q;
	q.push({ a, 0 });
	vis[a] = 1;
	while (!q.empty()) {
		auto c = q.front();
		if (c.first == f)
		{
			return c.second;
		}
			q.pop();
//		cout << c.first << ' ' << c.second << endl;
		for (int i = k-1; i < a.size(); ++i){
			for (int j = i-k+1; j <= i; ++j) {
				c.first[j] = c.first[j] == '+'?'-':'+';
			}
			if (vis[c.first]++)
				goto kek;

			q.push({ c.first,c.second + 1 });


		kek:;
			for (int j = i - k + 1; j <= i; ++j) {
				c.first[j] = c.first[j] == '+' ? '-' : '+';
			}
		}

	}
	
	
	return -1;
}

int main() {
	ifstream in("test.in");
	ofstream out("test.out");

	int n;
	in >> n;
	for (int i = 1; i <= n; ++i) {
		int k;
		string st;
		in >> st >> k;
		int sol=-1337;

		if (k == 1) {
			sol = count(st.begin(), st.end(), '-');
		}

		if (st.size() == count(st.begin(), st.end(), '+'))
			sol = 0;
		
		if(sol==-1337)
		sol = solve(st, k);
		if (sol == -1)
		{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			out << "Case #" << i << ": IMPOSSIBLE" << endl;

		}
		else {
			cout << "Case #" << i << ": " << sol << endl;
			out << "Case #" << i << ": " << sol << endl;
		}
		}

	return 0;
}