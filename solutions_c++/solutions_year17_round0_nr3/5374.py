#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std ;

typedef long long ll ;
typedef pair < ll , ll > PAIR ;

priority_queue < PAIR > Q ;

ll n , k ;
int T ;

void Clear() {
	while ( !Q.empty() ) Q.pop() ;
}

int main() {
	freopen( "C.in" , "r" , stdin ) ;
	freopen( "C.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int  Case = 1 ; Case <= T ; Case ++ ) {
		printf( "Case #%d: " , Case ) ;
		cin >> n >> k ;
		Clear() ;
		Q.push( make_pair( n , 1 ) ) ;
		while ( k ) {
			PAIR top = Q.top() ;
			Q.pop() ;
			while ( !Q.empty() && Q.top().first == top.first ) {
				top.second += Q.top().second ;
				Q.pop() ;
			}
			ll now1 = (top.first - 1) / 2 ;
			ll now2 = (top.first - 1 - now1) ;
			k -= top.second ;
			if ( k <= 0 ) {
				cout << now2 << " " << now1 << endl ;
				break ;
			}
			Q.push( make_pair( now1 , top.second ) ) ;
			Q.push( make_pair( now2 , top.second ) ) ;
		}
	}

}
