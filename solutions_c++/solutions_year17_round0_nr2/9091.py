#include <bits/stdc++.h>
#include <cstring>
#define ll long long
using namespace std;

string s;
void getTidyNum(); 	

int main(){
	int t, j;

	cin>>t;
	for(j = 1; j <= t; j++){
		ll ans;

		cin>>s;
		getTidyNum();
		ans = stoll(s);
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
}

void getTidyNum(){
	ll l;

	if(s.length() == 1) return;
	for(l = 0; (l < (s.length() - 1))  && (s[l] <= s[l + 1]); l++);
	if(l == s.length() - 1) return;
	while(l && s[l] == s[l - 1])	l--;
	s[l]--; l++;
	for(; l < s.length(); l++)	s[l] = '9';
}