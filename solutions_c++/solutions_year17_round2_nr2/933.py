#include <bits/stdc++.h>

using namespace std;

int n, r, o, y, g, b, v;
int tn;
char str[1020];
char ans[1020];
char R, B, Y;

char gt() {
  if (r) {
    r--;
    return R;
  }
  else if (b) {
    b--;
    return B;
  }
  else if (y) {
    y--;
    return Y;
  }
  else {
    return '#';
  }
}

void getans() {
  int p = 0;
  for (int i = 0; i < tn; i++) {
    ans[p++] = str[i];
    if (str[i] == 'R') {
      while(g) {
        ans[p++] = 'G';
        ans[p++] = 'R';
        g--;
      }
    }
    else if (str[i] == 'B') {
      while(o) {
        ans[p++] = 'O';
        ans[p++] = 'B';
        o--;
      }
    }
    else if (str[i] == 'Y') {
      while(v) {
        ans[p++] = 'V';
        ans[p++] = 'Y';
        v--;
      }
    }
  }
  ans[p++] = 0;
}


int main() {
  
  int T;
  cin >> T;
  for (int ka = 1; ka <= T; ka++) {
    cin >> n;
    cin >> r >> o >> y >> g >> b >> v ;
    bool ok = true;
    
    if (r == g && r + g == n) {
      for (int i = 0; i < n; i++) {
        if (i%2) ans[i] = 'R';
        else ans[i] = 'G';
      }
      ans[n] = 0;
      printf("Case #%d: %s\n", ka, ans);
      continue;
    }

    if (b == o && b + o == n) {
      for (int i = 0; i < n; i++) {
        if (i%2) ans[i] = 'B';
        else ans[i] = 'O';
      }
      ans[n] = 0;
      printf("Case #%d: %s\n", ka, ans);
      continue;
    }
    
    if (y == v && y + v == n) {
      for (int i = 0; i < n; i++) {
        if (i%2) ans[i] = 'Y';
        else ans[i] = 'V';
      }
      ans[n] = 0;
      printf("Case #%d: %s\n", ka, ans);
      continue;
    }


    if (r <= g && g)
      ok = false;
    if (b <= o && o)
      ok = false;
    if (y <= v && v)
      ok = false;

    if (!ok) {
      printf("Case #%d: %s\n",ka, "IMPOSSIBLE");
      continue;
    }

    r -= g;
    b -= o;
    y -= v;
  
    tn = n - g*2 - o*2 - v*2;

    R = 'R';
    B = 'B';
    Y = 'Y';

    if (r < b) {
      swap(r, b);
      swap(R, B);
    }
    if (r < y) {
      swap(r, y);
      swap(R, Y);
    }
    
    for (int i = 0; i < tn; i+=2) {
      str[i] = gt();
    }
    for (int i = 1; i < tn; i+=2) {
      str[i] = gt();
    }
    
    str[tn] = 0;

    for (int i = 0; i < tn; i++) {
      if (str[i] == str[(i+1)%tn]) {
        ok = false;
      }
    }

    if (ok) {
      getans();
      printf("Case #%d: %s\n", ka, ans);
    }
    else {
      printf("Case #%d: %s\n", ka, "IMPOSSIBLE");
    }
  }

  return 0;
}
