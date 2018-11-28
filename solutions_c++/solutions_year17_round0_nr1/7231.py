#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void io(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout.precision(15);
}

int main(int argc,char* argv[]) { 
    io() ;
    #ifndef ONLINE_JUDGE
        freopen("A-large (3).in", "r", stdin) ;
        freopen("A.txt", "w", stdout);
    #endif
    int tc = 0 ;
    int t; 
    cin >> t ;
    string s ;
    int n, k ;
    while(t--){
    	tc++ ;
    	cout << "Case #" << tc << ": " ;
    	cin >> s >> k ;
    	n = s.length() ;
    	int ans = 0 ;
    	for(int i = 0 ; i <= (n - k) ; i++){
    		if(s[i] == '-'){
    			ans++ ;
    			for(int j = i ; j <= (i + k - 1) ; j++){
    				if(s[j] == '-') s[j] = '+' ;
    				else s[j] = '-' ;
    			}
    		}
    	}
    	bool ok = 1 ;
    	for(int i = 0 ; i < n ; i++){
    		if(s[i] == '-'){
    			ok = 0 ;
    			break ;
    		}
    	}
    	if(!ok){
    		cout << "IMPOSSIBLE\n" ;
    		continue ;
    	}
    	cout << ans << endl ;
    }
    return 0 ; 
}