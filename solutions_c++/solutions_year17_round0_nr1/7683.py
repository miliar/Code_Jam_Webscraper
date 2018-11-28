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

int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "w", stdout);

	int t , tt =1 ;  
	cin >> t; 
	while(t--){
		string s ; 
		int k ; 
		cin >> s >> k ; 
		bool f = 1  , lst = -1  ;
		int res =  0 ; 
		for ( int i = 0 ; i < s.size()-k+1; i++ ) { 
			if ( s[i] == '-' ) {
				for ( int j =  0 ; j < k ; j++ ) 
					if(s[j+i] == '-') 
						s[j+i] = '+' ;
					else 
						s[j+i] = '-' ;
				res++;
			}
		}
		for ( int i = 0 ; i < s.size() ; i++ )
			if(s[i]=='-')
				f = 0;
		if(!f)
			printf("Case #%d: IMPOSSIBLE\n", tt++);
		else 
			printf("Case #%d: %d\n", tt++ ,res ) ; 
	}
}