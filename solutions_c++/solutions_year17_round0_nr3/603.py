#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
void main2(){
	long long n;
	long long k;
	cin >> n >> k;
	long long tot=0;
	long long cur = 1;
	map<long long, long long> m;
	
	m[n]=1;
	while(tot+cur<k){
		map<long long, long long> m2;
		for(auto num : m){
			ll n1 = num.first/2;
			ll n2 = num.second;
			if(n1*2==num.first){
				m2[n1]+=n2;
				m2[n1-1]+=n2;
			} else {
				m2[n1]+=n2;
				m2[n1]+=n2;
			}
		}
		tot=tot+cur;
		cur*=2;
		m=m2;
	}

	ll lef = k-tot;
	ll ans = 0;
	if(lef <= m.rbegin()->second){
		ans = m.rbegin()->first;
	} else {
		ans = m.begin()->first;
	}
	ll sum = 0;
	for(auto x : m){
		sum+=x.second;
	}
	ll n1 = ans/2;
	if(n1*2==ans){
		cout << n1 << " " << n1-1;
	} else {
		cout << n1 << " " << n1;
	}
}
void main3(){
	long long n = 2198373278923460;
	set<ll> s;
	set<ll> s2;
	s.insert(n);
	for(int i=0;i<140;i++){
		s2.clear();
		for(auto num: s){
			ll n1  = num/2;
			if(n1*2==num){
				s2.insert(n1);
				s2.insert(n1-1);
			} else {
				s2.insert(n1);
				s2.insert(n1);
			}
		}
		s=s2;
	}
	cout << endl;
	cout << n << endl;
	for(auto num: s){
		cout << num << " ";
	}
	cout << endl;
}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}