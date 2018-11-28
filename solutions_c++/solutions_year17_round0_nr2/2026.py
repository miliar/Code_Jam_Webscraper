#include <iostream>
using namespace std;
typedef long long ll;
int main()
{
  ios::sync_with_stdio(false);
  int T;
  ll N;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    cin >> N;
    int n[20];
    int s = 0;
    while( N > 0 ){
      n[s] = N % 10;
      s++;
      N /= 10;
    }
    int prev = 0;
    int f = 0;
    int pos = -1;
    for( int i=s-1; i>=0; i-- ){
      if( !f ){
        if( prev > n[i] ){
          n[pos]--;
          for( int j=i+1; j<pos; j++ ){
            n[j] = 9;
          }
          f = 1;
        } else if( prev != n[i] ) {
          prev = n[i];
          pos = i;
        }
      }
      if( f ) n[i] = 9;
    }
    for( int i=s-1; i>=0; i-- ){
      N = N*10 + n[i];
    }
    cout << "Case #" << testcase << ": " << N << endl;
  }
}
