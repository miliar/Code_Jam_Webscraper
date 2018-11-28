#include <bits/stdc++.h>
using namespace std;
int t;
int main(){
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		bool tidy = 1;
		string s;
		cin >> s;
		int critical = 0;
		for(int i = 1;i < (int)s.length() && tidy; ++i){
			if(s[i] > s[i-1]) critical = i;
			else if(s[i] < s[i-1]) tidy = 0;
		}
		if(!tidy) {
			s[critical]--;
			for(int i = critical+1; i < (int) s.length(); ++i){
				s[i] = '9';
			}
			long long n = stoll(s);
			s = to_string(n);
		}
		printf("Case #%d: %s\n", tc, s.c_str());
	}
	return 0;
}