/*input
3
---+-++- 3
+++++ 4
-+-+- 4

*/
#include "bits/stdc++.h" 
using namespace std;
#define ll long long

int main(int argc, char const *argv[]){
	ll T,k;
	string s;
	ios::sync_with_stdio(0)	;
	cin>>T;
	for(ll cases=1;cases<=T;cases++){
		cin>>s>>k;
		ll flips = 0;
		cout<<"Case #"<<cases<<": ";
		for(ll i=0;i<=s.length()-k;i++){
			if(s[i]=='-'){
				flips++; 
				//cout<<s<<" -> ";
				for(ll j=0;j<k;j++){
					s[i+j] = (s[i+j]=='-')?'+':'-';
				}
				//cout<<s<<'\n';
			}
		}
		bool done = true;
		for(ll i=0;i<s.length();i++){
			if(s[i]=='-'){
				done=false;
			}
		}
		if(done){
			cout<<flips<<'\n';
		}else{
			cout<<"IMPOSSIBLE\n";
		}

	}
}
