#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int inf = 1000000;
string s;
int cnt,n,T;
int vis[100];

char rev(char c) {
	if(c == '+') return '-';
	if(c == '-') return '+';
	return 0;
} 

string tran(int num, int len) {
	memset(vis, 0, sizeof(vis));
	int i = 1;
	while(num != 0) {
		if(num % 2 == 1) {
			vis[i] = 1;
			cnt ++;
		}
		num /= 2;
		i++;
	}
	string new_s = s;
	for(int i = 1; i <= len; i++) {
		if(vis[i]) {
			for(int j = i-1; j <= i-1+n-1; j++) {
				new_s[j] = rev(new_s[j]);
			}
		}
	}
	return new_s;
}

bool judge(string str) {
	char c = '+';
	for(int i = 0; i < str.length(); i++) 
		if(c != str[i]) return false;
	return true;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	// freopen("input.txt","r",stdin);
	freopen("Aoutput_small.txt","w",stdout);
	int ncase = 0;
	cin >> T;
	while(T--) {
		ncase++;
		cin >> s >> n;
		int len = s.length();
		int total = (1<< (len - n + 1));
		int ans = inf;
		for(int i = 0; i < total; i++) {
			cnt = 0;
			string new_s = tran(i,len);
			// cout << "i = " << i << " cnt = "<< cnt << " new_s = " << new_s << endl;
			if(judge(new_s)) {
				ans = min(ans,cnt);
			}
		}
		if(ans == inf) 
			printf("Case #%d: IMPOSSIBLE\n",ncase);
		else 
			printf("Case #%d: %d\n",ncase,ans);
	}
	return 0;
}