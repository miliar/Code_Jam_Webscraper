#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	int t , u = 1 , temp , n , k ;

	priority_queue<int> pq ;
	
	cin >> t; 
	
	while ( t-- ){
		
		cin >> n >> k ;
		pq.push( n ) ;
		k--;
		
		while ( k-- ){
			
			temp = pq.top( ) ;
			pq.pop( ) ;
			pq.push(temp/2) ;
			pq.push((temp-1)/2) ;
		}
		
		temp = pq.top( ) ;
		//pq.clear( ) ;
		while ( !pq.empty( ) ){
			pq.pop( ) ;
		}
		cout << "Case #"<<u++<<": "<<temp/2 << " " << (temp-1)/2 << endl ;
	}

	
	return 0;
}
