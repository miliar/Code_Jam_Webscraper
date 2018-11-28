#include<bits/stdc++.h>
using namespace std ;

int main() {

	const double pi  =3.141592653589793238463;
	
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t , n , m ;
	
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		
		cin >> n >> m ;
	
		vector< pair< double , double > > measurement(n) ;	
		
		for( int i = 0 ; i < n ; i++ ) cin >> measurement[i].first >> measurement[i].second ;
	
		
		vector< pair< double , pair< double, int > > > result ;
		for( int i = 0 ; i < n ; i++ ){
			result.push_back( make_pair( pi*measurement[i].first*2*measurement[i].second  ,  make_pair( measurement[i].first , i )  )  );
		}
	
		
		sort( result.begin() , result.end() ) ;
	//	cout << " surface area : " ; for( int i = 0 ; i < n ; i++ ) cout << result[i].first << " , " << result[i].second << endl ;
		double ans = 0 ;
		
		for( int i = 0 ; i < n ; i++ ) {
			double curR = measurement[i].first , curSA = 2*pi*curR*measurement[i].second ;
			int j = result.size()-1 ;
			int temp = m-1 ;
			double curAns = pi*curR*curR + curSA ;
			//cout << " curAns : " << curAns << " , curSA : " << curSA << " , rad : " << result[j].second << endl ;
			while( temp && (j >= 0 ) ) {
				if( (result[j].second.first < curR) || ( ( result[j].second.first == curR ) && (result[j].second.second != i ) ) )
					curAns += result[j].first , temp-- ;
				j-- ;	
			}
			//cout << " i : " << i << " , curAns : " << curAns << " , curR : " << curR << endl ;
			ans = max( ans , curAns ) ;
		}
		
		cout << "Case #" << k << ": " ;
		
		printf("%.9lf\n",ans) ;

	}
	return 0 ;

}
