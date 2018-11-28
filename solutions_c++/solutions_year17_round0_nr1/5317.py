#include <bits/stdc++.h>

using namespace std;

string copy(string s) {
	string res;
	for (int i=0; i<s.size(); i++) {
		res.push_back(s[i]);
	}
	return res;
}

string flip(string s, int st, int e) {
	string n = copy(s);
	for (int i=st; i<e; i++) {
		if (n[i] == '+')
			n[i] = '-';
		else
			n[i] = '+';
	}
	return n;
}

int main() {
	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		string s;
		int k;
		cin >> s >> k;
		set<string> v;
		deque< pair <string, int> > q;
		q.push_back({s, 0});
		bool found = false;
		while(! q.empty()) {
			if (v.find(q.front().first) != v.end()) {
				q.pop_front();
				continue;
			}
			if (q.front().first.find("-") == string::npos) {
				cout << "Case #" << i << ": " << q.front().second << endl;
				found = true;
				break;
			}
			for (int i=0; i<=s.size()-k; i++) {
				string n = flip(q.front().first, i, i+k);
				if (v.find(n) == v.end()) q.push_back({n, q.front().second+1});
			}
			v.insert(q.front().first);
			q.pop_front();
			//for (auto i : q) cout << i.first << " ";
			//cout << endl;
		}
		if (! found)
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
