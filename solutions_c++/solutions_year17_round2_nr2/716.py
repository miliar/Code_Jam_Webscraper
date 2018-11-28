#include <cstdio>

int main() {
  int t; scanf("%d", &t);
  for(int _i=1; _i<=t; _i++) {
    printf("Case #%d: ", _i);
    int n, r, o, y, g, b, v; scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
    char s[1005];
    bool impossible = false;
    if(r>0) { s[0] = 'R'; r--; }
    else if(o>0) { s[0] = 'O'; o--; }
    else if(y>0) { s[0] = 'Y'; y--; }
    else if(g>0) { s[0] = 'G'; g--; }
    else if(b>0) { s[0] = 'B'; b--; }
    else if(v>0) { s[0] = 'V'; v--; }
    for(int i=1; i<n and !impossible; i++) {
      if(s[i-1] == 'G') {
        if(r>0) { s[i] = 'R'; r--; }
        else { impossible = true; continue; }
      }
      if(s[i-1] == 'O') {
        if(b>0) { s[i] = 'B'; b--; }
        else { impossible = true; continue; }
      }
      if(s[i-1] == 'V') {
        if(y>0) { s[i] = 'Y'; y--; }
        else { impossible = true; continue; }
      }
      if(s[i-1] == 'R') {
        if(g>0) { s[i] = 'G'; g--; }
        else if(b>0 and (b>y or (b==y and s[0]=='B'))) { s[i] = 'B'; b--; }
        else if(y>0) { s[i] = 'Y'; y--; }
        else { impossible = true; continue; }
      }
      if(s[i-1] == 'B') {
        if(o>0) { s[i] = 'O'; o--; }
        else if(r>0 and (r>y or (r==y and s[0]=='R'))) { s[i] = 'R'; r--; }
        else if(y>0) { s[i] = 'Y'; y--; }
        else { impossible = true; continue; }
      }
      if(s[i-1] == 'Y') {
        if(v>0) { s[i] = 'V'; v--; }
        else if(r>0 and (r>b or (r==b and s[0]=='R'))) { s[i] = 'R'; r--; }
        else if(b>0) { s[i] = 'B'; b--; }
        else { impossible = true; continue; }
      }
    }
    if(impossible or s[0]==s[n-1]) printf("IMPOSSIBLE\n");
    else {
      for(int i=0; i<n; i++) printf("%c", s[i]);
      printf("\n");
    }
  }
}
