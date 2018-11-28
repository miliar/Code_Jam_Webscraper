#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
string s[1000];


int main() {
  //  freopen("output.txt", "w", stdout);
  int t=0, T, n, m;
  int l, r;
  scanf("%d", &T);
  while(T--) {
    cin >> n >> m;
    printf("Case #%d:\n", ++t);
    for(int i=0;i<n;i++) cin >> s[i];
    int c = -1, k;
    for(int i=0;i<n;i++) {
      k = -1;
      for(int j=0;j<m;j++) 
	if(s[i][j] != '?') k=j,j=m;
      if(k>-1) c = i, i = n;
    }
    for(int i=c;i<n;i++) {
      int pre = 0;
      for(int j=0;j<m;j++) {
	if(s[i][j] != '?') {
	  for(int k=pre;k<j;k++) s[i][k] = s[i][j];
	  pre = j+1;
	}
      }
      if(pre==0) {
	for(int j=0;j<m;j++) {
	  if(s[i][j] == '?') s[i][j] = s[i-1][j];
	}
      }
      else for(int k=pre;k<m;k++) s[i][k] = s[i][pre-1];
    }
    for(int i=0;i<c;i++) {
      for(int j=0;j<m;j++) s[i][j] = s[c][j];
    }
    for(int i=0;i<n;i++) cout << s[i] << endl;
  }
}
