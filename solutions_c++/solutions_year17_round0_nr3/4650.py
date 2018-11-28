#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>

#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define F(i , a , b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define pb push_back
#define ll long long
#define E(a) cerr << #a << " = " << a << '\n'
#define X first
#define Y second
#define INF 10000000000000
#define int long long
const int MAX_N = 2000 + 10 , mod = 1000000007;

multiset <int> s;

void clr(){
	s.clear();
}
void solve(){
	int p,n,k;
	cin >> n >> k;
	s.insert(n);
	for(int i =0 ; i<k-1 ; i++){
		multiset <int> :: iterator it;
		it = s.end();
		it--;
		p = *it;
		p--;
		s.erase(it);
		s.insert(p/2);
		s.insert(p/2 + p%2);
	}
	multiset <int> :: iterator it;
	it = s.end();
	it--;
	p = *it;
	p--;
	cout << (p/2 + p%2) << " " << p/2 << endl; 
	
}


int32_t main(){
    
        freopen("input.txt" , "r" , stdin);
        freopen("output.txt" , "w" , stdout);
    //    cout << setprecision(10) << fixed;
    ios::sync_with_stdio(0); cin.tie() ; cout.tie();

    int T;
    cin >> T;
    for(int _ = 1 ; _ <= T ; _++){
    	clr();
    	cout << "Case #"<<_<<": ";
    	solve();
	}
        
    
    return 0;
}
