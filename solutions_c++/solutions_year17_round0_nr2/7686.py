/**			
***** Judge
******* Yourself 
********* Only   
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <math.h>
#include<cstdio>
#include<deque>
#include<sstream>
#include<cmath>
using namespace std;
#define mp make_pair
#define eps 1e-6
vector<vector<long long> > v ; 
int n ;
void calc( int ind , int nub , long long res ) {
	if ( nub == n ) {
		v[n].push_back(res) ; 
		return ; 
	}
	for ( int i = ind ;i<= 9 ; i++){
		long long g = res*10 + i ; 
		calc(i,nub+1 , g );
	}
}
int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "w", stdout);
	v.resize(20);
	for ( int i = 1 ; i <= 18 ; i++ ) {
		n = i ; 
		calc(1,0,0);
	}

	int t , tt =1 ; 
	cin >> t; 
	while(t--){
		long long x , tmp; 
		cin >> x; 
		tmp = x ; 
		int c = 0 ; 
		while(tmp){
			c++;
			tmp/=10;
		}
		int res = upper_bound(v[c].begin(),v[c].end(), x ) - v[c].begin() ; 
		res--;
		long long ans ; 
		if (res == -1 ) 
			ans = v[c-1][v[c-1].size()-1];
		else
			ans = v[c][res];
			
		printf("Case #%d: %lld\n", tt++ , ans ) ; 
		//cout << c << " -  " << v[c].size() << " " << res << " " << v[c][res] << endl;
	}
}