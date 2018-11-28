#include<bits/stdc++.h>
using namespace std;

string s; int k, n;
bitset<1010> pancake;

int flip(int i){
	if(pancake[i]) return 0;
	for(int j = i; j<i+k; j++){
		pancake.flip(j);
	}
	return 1;
}

int main(){
	int tcn = 1;
	int t; cin>>t;
	while(t--){
		cin>>s>>k;
		n = s.size();
		pancake.reset();
		for(int i = 0; i<n; i++){
			if(s[i]=='+'){
				pancake[i]=1;
			}else pancake[i] = 0;
		}
		int ans = 0;
		for(int i = 0; i<=n-k; i++){
			ans += flip(i);
		}
		cout<<"Case #"<<tcn++<<": ";
		if(pancake.count()==n){
			cout<<ans<<endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;
	}
	
}