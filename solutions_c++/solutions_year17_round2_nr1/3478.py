#include<iostream>
#include<iomanip>
using namespace std;


double A[4000] , B[4000];

int main()
{
  int t;
  cin >> t;
  for( int tc = 1 ; tc <= t ; ++tc )
  {
    cout << "Case #"<<tc<<": ";
    int K, D;
    cin >> K >> D;
    for( int i = 0 ; i < D ; ++i )
      cin >> A[i] >> B[i];
    double lo = 1 , hi = 1e30;
    for( int i = 0 ; i < 300 ; ++i )
    {
      double mid  = ( lo + hi )/ 2;
      double timer = K / mid;

      bool ok = true;
      for( int j = 0 ; j < D;  ++j )
	if( B[j] < mid )
	{
	  double tt = A[j] / ( mid - B[j]  );
	  if( tt < timer )
	    ok = false;
	}
      if( ok ) lo = mid;
      else hi = mid;
    }
    cout << fixed << setprecision(9) << lo << endl;
  }
  return 0;
}
