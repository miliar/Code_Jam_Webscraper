#include <bits/stdc++.h>
using namespace std;

char a[33][33];

int Main() {
  int n, m;
  cin >> n >> m;
  
  for (int i=0; i<n; i++) cin >> a[i];
  
  for (int i=0; i<n; i++) {
    int lst = 0;
    for (int j=0; j<m; j++) {
      if (a[i][j] == '?') continue;
      
      for (int k=lst; k<j; k++) a[i][k] = a[i][j];
      lst = j + 1;
    }
    
    if (lst > 0) for (int j=lst; j<m; j++) a[i][j] = a[i][lst-1];
  }
  
  int lst = 0;
  for (int i=0; i<n; i++) {
    if (a[i][0] == '?') continue;
    for (int k=lst; k<i; k++) {
      for (int j=0; j<m; j++) a[k][j] = a[i][j];
    }
    lst = i+1;
  }
  
  for (int i=lst; i<n; i++) for (int j=0; j<m; j++) {
    a[i][j] = a[lst-1][j];
  }
  
  for (int i=0; i<n; i++) cout << a[i] << endl;
  return 0;
}

int main() {
  int t;
  cin >> t;
  for (int tc=0; tc<t; tc++) {
    printf("Case #%d:\n", tc+1);
    Main();
  }
  return 0;
}