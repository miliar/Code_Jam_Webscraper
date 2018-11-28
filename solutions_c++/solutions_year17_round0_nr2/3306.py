//Author: net12k44

#include <bits/stdc++.h>
using namespace std;

string get(string s, int last){
	string res = "";
	for(int i = 0; i <= last; ++i){
		res = res + s[i];
		if (i > 0 && res[i] < res[i-1])
			return "";
	}
	
	if (res.length() == s.length())
		return res;
	
	if (s[last+1] <= s[last])
		return "";
	
	res = res + (char)(s[last+1] - 1);
	for(int i = last+2; i < s.length(); ++i)
		res = res + '9';
	
	return res;
	
}

void solve(){
	string s; cin >> s;
	s = "0" + s;
		
	for(int i = s.length()-1; i >= 0; --i){
		string cur = get(s, i);
		//cout << i << " " << s << " " << cur << endl;
		if (cur != ""){			
			while (cur.length() > 0 && cur[0] == '0')
				cur.erase(0,1);
			printf("%s\n", cur.c_str());
			return;
		}
	}	
		
	exit(1);
	
}

int main(){
	freopen("file.out","w",stdout);
	
	int test; cin >> test;
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}