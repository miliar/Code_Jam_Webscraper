#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;

ll t;
ll n;
ll p[20];

ll nuyn(ll pind, ll dig){
	ll answ = 0;
	for(ll i=0;i<pind;i++) answ += p[i] * dig;
	return answ;
}

int main(){
	cin>>t;
	p[0] = 1;
	for(ll i=1;i<=18;i++) p[i] = p[i-1] * 10;
	ll f = 1;
	while(t){
		printf("Case #%lld: ", f);
		f++;
		cin>>n;
		if(n < 10){
			cout<<n<<endl;
			t--;
			continue;
		}
		if(n == p[18]){
			cout<<n-1<<endl;
			t--;
			continue;
		}
		ll answ = 0;
		ll mn = 0;
		for(ll i = 17; i>= 0; i--){
			ll dig = max((n/p[i])%10, mn);
			mn = dig;
			//cout<<dig<<": ";
			ll numdig = nuyn(i+1,dig);
			//cout<<numdig<<endl;
			if(numdig > n%p[i+1]){
				answ+=(dig-1)*p[i];
				answ+=nuyn(i,9);
				break;
			}
			else answ+=(dig)*p[i];

		}
		cout<<answ<<endl;
		t--;
	}

	return 0;
}