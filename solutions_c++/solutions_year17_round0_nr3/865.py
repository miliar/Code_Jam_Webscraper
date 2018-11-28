#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
long long T, n, k, y, z, guess;
unordered_map<long long, long long> mp;
long long cnt(long long rem){
	if (rem < guess) return 0;
	if (mp.count(rem)) return mp[rem];
	return mp[rem] = 1ll + cnt(rem/2) + cnt(rem-rem/2); 
}
int main(){
	ifstream inp;
	inp.open ("c.in");
	ofstream oup;
	oup.open("c.out");
	inp>>T;
	F(t, T){
		inp>>n>>k;
		long long low = 1, high = n+1;
		while (high > low){
			guess = (high + low + 1)/2;
			mp.clear();
			if (cnt(n+1)>=k) low = guess;
			else high = guess - 1;
		}
		cout<<t<<endl;
		oup<<"Case #"<<t<<": "<<low-low/2-1<<" "<<low/2 - 1<<endl;
	}
}
//Case #7: 7812 7811
