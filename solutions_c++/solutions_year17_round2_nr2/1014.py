#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

typedef pair<int,char> P;
int main( void )
{
  ios::sync_with_stdio(false);
  int T, N, R, O, Y, G, B, V;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N >> R >> O >> Y >> G >> B >> V;
    P D[4];
    D[0].first = R; D[0].second = 'R';
    D[1].first = Y; D[1].second = 'Y';
    D[2].first = B; D[2].second = 'B';
    D[3].first = -1; D[3].second = 'x';
    sort( D, D+3 );
    cout << "Case #" << testcase << ": ";
    if( D[2].first > N/2 ){
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << D[2].second;
    D[2].first--;
    int prev = 2;
    for( int i=1; i<N; i++ ){
      if( i % 2 == 0 && D[2].first > 0 ){
        cout << D[2].second;
        D[2].first--;
        prev = 2;
        continue;
      }
      int idx = 3;
      if( prev == 1 ) idx = 0;
      else if( prev == 0 ) idx = 1;
      else if( D[0].first > D[1].first ) idx = 0;
      else idx = 1; 

      cout << D[idx].second;
      D[idx].first--;
      prev = idx;
    }
    cout << endl;
  }
}
