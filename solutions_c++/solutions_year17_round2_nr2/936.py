#include <bits/stdc++.h>

using namespace std;

int T, cs, R, O, Y, G, B, V, n;
string a, b, c;

string T1(){
  string ret = a + b + c;
  int t1 = R, t2 = Y, t3 = B;
  string x = "";
  x.push_back(ret[0]);
  for(int i=1; i<ret.size(); i++){
    if(((x.back() == 'R' && ret[i] == 'B') || (x.back() == 'B' && ret[i] == 'R')) && t2){
      x.push_back('Y');
      t2--;
    }
    if(((x.back() == 'R' && ret[i] == 'Y') || (x.back() == 'Y' && ret[i] == 'R')) && t3){
      x.push_back('B');
      t3--;
    }
    if(((x.back() == 'Y' && ret[i] == 'B') || (x.back() == 'B' && ret[i] == 'Y')) && t1){
      x.push_back('R');
      t1--;
    }
    x.push_back(ret[i]);
  }
  if(((x.back() == 'R' && x[0] == 'B') || (x.back() == 'B' && x[0] == 'R')) && t2){
    x.push_back('Y');
    t2--;
  }
  if(((x.back() == 'R' && x[0] == 'Y') || (x.back() == 'Y' && x[0] == 'R')) && t3){
    x.push_back('B');
    t3--;
  }
  if(((x.back() == 'Y' && x[0] == 'B') || (x.back() == 'B' && x[0] == 'Y')) && t1){
    x.push_back('R');
    t1--;
  }
  if(x.size() != n || t1 || t2 || t3)
    return ".";
  x.push_back(x[0]);
  for(int i=1; i<x.size(); i++){
    if(x[i] == x[i-1])
      return ".";
    int f1 = x[i] == 'R' || x[i] == 'O' || x[i] == 'V';
    int f2 = x[i - 1] == 'R' || x[i - 1] == 'O' || x[i - 1] == 'V';
    if(f1 && f2)
      return ".";
    f1 = x[i] == 'B' || x[i] == 'G' || x[i] == 'V';
    f2 = x[i - 1] == 'B' || x[i - 1] == 'G' || x[i - 1] == 'V';
    if(f1 && f2)
      return ".";
    f1 = x[i] == 'Y' || x[i] == 'O' || x[i] == 'G';
    f2 = x[i - 1] == 'Y' || x[i - 1] == 'O' || x[i - 1] == 'G';
    if(f1 && f2)
      return ".";
  }
  x.pop_back();
  return x;
}
string T2(){
  string ret = a + c + b;
  int t1 = R, t2 = Y, t3 = B;
  string x = "";
  x.push_back(ret[0]);
  for(int i=1; i<ret.size(); i++){
    if(((x.back() == 'R' && ret[i] == 'B') || (x.back() == 'B' && ret[i] == 'R')) && t2){
      x.push_back('Y');
      t2--;
    }
    if(((x.back() == 'R' && ret[i] == 'Y') || (x.back() == 'Y' && ret[i] == 'R')) && t3){
      x.push_back('B');
      t3--;
    }
    if(((x.back() == 'Y' && ret[i] == 'B') || (x.back() == 'B' && ret[i] == 'Y')) && t1){
      x.push_back('R');
      t1--;
    }
    x.push_back(ret[i]);
  }
  if(((x.back() == 'R' && x[0] == 'B') || (x.back() == 'B' && x[0] == 'R')) && t2){
    x.push_back('Y');
    t2--;
  }
  if(((x.back() == 'R' && x[0] == 'Y') || (x.back() == 'Y' && x[0] == 'R')) && t3){
    x.push_back('B');
    t3--;
  }
  if(((x.back() == 'Y' && x[0] == 'B') || (x.back() == 'B' && x[0] == 'Y')) && t1){
    x.push_back('R');
    t1--;
  }
  if(x.size() != n || t1 || t2 || t3)
    return ".";
  x.push_back(x[0]);
  for(int i=1; i<x.size(); i++){
    if(x[i] == x[i-1])
      return ".";
    int f1 = x[i] == 'R' || x[i] == 'O' || x[i] == 'V';
    int f2 = x[i - 1] == 'R' || x[i - 1] == 'O' || x[i - 1] == 'V';
    if(f1 && f2)
      return ".";
    f1 = x[i] == 'B' || x[i] == 'G' || x[i] == 'V';
    f2 = x[i - 1] == 'B' || x[i - 1] == 'G' || x[i - 1] == 'V';
    if(f1 && f2)
      return ".";
    f1 = x[i] == 'Y' || x[i] == 'O' || x[i] == 'G';
    f2 = x[i - 1] == 'Y' || x[i - 1] == 'O' || x[i - 1] == 'G';
    if(f1 && f2)
      return ".";
  }
  x.pop_back();
  return x;
}

int main()
{
  freopen("B-large (1).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    a = b = c = "";
    printf("Case #%d: ", ++cs);
    scanf("%d %d %d %d %d %d %d", &n, &R, &O, &Y, &G, &B, &V);
    if(B){
      a.push_back('B');
      --B;
    }
    while(O){
      a.push_back('O');
      O--;
      if(!B) break;
      a.push_back('B');
      --B;
    }
    if(R){
      b.push_back('R');
      --R;
    }
    while(G){
      b.push_back('G');
      G--;
      if(!R) break;
      b.push_back('R');
      --R;
    }
    if(Y){
      c.push_back('Y');
      --Y;
    }
    while(V){
      c.push_back('V');
      V--;
      if(!Y) break;
      c.push_back('Y');
      --Y;
    }
    while(R && Y && B){
      int mx = max(R, max(Y, B));
      int mn = min(R, min(Y, B));
      if(R == mx){
        if(Y == mn){
          b.push_back('B');
          --B;
        }else{
          b.push_back('Y');
          --Y;
        }
        b.push_back('R');
        --R;
      }else if(Y == mx){
        if(R == mn){
          c.push_back('B');
          --B;
        }else{
          c.push_back('R');
          --R;
        }
        c.push_back('Y');
        --Y;
      }else{
        if(R == mn){
          a.push_back('Y');
          Y--;
        }else{
          a.push_back('R');
          --R;
        }
        a.push_back('B');
        B--;
      }
    }
    while(Y && B){
      a.push_back('Y');
      a.push_back('B');
      --Y;
      --B;
    }
    while(B && R){
      a.push_back('R');
      a.push_back('B');
      --R;
      --B;
    }
    while(R && Y){
      c.push_back('R');
      c.push_back('Y');
      --R;
      --Y;
    }
    string ans = T1();
    if(ans != "."){
      cout << ans << "\n";
      continue;
    }
    ans = T2();
    if(ans != ".")
      cout << ans;
    else
      cout << "IMPOSSIBLE";
    cout << "\n";
  }
  return 0;
}
