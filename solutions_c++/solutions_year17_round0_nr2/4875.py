#include <bits/stdc++.h>
using namespace std;

int T, C = 1;
long long N;
string n, n1;

int ok(int i) {
  string s = to_string(i);
  for(int i = 1; i < int(s.size()); i++) 
    if(s[i] < s[i - 1]) return 0;
  return (i % 10) != 0;
}

int main() {
	freopen("../in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", C++);
    scanf("%lld", &N);
    if(!N) {
      cout << N << '\n';
      continue;
    }
    n1 = n = to_string(N);
    for(int j = int(n.size()) - 1; j > 0; --j) {
      if(n[j] == '0') 
        if(n[j - 1] != '0') break;
        else n[j] = '9';
    }
    n1 = n;
    long long ans = 0;
    for(char c = '1'; c <= '9'; c++) {
      n = n1;
      n[n.size() - 1] = c;
      for(int j = int(n.size()) - 1; j > 0; --j) {
        if(n[j] >= n[j - 1]) continue;
        n[j] = j == int(n.size()) - 1 ? '9' : n[j + 1];
        while(j - 1 >= 0 && n[j - 1] == '0') 
          n[j - 1] = '9', --j;
        if(j) n[j - 1]--;
      }
      reverse(n.begin(), n.end()); 
      while(n.size() && n.back() == '0') 
        n.pop_back();
      reverse(n.begin(), n.end()); 
      long long x = atoll(n.c_str());
      if(x <= N) ans = max(ans, x);
    }
    printf("%lld\n", ans);
  }
}
