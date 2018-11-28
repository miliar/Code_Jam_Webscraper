#include <bits/stdc++.h>
using namespace std;

void resolve(map<long long, long long> mp, long long k){
    map<long long, long long>::iterator it = mp.end();
    it--;
    while(k > 0){
	k -= it->second;
	if(k <= 0){
	    long long ls,rs;
	    ls = rs = (it->first) / 2;
	    if((ls + rs) == it->first)
		ls--;
	    cout << max(ls,rs) << " " << min(ls,rs);
	    return;
	}
	it--;
    }
}

void brute(map<long long, long long> mp, long long k){
    long long sum = 0;
    for(auto i: mp)
	sum += i.second;

    if(sum >= k)
	resolve(mp,k);
    else{
	map<long long, long long> splits;
	for(auto i: mp){
	    k -= i.second;
	    if(i.first == 1) continue;
	    long long ls = i.first/2;
	    long long rs = i.first/2;
	    if((ls + rs) == i.first)
		ls--;
	    splits[ls] += i.second;
	    splits[rs] += i.second;
	}
	assert(k > 0);
	brute(splits, k);
    }
}

void solve(){
    long long n,k;
    cin >> n >> k;
    map<long long, long long> mp;
    mp[n] = 1;
    brute(mp,k);
}

int main(){
    int cases;
    cin >> cases;
    for(int i = 1; i <= cases; i++){
	cout << "Case #" << i << ": ";
	solve();
	cout << "\n";
    }
    return 0;
}
