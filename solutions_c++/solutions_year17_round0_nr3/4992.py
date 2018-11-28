#include <iostream>  
#include <string>
#include <vector>

using namespace std;  

void solve_rec( int n, int k, int& Max, int& Min ) {
    int right = n >> 1;
    int left = ( (right << 1) == n ? right - 1 : right );
    
    if ( k == 1 ) {
        Max = right;
        Min = left;
        return;
    }

    int rppl = k >> 1;
    int lppl = ( (rppl << 1) == k ? rppl - 1 : rppl );

    if ( rppl != lppl )
        solve_rec( right, rppl, Max, Min );
    else
        solve_rec( left, lppl, Max, Min );
}

void solve( int n, int k, int& Max, int& Min ) {
    solve_rec( n, k, Max, Min );
}

int main() {
  int t;
  int n, k;
  
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int Max, Min;
    cin >> n >> k; 
    solve(n , k, Max, Min);
    cout << "Case #" << i << ": " << Max << " " << Min << endl;
  }

  return 0;
}
