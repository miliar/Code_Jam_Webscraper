#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5+4;
typedef long long ll;

string func(string num){
	int i = 0;
	if(num.length() == 1) return num;
	while(true){
		if(i == num.length()-1) break;
		if(num[i] <= num[i+1]) i++;
		else num[i+1] = num[i];
	}
	return num;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("/home/harsh/Desktop/B-small-attempt0.in", "r", stdin);
	freopen("/home/harsh/Desktop/B-small-attempt0.out", "w", stdout);		
#endif
	int t, cnt = 0; cin >> t;
	while(t--){
		ll n; cin >> n;
		ll low = 0, high = n, ans = 0;
		while(low <= high){
			// printf("low = %lld high = %lld\n", low, high);
			ll mid = high - (high - low)/2;
			string s = func(to_string(mid));
			ll tmp = stoll(s);
			if(tmp > n) high = mid-1; 
			else {ans = max(ans, tmp); low = tmp+1;}
			// printf("mid = %lld tmp = %lld\n", mid, tmp);
			// printf("ans = %lld\n\n", ans);
		}
		printf("Case #%d: %lld\n", ++cnt, ans);
	}
	return 0;
}