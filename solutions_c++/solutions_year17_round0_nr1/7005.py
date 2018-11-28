#include <iostream>
#include <set>
#include <queue>
using namespace std;

int bfs(string s, string final_str, int k) {
	set<string> set_str;
	queue<pair<string, int> > q;

	q.push(make_pair(s,0));

	while(!q.empty()) {
		pair<string,int> cur = q.front();
		q.pop();
		if(cur.first == final_str) {
			return cur.second;
		}
		string str = cur.first;
		for(int i = 0; i <= str.length() - k; i++) {
			string next(str);
			for(int j = i; j <= i + k -1; j++) {
				if(next[j] == '+')
					next[j] = '-';
				else
					next[j] = '+';
			}
			if(set_str.count(next) == 0) {
				//cout << next << " " << cur.second + 1 << endl;
				set_str.insert(next);
				q.push(make_pair(next, cur.second + 1));
			}
		}
	}
	return -1;
}

bool allPlus(string s) {
	for(int i = 0; i < s.length(); i++) {
		if(s[i] != '+')
			return false;
	}
	return true;
}

int simulate(string s, int k) {
	int cnt = 0;
	for(int i = 0; i < s.length() - k + 1; i++) {
		if(s[i] == '-') {
			cnt++;
			for(int j = i; j <= i+k-1; j++) {
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	if(allPlus(s))
		return cnt;
	return -1;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		string s;
		int k;
		cin >> s >> k;
		string final_str(s.length(),'+');
		/*
		if(simulate(s,k) != bfs(s,final_str,k))
			cout << s << " " << k << " " << simulate(s,k) << " " << bfs(s,final_str,k) << endl;
		*/
		int ans = simulate(s,k);
		if(ans == -1)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
	}
}
