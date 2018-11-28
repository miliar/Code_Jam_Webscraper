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

    cout << "Case #" << tt+1 << ": ";


    long long int r, c;
    cin >> r >> c;

    vector< string > v, ans;

    long long int cnt = 0;

    for ( long long int i = 0; i < r; i++ ) {
      string in;
      cin >> in;
      for ( long long int j = 0; j < in.size(); j++ ) {
	if ( in[j] == '-' || in[j] == '|' ) in[j] = '@';
      }
      v.push_back( in );
      ans.push_back( in );
    }

    bool flag = true;

    for ( long long int y = 0; y < r; y++ ) {
      for ( long long int x = 0; x < c; x++ ) {
	if ( v[y][x] == '@' ) {
	  bool f[2] = {};
	  for ( long long int xx = x - 1; xx >= 0; xx-- ) {
	    if ( v[y][xx] == '@' ) {
	      f[0] = true;
	      break;
	    }
	    if ( v[y][xx] == '#' ) break;
	  }
	  for ( long long int xx = x + 1; xx < c; xx++ ) {
	    if ( v[y][xx] == '@' ) {
	      f[0] = true;
	      break;
	    }
	    if ( v[y][xx] == '#' ) break;
	  }
	  for ( long long int yy = y - 1; yy >= 0; yy-- ) {
	    if ( v[yy][x] == '@' ) {
	      f[1] = true;
	      break;
	    }
	    if ( v[yy][x] == '#' ) break;
	  }
	  for ( long long int yy = y + 1; yy < r; yy++ ) {
	    if ( v[yy][x] == '@' ) {
	      f[1] = true;
	      break;
	    }
	    if ( v[yy][x] == '#' ) break;
	  }
	  if ( f[0] == true && f[1] == true ) {
	    flag = false;
	    break;
	  }
	  if ( f[0] == true ) {
	    ans[y][x] = '|';
	    for ( long long int yy = y - 1; yy >= 0; yy-- ) {
	      if ( v[yy][x] == '.' ) v[yy][x] = '*';
	      if ( v[yy][x] == '#' ) break;
	    }
	    for ( long long int yy = y + 1; yy < r; yy++ ) {
	      if ( v[yy][x] == '.' ) v[yy][x] = '*';
	      if ( v[yy][x] == '#' ) break;
	    }
	  }
	  if ( f[1] == true ) {
	    ans[y][x] = '-';
	    for ( long long int xx = x - 1; xx >= 0; xx-- ) {
	      if ( v[y][xx] == '.' ) v[y][xx] = '*';
	      if ( v[y][xx] == '#' ) break;
	    }
	    for ( long long int xx = x + 1; xx < c; xx++ ) {
	      if ( v[y][xx] == '.' ) v[y][xx] = '*';
	      if ( v[y][xx] == '#' ) break;
	    }
	  }

	}
      }
      if ( flag == false ) break;
    }
    if ( flag == false ) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    //ここまで初手レーザー並び替え

    while( true ) {
      //ここから、空白に１通りレーザー決め
      bool re = false;
      for ( long long int y = 0; y < r; y++ ) {
	for ( long long int x = 0; x < c; x++ ) {
	  if ( v[y][x] == '.' ) {
	    bool f[2] = {};
	    for ( long long int xx = x - 1; xx >= 0; xx-- ) {
	      if ( ans[y][xx] == '-' || ans[y][xx] == '@' ) {
		f[0] = true;
		break;
	      }
	      if ( v[y][xx] == '#' ) break;
	    }
	    for ( long long int xx = x + 1; xx < c; xx++ ) {
	      if ( ans[y][xx] == '-' || ans[y][xx] == '@' ) {
		f[0] = true;
		break;
	      }
	      if ( v[y][xx] == '#' ) break;
	    }
	    for ( long long int yy = y - 1; yy >= 0; yy-- ) {
	      if ( ans[yy][x] == '|' || ans[yy][x] == '@' ) {
		f[1] = true;
		break;
	      }
	      if ( v[yy][x] == '#' ) break;
	    }
	    for ( long long int yy = y + 1; yy < r; yy++ ) {
	      if ( ans[yy][x] == '|' || ans[yy][x] == '@' ) {
		f[1] = true;
		break;
	      }
	      if ( v[yy][x] == '#' ) break;
	    }
	    if ( f[0] == false && f[1] == false ) {
	      flag = false;
	      break;
	    }
	    if ( f[0] == false && f[1] == true ) {
	      re = true;
	      v[y][x] = '*';
	      for ( long long int yy = y - 1; yy >= 0; yy-- ) {
		if ( ans[yy][x] == '@' ) ans[yy][x] = '|';
		if ( v[yy][x] == '#' ) break;
	      }
	      for ( long long int yy = y + 1; yy < r; yy++ ) {
		if ( ans[yy][x] == '@' ) ans[yy][x] = '|';
		if ( v[yy][x] == '#' ) break;
	      }
	    }
	    if ( f[1] == false && f[0] == true ) {
	      re = true;
	      v[y][x] = '*';
	      for ( long long int xx = x - 1; xx >= 0; xx-- ) {
		if ( ans[y][xx] == '@' ) ans[y][xx] = '-';
		if ( v[y][xx] == '#' ) break;
	      }
	      for ( long long int xx = x + 1; xx < c; xx++ ) {
		if ( ans[y][xx] == '@' ) ans[y][xx] = '-';
		if ( v[y][xx] == '#' ) break;
	      }
	    }
	  }
	}
	if ( flag == false ) break;
      }
      if ( flag == false ) break;
      if ( re == true ) continue;

      for ( long long int y = 0; y < r; y++ ) {
	for ( long long int x = 0; x < c; x++ ) {
	  if ( ans[y][x] == '@' ) {
	    ans[y][x] = '-';
	    for ( long long int xx = x - 1; xx >= 0; xx-- ) {
	      if ( v[y][xx] == '.' ) v[y][xx] = '*';
	      if ( v[y][xx] == '#' ) break;
	    }
	    for ( long long int xx = x + 1; xx < c; xx++ ) {
	      if ( v[y][xx] == '.' ) v[y][xx] = '*';
	      if ( v[y][xx] == '#' ) break;
	    }
	    re = true;
	    break;
	  }
	}
	if ( re == true ) break;
      }
      if ( re == true ) continue;
      break;

    }

    if ( flag == false ) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << "POSSIBLE" << endl;
    for ( long long int i = 0; i < r; i++ ) {
      cout << ans[i] << endl;
    }

  }

  return 0;

}
