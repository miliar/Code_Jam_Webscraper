#include <bits/stdc++.h>

using namespace std;


struct tEvent{
	
	int min_dist;
	int max_dist;
	int coord;
	
	
	bool operator < (const tEvent& sec) const
    {
		if ( min_dist < sec.min_dist )
			return true;
		if ( min_dist > sec.min_dist ) 
			return false;
		
		// min_dist same
		
		if ( max_dist < sec.max_dist )
			return true;
		if ( max_dist > sec.max_dist )
			return false;
		
		// max_dist same
		
		return ( coord < sec.coord );
		
    }
	
};

tEvent make_event ( int mi , int ma , int co ){
	tEvent res;
	res.min_dist = mi;
	res.max_dist = ma;
	res.coord = co;
	
	return res;
}


tEvent get_for ( int L , int R ){
	
	int med = ( L + R ) / 2;
	
	tEvent res;
	
	res.coord = med;
	res.min_dist = min ( R - med - 1 , med - L - 1 );
	res.max_dist = max ( R - med - 1 , med - L - 1 );
	
	return res;
	
	
}

void solve(){
	
	int n;
	int k;
	
	scanf ( "%i %i" , &n , &k );
	
	priority_queue<tEvent> q;
	
	
	q.push( get_for(0,n+1) );
	
	for ( int i = 0 ; i < k ; i++ ){
		tEvent cur = q.top();
		q.pop();
		
		
		if ( cur.min_dist > 0 )
			q.push( get_for( cur.coord - cur.min_dist - 1 , cur.coord ) );
		if ( cur.max_dist > 0 )
			q.push( get_for( cur.coord , cur.coord + cur.max_dist + 1 ) );
		
		
		if ( i+1 == k )
			printf ( "%i %i \n" , cur.max_dist , cur.min_dist );
		
	}
}


int main(){
	
	
	int t;
	
	scanf ( "%i" , &t );
	for ( int i = 1 ; i <= t ; i++ ) {
		printf ( "Case #%i: " , i );
		solve();
		
		cerr << "Done " << i << endl;
	}
	
	
}
