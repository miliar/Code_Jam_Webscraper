#include <bits/stdc++.h>

using namespace std;

bool allFliped(string s) {
  for(int i=0; i<s.length(); i++)
    if(s[i] == '-') return false;
  return true;
}

int main() {
  int t, tc = 0; scanf("%d", &t);
  
  string s;
  int n, c;
  while(t--) {
    cin >> s >> n;
    c = 0;

    for(int i=0; i<=s.length()-n; i++) {
      if(s[i] == '-') {
	c++;
	for(int j=i; j<i+n; j++) {
	  if(s[j] == '-') s[j] = '+';
	  else s[j] = '-';
	}
      }
    }

    if(allFliped(s)) printf("Case #%d: %d\n", ++tc, c);
    else printf("Case #%d: IMPOSSIBLE\n", ++tc);
  }
  
  return 0;
}
