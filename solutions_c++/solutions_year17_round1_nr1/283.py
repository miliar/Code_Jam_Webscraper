#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ":" << endl;


    long long int r, c;
    cin >> r >> c;

    vector< string > v;

    for ( long long int i = 0; i < r; i++ ) {

      string in;
      cin >> in;
      v.push_back( in );

    }

    long long int lx[26] = {};
    for ( long long int y = 0; y < r; y++ ) {
      for ( long long int x = 0; x < c; x++ ) {
	if ( v[y][x] == '?' ) continue;

	long long int xx = x;
	for ( long long int dx = x - 1; dx >= 0; dx-- ) {
	  if ( v[y][dx] != '?' ) break;
	  v[y][dx] = v[y][x];
	  xx = dx;
	}
	long long int xxx = x;
	for ( long long int dx = x + 1; dx <  c; dx++ ) {
	  if ( v[y][dx] != '?' ) break;
	  v[y][dx] = v[y][x];
	  xxx = dx;
	}
	lx[ v[y][x] - 'A' ] = xxx - xx + 1;

      }
    }
    for ( long long int y = 0; y < r; y++ ) {
      for ( long long int x = 0; x < c; x++ ) {
	if ( v[y][x] == '?' ) continue;

	for ( long long int dy = y - 1; dy >= 0; dy-- ) {
	  bool flag = true;
	  for ( long long int i = 0; i < lx[ v[y][x] - 'A' ]; i++ ) {
	    long long int dx = x + i;
	    if ( v[dy][dx] != '?' ) {
	      flag = false;
	      break;
	    }
	  }
	  if ( flag == false ) break;
	  for ( long long int i = 0; i < lx[ v[y][x] - 'A' ]; i++ ) {
	    long long int dx = x + i;
	    v[dy][dx] = v[y][x];
	  }
	}
	for ( long long int dy = y + 1; dy < r; dy++ ) {
	  bool flag = true;
	  for ( long long int i = 0; i < lx[ v[y][x] - 'A' ]; i++ ) {
	    long long int dx = x + i;
	    if ( v[dy][dx] != '?' ) {
	      flag = false;
	      break;
	    }
	  }
	  if ( flag == false ) break;
	  for ( long long int i = 0; i < lx[ v[y][x] - 'A' ]; i++ ) {
	    long long int dx = x + i;
	    v[dy][dx] = v[y][x];
	  }
	}

      }
    }


    for ( long long int y = 0; y < r; y++ ) {
      cout << v[y] << endl;
    }

  }

  return 0;

}
