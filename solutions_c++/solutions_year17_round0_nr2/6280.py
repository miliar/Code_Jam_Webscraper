#include <bits/stdc++.h>
using namespace std;

string to_str(long long n){
	string r("");
	while(n!=0){
		r = char((n%10)+48) + r;
		n/=10;
	}
	return r;
}

string solve(string &s){
	string ans("");
	int i;
	int l = s.size();
	
	char prev = s[0], tmp;
	int f=0;
	for(i = 1;i < l;++i){
		if(int(s[i-1]) > int(s[i])){
			f = 1;
			break;
		}
	}
	if(f){
		for(i=1;i<l;++i){
			if(int(prev) >= int(s[i])){
				tmp = int(prev)-1;
				if(tmp != 48)
					ans += char(tmp);
				ans += '9';
				prev = '9';
				break;
			}
			else{
				ans +=  prev;
			}
			prev = s[i];
			//cout << "ans: " << ans << endl; 
		}
		if(i==l)
			ans += char(int(prev));
		i++;
		for(;i<l;++i)
			ans += prev;
		return ans;
	}
	//cout << "hello\n";
	return s;
}

int main(){
	int t;
	cin >> t;
	int i;
	for(i=0;i<t;++i){
		long long n;
		cin >> n;
		string s(to_str(n));
		printf("Case #%d: ", i+1);
		cout << solve(s) << endl;
		/*if(r == -1)
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, r);*/
	}
}