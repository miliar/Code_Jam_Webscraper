/*input
5
132
1000
7
111111111111111110
450


*/
#include "bits/stdc++.h" 
using namespace std;
#define ll long long

int main(int argc, char const *argv[]){
	ll T,num;
	string n;
	ios::sync_with_stdio(0)	;
	cin>>T;
	for(ll cases=1;cases<=T;cases++){
		cin>>num;
		n = to_string(num);
		cout<<"Case #"<<cases<<": ";
		for(ll i=n.length()-2;i>=0;i--){
			if( n[i] > n[i+1] ){
				//cout<<n<<" -> ";
				n[i]-=1;
				for(ll j=i+1;j<n.length();j++){
					n[j]='9';
				}
				//cout<<n<<'\n';
			}
		}
		cout<<stoll(n)<<'\n';
		
	}
}

