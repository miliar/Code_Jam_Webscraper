#include<bits/stdc++.h>
using namespace std;
string s; int n;
string res;
string ans1, ans2;
void backtrack(int i){
	//cout<<res<<endl;
	if(ans1!="") return;
	if(i==n){
		ans1 = res;
		return;
	}
	if(i==0){
		for(char c = s[0]; c>='1'; c--){
			res.push_back(c);
			backtrack(1);
			res.pop_back();
		}
	}else{
		char u = s[i];
		bool ffa = false;
		for(int j = 0; j<i; j++){
			if(s[j]>res[j]) ffa = true;
		}
		if(ffa) u = '9';
		for(char c = u; c>=res[i-1]; c--){
			res.push_back(c);
			backtrack(i+1);
			res.pop_back();
		}
	}
}

long long conv(string s){
	stringstream ss;
	ss<<s;
	long long r;
	ss>>r;
	return r;
}
int main(){
	int tcn = 1;
	int t; cin>>t;
	while(t--){
		cin>>s;
		cout<<"Case #"<<tcn++<<": ";
		if(s.size()==1){
			cout<<s<<endl;
			continue;
		}
		n = s.size();
		ans1 = "";
		backtrack(0);
		string ans2 = "";
		for(int i = 0; i<n-1; i++){
			ans2.push_back('9');
		}
		if(ans1!="")
			cout<<max(conv(ans1),conv(ans2))<<endl;
		else cout<<ans2<<endl;
	}
}