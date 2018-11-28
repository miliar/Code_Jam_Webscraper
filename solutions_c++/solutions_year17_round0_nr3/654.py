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
ll n,k;
ll ast[62];
int main(){
	cin>>t;
	ast[0] = 1;
	for(ll i=1;i<=60;i++) ast[i] = ast[i-1]*(2ll);
	ll f = 1;
	while(t){
		printf("Case #%lld: ", f);
		f++;
		cin>>n>>k;
		ll n1 = n;
		ll height = 0, floor = 0;
		ll current = 0;
		while(n1 >= 0){
			if(n1 - ast[current] < 0){
				floor = n1;
				break;
			}
			height++;
			n1-=ast[current];
			current++;
		}
		ll answer_level = 1, answer_indent = 0;
		ll k1 = k;
		current = 0;
		while(k1 > 0){
			if(k1 - ast[current] <= 0){
				answer_indent = k1;
				break;
			}
			answer_level++;
			k1-=ast[current];
			current++;
		}
		if(answer_level > height){
			cout<<0<<" "<<0<<endl;
			t--;
			continue;
		}
		ll defl = ast[height-answer_level+1]-(1ll);
		ll num_elem = ast[answer_level-1];

		ll answ = 0;
		answ = defl + floor/num_elem;
		if(floor%num_elem >= answer_indent) answ++;

		cout<<(answ - 1 - (answ-1)/2)<<" "<<(answ-1)/2<<endl;
		t--;
	}

	return 0;
}