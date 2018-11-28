#include <bits/stdc++.h>

using namespace std;

long long T, N;
vector< int > digits;

int main() {
  cin >> T;
  for ( int num = 1 ; num <= T ; ++num ) {
    cin >> N;
    
    digits.clear();
    long long tmp = N;
    while ( tmp > 0 ) {
      digits.push_back( tmp % 10 );
      tmp /= 10;
    }
    reverse( digits.begin(), digits.end() );
    if ( digits.size() == 1 ) {
      cout << "Case #" << num << ": " << N << endl;
      continue;
    }

    vector< int > ans;
    for ( int i = 0 ; i < digits.size() - 1 ; ++i ) {
      if ( digits[ i ] <= digits[ i + 1 ] ) {
        ans.push_back( digits[ i ] );
        if ( i == digits.size() - 2 )
          ans.push_back( digits[ i + 1 ] ); 
        continue;
      }
      ans.push_back( digits[ i ] - 1 );
      while ( ans.size() != digits.size() )
        ans.push_back( 9 );
      break;
    }
    for ( int i = ans.size() - 1 ; i > 0 ; --i )  
      if ( ans[ i - 1 ] > ans[ i ] ) {
        --ans[ i - 1 ];
        ans[ i ] = 9;
      }
    
    cout << "Case #" << num << ": ";
    bool flag = false;
    for ( int i = 0 ; i < ans.size() ; ++i ) {
      if ( !flag && !ans[ i ] ) continue;
      cout << ans[ i ];
    }
    cout << endl; 
  }
}
