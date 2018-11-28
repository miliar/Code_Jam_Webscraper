#include <iostream>
#include <string>
#include <vector>
using namespace std;

string s[100];
bool f_x[2][101][101] = {};
bool f_a[2][101][101] = {};
long long int n, m;
long long int ans = 0;

void kansu_x( long long int y, long long int x ) {

  f_a[0][y][x] = true;
  for ( long long int xx = 0; xx < n; xx++ ) {
    f_x[0][y][xx] = true;
  }
  for ( long long int yy = 0; yy < n; yy++ ) {
    f_x[0][yy][x] = true;
  }
  return;
}

void kansu_p( long long int y, long long int x ) {

  f_a[1][y][x] = true;
  for ( long long int j = 0; j < n; j++ ) {
    long long int xx = x - j;
    long long int yy = y - j;
    if ( xx < 0 || yy < 0 ) break;
    f_x[1][yy][xx] = true;
  }
  for ( long long int j = 0; j < n; j++ ) {
    long long int xx = x + j;
    long long int yy = y - j;
    if ( xx >= n || yy < 0 ) break;
    f_x[1][yy][xx] = true;
  }
  for ( long long int j = 0; j < n; j++ ) {
    long long int xx = x - j;
    long long int yy = y + j;
    if ( xx < 0 || yy >= n ) break;
    f_x[1][yy][xx] = true;
  }
  for ( long long int j = 0; j < n; j++ ) {
    long long int xx = x + j;
    long long int yy = y + j;
    if ( xx >= n || yy >= n ) break;
    f_x[1][yy][xx] = true;
  }

  return;

}

int main() {

  long long int in_t;
  cin >> in_t;
  for ( long long int for_t = 0; for_t < in_t; for_t++ ) {
    cout << "Case #" << for_t + 1 << ": ";

    cin >> n >> m;

    string g = "";
    for ( long long int i = 0; i < n; i++ ) {
      g += ".";
    }
    for ( long long int i = 0; i < n; i++ ) {
      s[i] = g;
      for ( long long int j = 0; j < n; j++ ) {
	f_x[0][i][j] = false;
	f_x[1][i][j] = false;
	f_a[0][i][j] = false;
	f_a[1][i][j] = false;
      }
    }

    for ( long long int i = 0; i < m; i++ ) {

      char c;
      long long int x, y;
      cin >> c >> y >> x;
      y--;
      x--;
      s[y][x] = c;
      if ( c == 'x' || c == 'o' ) {
	kansu_x( y, x );
      }
      if ( c == '+' || c == 'o' ) {
	kansu_p( y, x );
      }

    }

    for ( long long int y = 0; y < n; y++ ) {
      for ( long long int x = 0; x < n; x++ ) {

	if ( f_x[0][y][x] == true ) continue;
	kansu_x( y, x );

      }
    }

    for ( long long int y = 0; y < n; y++ ) {
      if ( f_x[1][y][0] == false ) kansu_p( y, 0 );
      if ( f_x[1][y][n-1] == false ) kansu_p( y, n-1 );
    }
    for ( long long int x = 0; x < n; x++ ) {
      if ( f_x[1][0][x] == false ) kansu_p( 0, x );
      if ( f_x[1][n-1][x] == false ) kansu_p( n-1, x );
    }


    ans = 0;
    vector< char > ans_c;
    vector< long long int > ans_x, ans_y;
    char dc[4] = { '.', 'x', '+', 'o' };
    for ( long long int y = 0; y < n; y++ ) {
      for ( long long int x = 0; x < n; x++ ) {
	long long int cnt = 0;
	if ( f_a[0][y][x] == true ) {
	  cnt += 1;
	  ans++;
	}
	if ( f_a[1][y][x] == true ) {
	  cnt += 2;
	  ans++;
	}
	if ( s[y][x] == '.' && cnt != 0 ) {
	  ans_c.push_back( dc[cnt] );
	  ans_y.push_back( y + 1 );
	  ans_x.push_back( x + 1 );
	}else if ( s[y][x] != 'o' && cnt == 3 ) {
	  ans_c.push_back( 'o' );
	  ans_y.push_back( y + 1 );
	  ans_x.push_back( x + 1 );
	}
      }
    }

    cout << ans << " " << ans_c.size() << endl;
    for ( long long int i = 0; i < ans_c.size(); i++ ) {
      cout << ans_c[i] << " " << ans_y[i] << " " << ans_x[i] << endl;
    }


  }

  return 0;

}
