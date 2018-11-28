#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 100000 + 10;
const int M = 1000000007;
const double PI = atan(1) * 4;
const int oo = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
#define pb push_back 
#define all(c) (c).begin(),(c).end()
string s,s2;
int k;
void flip(string &s, int j){
	for(int i=j; i<j+k; ++i)
		if(s[i]=='+')s[i]='-';
		else s[i]='+';
}
bool check(string &s){
	for(int i=0; i<s.size(); ++i)
		if(s[i]=='-')return 0;
	return 1;
}
int main(){
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "r", stdin);
		freopen("output.txt","w",stdout);
	#endif
	int T;
	cin>>T;
	int t=1;
	while(T--){
		cin>>s>>k;
		s2=s;
		reverse(all(s2));
		int ans1=0,ans2=0;
		for(int i=0; i<=s.size()-k; ++i){
			if(s[i]=='-'){
				flip(s,i);
				++ans1;
			}
		}
		if(!check(s))ans1=-1;
		for(int i=0; i<=s.size()-k; ++i){
			if(s2[i]=='-'){
				flip(s2,i);
				++ans2;
			}
		}
		if(!check(s2))ans2=-1;
		cout<<"Case #"<<t++<<": ";
		if(ans1==-1 && ans2==-1)cout<<"IMPOSSIBLE\n";
		else if(ans1==-1)cout<<ans2<<endl;
		else if(ans2==-1)cout<<ans1<<endl;
		else cout<<min(ans1,ans2)<<endl;
	}
	
}


