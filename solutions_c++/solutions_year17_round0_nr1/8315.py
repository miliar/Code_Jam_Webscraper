
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <utility>
using namespace std;
class state {

public:
	string n;//number
	int length;
	int ones;
	int flips;
	state(string  s){
		this->n = s;
		length = s.length();
		ones = countones(s);
		flips = countflip(s);
	}
	bool isgoal() {
		return length == ones;
	}
private:

	int countones(string& s) {
		int c = 0;
		for (int i = 0; i < s.length(); i++) {
			c += (s[i] == '+');
		}
		return c;
	}
	int countflip(string& s) {
		int c = 0;
		for (int i = 1; i < s.length(); i++) {
			c += (s[i] != s[i - 1]);
		}
		return c;
	}

};

string flip(string& s, int i, int k) {
	string z(s);
	for (int l = 0; l < k; l++, i++) {
		if (s[i] == '+')z[i] = '-';
		else if (s[i] == '-')z[i] = '+';
	}
	return z;
}
int solve(string s0, int k) {
	set<string> visited;
	queue<pair<string, int>> q;
	q.push(make_pair(s0, 0));
	
	while (!q.empty()) {
		pair<string, int> s = q.front();
		q.pop();
		if (visited.find(s.first) == visited.end()) {
			visited.insert(s.first);
			state sts(s.first);
			if (sts.isgoal())return s.second;
#ifdef DEBUG	
			cout << endl<<"@" << s.first << endl;
#endif
			for (int i = 0; i <= sts.length - k; i++) {
				string nstr = flip(s.first, i, k);
#ifdef DEBUG	
				cout <<"$"<< nstr << endl;
#endif
//				state nstate(nstr);
//				if(nstate.flips < sts.flips) 
				q.push(make_pair(nstr, s.second + 1));
			}
		}

	}

	return -1;
}

int main() {

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";
		string n;
		cin >> n;
		int k;
		cin >> k;
		
		int rc = solve(n, k);
		if (rc >= 0)
			cout << rc << '\n';
		else
			cout << "IMPOSSIBLE" << '\n';
	}
}
