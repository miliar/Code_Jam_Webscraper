#include <iostream>  
#include <string>
#include <vector>

using namespace std;  

string solve( const string& cakes, int k ) {
    vector<bool> mark( cakes.size() );
    for ( size_t i = 0; i < cakes.size(); ++i )
        mark[i] = (cakes[i] == '+' ? 1 : 0);

    unsigned count = 0;
    for ( size_t i = 0; i < mark.size() - k + 1; ++i ) {
        if ( !mark[i] ) {
            ++count;
            for (int j = 0; j < k; ++j) {
                mark[i+j] = !mark[i+j];
            }
        }
    }

    for ( int i = (int)mark.size() - k; i < (int)mark.size(); ++i )
        if (!mark[i])
            return "IMPOSSIBLE";

    return to_string(count);
}

int main() {
  int t, k;
  string cakes;
  
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> cakes >> k; 
    cout << "Case #" << i << ": " << solve(cakes, k) << endl;
  }

  return 0;
}
