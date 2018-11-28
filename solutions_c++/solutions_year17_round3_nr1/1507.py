#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
using namespace std;

vector < pair<double,double> > P;
int n, k;
long double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;



int main()
{
  int t;
  cin >> t;
  for( int tc = 1 ; tc <= t ; ++tc )
  {
    cout << "Case #"<<tc<<": ";
    cin >> n >> k;
    P.resize( n );
    for( int i = 0 ; i < n ; ++i )
      cin >> P[i].second >> P[i].first;
    sort( P.rbegin() , P.rend() );
    double ans = 0;
    for( int i = 0 ; i < n ; ++i  )
    {
       vector < pair<double,double> > V = P;
       V.erase( V.begin() + i );
       vector< double > vals;
       for( auto x : V )
	 vals.push_back( x.second * x.first );
       sort( vals.rbegin(), vals.rend() );
       double tmp = pi * P[i].second * P[i].second;
       tmp += 2.0*pi*( P[i].second * P[i].first);
       for( int j = 0 ; j < k - 1 ; ++j )
	 tmp += 2.0*pi*vals[j];
       ans = max( ans ,(double) tmp);
    }
    cout << fixed << setprecision(9) << ans << endl;
  }
  return 0;
}
