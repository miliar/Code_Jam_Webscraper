#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<pair<int,int>,int> P;
P D[405];
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    int Nc, Nj;
    cin >> Nc >> Nj;

    int R[2] = {720,720};
    for( int i=0; i<Nc; i++ ){
      P *p = &D[i];
      cin >> p->first.first >> p->first.second;
      p->second = 0;
      R[0] -= p->first.second - p->first.first;
    }
    for( int i=0; i<Nj; i++ ){
      P *p = &D[Nc + i];
      cin >> p->first.first >> p->first.second;
      p->second = 1;
      R[1] -= p->first.second - p->first.first;
    }
    int N = Nc+Nj;
    sort( D, D + N );
    
    
    while( 1 ){
      int M[2] = {10000,10000};
      int I[2] = {-1,-1};
      for( int i=0; i<N; i++ ){
        int nx = (i+1) % N;
        if( D[nx].second == D[i].second ){
          int d = ( D[nx].first.first - D[i].first.second + 1440 * 400 ) % 1440;
          if( M[D[i].second] > d ){
            M[D[i].second] = d;
            I[D[i].second] = i;
          }
        }
      }
      if( M[0] <= R[0] ){
        R[0] -= M[0];
        int nx = (I[0]+1) % N;
        D[I[0]].first.second = D[nx].first.second;
        for( int j=nx; j<N-1; j++ ){
          D[j] = D[j+1];
        }
        N--;
        continue;
      }
      if( M[1] <= R[1] ){
        R[1] -= M[1];
        int nx = (I[1]+1) % N;
        D[I[1]].first.second = D[nx].first.second;
        for( int j=nx; j<N-1; j++ ){
          D[j] = D[j+1];
        }
        N--;
        continue;
      }
      break;
    }
    int ret = 0;
    for( int i=0; i<N; i++ ){
      int nx = (i+1)%N;
      if( D[i].second == D[nx].second ) ret++;
      ret++;
    }

    cout << "Case #" << testcase << ": " << ret << endl;
  }
}
