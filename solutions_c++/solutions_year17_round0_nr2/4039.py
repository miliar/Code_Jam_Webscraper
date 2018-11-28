#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

int coun;
void outt(){
	coun++;
	cout << "Case #" << coun << ": ";
}

string s;

deque<int> ans;

inline bool dfs(int b, int pr = -1, bool ok = false){
	if (b == s.size()){
		while (!ans.empty() && ans.front() == 0){
			ans.pop_front();
		}
		for (int i = 0; i < ans.size(); i++){
			cout << ans[i];
		}
		cout << endl;
		return true;
	}
	if (ok){
		ans.push_back(9);
		dfs(b + 1, 9, true);
		return true;
	}
	int val = s[b] - '0';
	for (int i = val; i >= 0; i--){
		if (pr > i){
			return false;
		}
		ans.push_back(i);
		bool nex = dfs(b + 1, i, i != val);
		ans.pop_back();
		if (nex)return true;
	}
	return false;
}

int main(){
	int t;
	cin >> t;
	while (t--){
		cin >> s;
		outt();
		dfs(0);
		ans.clear();
		s.clear();
	}
	return 0;
}