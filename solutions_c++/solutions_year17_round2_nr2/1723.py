#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;

int r,y,b;
int o,g,v;
int n;

string addR(string s){
  if(g > 0){
    for(int i = 0;i < g;++i){
      s += "RG";
    }
    g = 0;
  }
  s += "R";
  --r;
  return s;
}
string addY(string s){
  if(v > 0){
    for(int i = 0;i < v;++i){
      s += "YV";
    }
    v = 0;
  }
  s += "Y";
  --y;
  return s;
}

string addB(string s){
  if(o > 0){
    for(int i = 0;i < o;++i){
      s += "BO";
    }
    o = 0;
  }
  s += "B";
  --b;
  return s;
}



void solve(){
  cin >> n;
  // r, o, y, g, b, v;
  cin >> r >> o >> y
      >> g >> b >> v;
  if(o > b || g > r || v > y){
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  if(o != 0 && o == b){
    if(o+b != n){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    for(int i = 0;i < o;++i){
      cout << "BO";
    }
    cout << endl;
    return;
  }
  if(g != 0 && g == r){
    if(g+r != n){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    for(int i = 0;i < g;++i){
      cout << "RG";
    }
    cout << endl;
    return;
  }
  if(v != 0 && v == y){
    if(v+y != n){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    for(int i = 0;i < v;++i){
      cout << "YV";
    }
    cout << endl;
    return;
  }
  int cr = r,cy = y,cb = b;;
  r -= g;y -= v;b -= o;
  if(r > y+b || y > r+b || b > r+y){
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  string res = "";
  if(cr > max(cb,cy)){
    res = addR(res);
  }else if(cy > cb){
    res = addY(res);
  }else{
    res = addB(res);
  }
  n = r+y+b;
  for(int i = 0;i < n;++i){
    if(res[i] ==  'R'){
      if(y > b){
        res = addY(res);
      }else if(y == b && res[0] == 'Y'){
        res = addY(res);
      }else{
        res = addB(res);
      }
    }else if(res[i] ==  'Y'){
      if(r > b){
        res = addR(res);
      }else if(r == b && res[0] == 'R'){
        res = addR(res);
      }else{
        res = addB(res);
      }
    }else if(res[i] ==  'B'){
      if(r > y){
        res = addR(res);
      }else if(r == y && res[0] == 'R'){
        res = addR(res);
      }else{
        res = addY(res);
      }
    }
  }
  cout << res << endl;
}


int main(void){
  int t;
  cin >> t;
  for(int i = 0;i < t;++i){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
