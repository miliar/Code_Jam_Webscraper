#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int n, m;
    cin >> n >> m;

    vector<bool> row(n, true);
    vector<bool> col(n, true);
    vector<bool> d1(n*2, true);
    vector<bool> d2(n*2, true);
    vector<vector<bool>> g1(n,vector<bool>(n, false));
    vector<vector<bool>> g2(n,vector<bool>(n, false));
    set<pair<int,int>> place;


    int style = 0;
    for (int i=0;i<m;i++) {
      char t;
      int r, c;
      cin >> t >> r >> c;
      r--;
      c--;
      if (t == 'x' || t == 'o') {
        row[r] = false;
        col[c] = false;
        style++;
        g1[r][c] = true;
      }
      if (t == '+' || t == 'o') {
        //d1[r+c+1] = false;
        //d2[r-c+n] = false;
        d1[r+c+1] = false;
        d2[r-c+n] = false;
        style++;
        g2[r][c] = true;
      }
    }

    for (int i = 0, j = 0;i<n && j<n;i++) {
      if (row[i]) {
        while (j < n && !col[j]) j++;
        if (j < n && col[j]) {
          g1[i][j] = true;
          place.insert(make_pair(i,j));
          j++;
          style++;
        }
      }
    }

    for (int a=0;a<2;a++) {
      for (int i=1+a,j=n+a;i<=n;i+=2) {
        for (int z=0;z<2;z++) {
          int ii=z==0?i:2*n-i;
          if (d1[ii]) {
            while (j < n+i && !(d2[j] || d2[2*n-j])) j+=2;
            if (j < n+i && (d2[j] || d2[2*n-j])) {
              int jj=d2[j]?j:2*n-j;

              //ii=x+y+1
              //jj=x-y+n
              //
              //ii+jj = 2x+n+1
              //ii-jj = 2y+1-n
              int x = (ii+jj-n-1)/2;
              int y = (ii-jj+n-1)/2;
              g2[x][y] = true;
              place.insert(make_pair(x,y));
              d2[jj] = false;
              d1[ii] = false;
              style++;
            }
          }
        }
      }
    }

    printf("Case #%d: %d %d\n", t, style, place.size());
    //for (int i=0;i<n;i++) {
    //  for (int j=0;j<n;j++) cout << g1[i][j] << " "; cout << endl;
    //}
    //cout << endl;
    //for (int i=0;i<n;i++) {
    //  for (int j=0;j<n;j++) cout << g2[i][j] << " "; cout << endl;
    //}
    for (auto loc : place) {
      int r = loc.first;
      int c = loc.second;
      char t = 'e';
      if (g1[r][c]) {
        t = g2[r][c]?'o':'x';
      }
      else if (g2[r][c]) t = '+';
      printf("%c %d %d\n", t, r+1, c+1);
    }
  }

}


