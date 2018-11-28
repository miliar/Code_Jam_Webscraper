#include <bits/stdc++.h>
using namespace std;

const int N = 20;
int t, T, v[N], n;
char s[N];

int main() {
  scanf("%d", &T);
  while(t++ < T) {
    scanf("%s", s);
    n = strlen(s);

    for(int i=0; i<n; ++i)
      v[i] = s[i] - '0';

    for(int i=n-2; i>=0; --i) if (v[i] > v[i+1]) {
      v[i]--;
      for(int j=i+1; j<n; ++j) v[j] = 9;
    }

    printf("Case #%d: ", t);
    int i=0;
    while(!v[i]) i++;
    while(i < n) printf("%d", v[i++]);
    printf("\n");
  }
  return 0;
}
