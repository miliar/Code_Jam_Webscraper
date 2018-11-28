#include <bits/stdc++.h>
using namespace std ; 

#define int long long
const int MAXN = 1e6 + 100 ; 




ifstream fin ("in.txt") ; 
ofstream fout ("out.txt") ; 

vector<int> res ; 

void calc(int a , int b , int c){
	if(c == 0){
		res . push_back(a) ;
		return ; 
	}
	calc(a * 10 + b , b , c - 1) ; 
	if(b < 9)calc(a , b + 1  , c) ; 
}
int32_t main(){

	ios_base::sync_with_stdio(0) ; 
	cout . tie(0) ; cout . tie(0) ;

	int t ; fin >> t ; 
	calc(0 , 0 , 18) ; 
	for(int _ = 0 ; _ < t ; _ ++){
		int n ; fin >> n ; 
		int l = 0 , r = res . size() ; 
		while(r - l > 1) {
			int mid = (r + l) / 2 ; 
			if(res[mid] > n)r = mid ; else l = mid ; 
		}
		fout << "Case #" << _ + 1 << ':' << ' ' << res[l] << '\n' ; 

	}

}	