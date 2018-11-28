#include<bits/stdc++.h>
using namespace std ;

int main() {

	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t ;
	long long n, m ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		cin >> n >> m ;
		
		priority_queue< int > pq ;
		
		pq.push(n) ;
		int val ;
		for( int i = 0 ; i < m ; i++ ){
			val = pq.top() ;
			pq.pop() ;
			if( val%2 ){
				pq.push(val/2) ;
				pq.push(val/2) ;
			} else {
				pq.push((val/2)-1) ;
				pq.push(val/2) ;
			}
		}
		
		cout << "Case #" << k << ": " ;
		if( val%2 )
			cout << val/2 << " " << val/2 << endl ;
		else cout << val/2  << " " << val/2 - 1 << endl ;

	}
	return 0 ;

}
