#include<bits/stdc++.h>
using namespace std ;

int main() {

	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t , n ;
	double d , cur ;
	double ans, s ;
	
	string str ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		
		cin >> d >> n ;
		double maxTime = 0 ;
		
		for( int j = 0 ; j < n ; j++){
			cin >> cur >> s ;
			if( cur < d )
				maxTime = max( maxTime , (d-cur)/s ) ;
		}
		
		ans = d/maxTime ;
		
		cout << "Case #" << k << ": "  ;
		printf("%.6f\n",ans) ;

	}
	return 0 ;

}
