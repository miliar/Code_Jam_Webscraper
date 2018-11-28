#include <bits/stdc++.h>
using namespace std ; 

#define int long long
const int MAXN = 1e6 + 100 ; 


ifstream fin ("in.txt") ; 
ofstream fout ("out.txt") ; 

map<int , int> mp , res[MAXN] ; 

void calc(int n){
	if(mp[n] == true)return ; 
	mp[n] = true ; 
	if(n / 2 > 0) calc(n / 2) ; 
	if(n - n / 2 - 1 > 0) calc(n - n / 2 - 1) ; 
}

int32_t main(){

	ios_base::sync_with_stdio(0) ; 
	cout . tie(0) ; cout . tie(0) ;

	int t ; fin >> t ; 
	for(int _ = 0 ; _ < t ; _ ++){
		int n ; fin >> n ;
		int k ; fin >> k ; 

		calc(n) ; 
		vector<int> base ; 
		for(auto u : mp)
			base . push_back(u . first) ; 
		mp . clear() ;
		int m = base . size() ; 
		for(int i = 0 ; i < m ; i ++){
			int x = base[i] ; 
			res[i][x] = 1 ; 
			if(x / 2 > 0){
				int t = x / 2 ; 
				int pos = lower_bound(base . begin() , base . end() , t) - base . begin() ; 
				for(auto u : res[pos])
					res[i][u . first] += u . second ; 
			}
			if(x - x / 2 - 1 > 0){
				int t = x - x / 2 - 1 ; 
				int pos = lower_bound(base . begin() , base . end() , t) - base . begin() ; 
				for(auto u : res[pos])
					res[i][u . first] += u . second ; 		
			}
		}
		vector<int> ans ; 
		for(auto u : res[base . size() - 1]){
			ans . push_back(u . first) ; 
			ans . push_back(u . second) ; 
		}
		int final = -1 ; 
		while(ans .  size() && k > 0){
			k -= ans . back() ; ans . pop_back() ; 
			final = ans . back() ; ans . pop_back() ; 
		}
		for(int i = 0 ; i < base . size() ; i ++)res[i] . clear() ; 
		base . clear() ; 
		fout << "Case #" << _ + 1 << ':' << ' ' << final / 2 << ' ' << final - final / 2 - 1 << '\n' ; 
	}
}