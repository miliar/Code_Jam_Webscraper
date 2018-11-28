/*  Coder: Harsh Gupta
	Email: harshgupta.11dec@gmail.com
	Github: harshgupta11
	Linkedin: harshgupta11
	Problem Link: 
*/

#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;

void solve(){
	priority_queue<ll> stalls;
	ll N,K,element, a,b;
	cin >> N >> K;
	stalls.push(N);
	for(ll i = 1;i<=K;++i){
		element = stalls.top();
		stalls.pop();
		if(element&1)	a = b = element/2;
		else{
			a = element/2;
			b = (element-1)/2;
		}
		stalls.push(a);
		stalls.push(b);
		//cout << element << ' ' << a << ' ' << b << '\n';
	}
	cout << a << ' ' << b << '\n';
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int test = 1;test <=T;++test){
		cout << "Case #" << test << ": ";
		solve();
	}
    return 0;
}
