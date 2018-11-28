#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

string N;
int T;

string memo[20][2][15];

void clear() {
	for(int i=0; i<20; ++i)
		for(int j=0; j<2; ++j)
			for(int r=0; r<15; ++r)
				memo[i][j][r] = "-1";
}

bool mor(string a, string &b) {
	if (a.size() < b.size()) return false;
	if (a.size() > b.size()) return true;
	for(int i=0; i<a.size(); ++i) {
		if (a[i] < b[i]) return false;
		if (a[i] > b[i]) return true;
	}
	return false;
}

bool invalid(string &s) {
	for(int i=0; i<s.size(); ++i) {
		if (s[i] == '$')
			return true;
	}
	return false;
}

string f(int pos, bool menor, int last) {
	if (pos == N.size()) {
		return "";
	}
	
	if (memo[pos][menor][last] != "-1")
		return memo[pos][menor][last];
	
	string ans = "$";
	
	if (menor == 1) {
		for(int d=last; d<=9; ++d) {
			string news = string(1, '0' + d) + f(pos+1, 1, d);
//			cout<<pos<<" "<<news<<endl;
			if (!invalid(news) && mor(news, ans)) {
				ans = news;
			}
		}
	} else {
		for(int d=last; d<=(N[pos]-'0'); ++d) {
			string news = string(1, '0' + d) + f(pos+1, (d==(N[pos]-'0'))?0:1 , d);
//			cout<<pos<<" "<<news<<endl;
			if (!invalid(news) && mor(news, ans)) {
				ans = news;
			}
		}
	}
	return memo[pos][menor][last] = ans;
}

int main() {
	cin>>T;
	int caso = 0;
	while (T--) {
		cin>>N;
		int n = N.size();
		string ans2 = "";
		for(int i=0; i<n-1; ++i) {
			ans2 += "9";
		}
		clear();
		string ans = f(0, 0, 1);
		printf("Case #%d: ", ++caso);
		if (ans != "$")cout<<ans<<endl;
		else cout<<ans2<<endl;
	}
}
