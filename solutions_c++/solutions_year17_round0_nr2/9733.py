#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool good(ll n){
	if(n%10==n) return true;
	int mod1=n%10,coc=n/10,mod2=coc%10;
	while(coc!=0){
		if(mod1<mod2){
			return false;
		}else{
			mod1=mod2;
			coc/=10;
			mod2=coc%10;
		}
	}
	return true;
}

int main(){
	int T;
	ll N;
	cin >> T;
	int t=0;
	while(t<T){
		cin >> N;
		while(!good(N)) N--;
		cout << "Case #" << t+1 << ": " << N << endl;
		t++;
	}
	return 0;
}
