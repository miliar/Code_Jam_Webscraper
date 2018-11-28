#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

#define N 1000 + 10

char S[N] ;
int k ;
int T ;
int ans ;

int main() {
	freopen( "A.in" , "r" , stdin ) ;
	freopen( "A.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int  Case = 1 ; Case <= T ; Case ++ ) {
		ans = 0 ;
		printf( "Case #%d: " , Case ) ;
		scanf( "%s" , S + 1 ) ;
		scanf( "%d" , &k ) ;
		int len = strlen( S + 1 ) ;
		for (int i = 1 ; i <= len - k + 1 ; i ++ ) {
			if ( S[i] == '-' ) {
				ans ++ ;
				for (int j = 1 ; j <= k ; j ++ ) {
					if ( S[i+j-1] == '-' ) S[i+j-1] = '+' ;
					else S[i+j-1] = '-' ;
				}
			} else continue ;
		}
		bool flag = 1 ;
		for (int i = len - k + 1 ; i <= len && flag ; i ++ ) {
			if ( S[i] == '-' ) flag = 0 ;
		}
		if ( flag ) printf( "%d\n" , ans ) ;
		else printf( "IMPOSSIBLE\n" ) ;
	}
	return 0 ;
}
