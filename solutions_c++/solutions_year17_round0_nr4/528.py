#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<list>
#include<utility>
#include<algorithm>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

int n,m;
char orig[100][100];
char best[100][100];
void main2() {
  cin>>n>>m;
  int a,b;
  int oa = 0, ob = 0;
  char c;
  bool found = false;
  memset(orig, 0, sizeof(orig));
  memset(best, 0, sizeof(best));
  for (int i=0; i<m; ++i) {
    cin>>c>>a>>b;
    a--; b--;
    orig[a][b] = c;
    best[a][b] = c;
    if (c != '+') {
      best[a][b] = 'o';
      oa = a;
      ob = b;
      found = b != 0;
    }
  }
  best[0][0] = found ? '+' : 'o';
  for (int i=1 ;i<n; ++i) {
    best[0][i] = best[0][i] ? best[0][i] : '+';
  }
  for (int i=1; i<n; ++i) {
    for (int j =0; j<n; ++j) {
      if (i-j == oa-ob) {
        best[i][j] = 'x';
      }
      if (i+j == n-1 && j < ob) {
        best[i][j] = 'x';
      }
      if (i == n-1 && j != 0 && j!=n-1) {
        best[i][j] = '+';
      }
    }
  }

  ostringstream ss;
//  cout<<"-------------------"<<endl;
  int nm = 0;

  for (int i=0 ;i<n; ++i) {
    for (int j =0; j<n; ++j) {
      if ( best[i][j] != orig[i][j] ) {
        nm++;
        ss << best[i][j] <<" " << i+1 <<" "<<j+1<<endl;
      }
 //     cout << (best[i][j] ? best[i][j] : '.');
    }
  //  cout<<endl;
  }

  int bs = 3*n - 2;
  if (n == 1) bs++;
  cout << bs<< " " << nm<<endl;
  cout << ss.str();
}

int main(int argc, char *argv[]) {
	cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
	for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
		cout<<"Case #"<<ca<<": ";
    main2();
	}
}
