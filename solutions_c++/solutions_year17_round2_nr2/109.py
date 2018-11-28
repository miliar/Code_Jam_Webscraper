#include <bits/stdc++.h>

using namespace std;

const int maxn = 1010;
int n,m;
int d[6];
int ini[6];
string c = "ROYGBV";
bool flag;

bool checkcaseputo(){
  for(int i = 0; i < 6; ++i){
    int i2 = (i+3)%6;
//     if(flag) cerr << i << ' ' << d[i] << ' ' << d[i2] << '\n';
    if(d[i] + d[i2] == n){
      if(d[i] == d[i2]){
        for(int j = 0; j < d[i]; ++j){
          cout << c[i] << c[i2];
        }
        cout << '\n';
      }
//       else continue;
      else cout << "IMPOSSIBLE\n";
      return true;
    }
  }
  return false;
}

bool bad(){
  for(int i = 0; i < 6; ++i){
    if((i&1) and d[i] and (d[i] >= d[(i+3)%6])){
      return true;
    }
  }
  return false;
}

bool bad2(){
  for(int i = 0; i < 6; ++i){
//     if(flag) cerr << m << ' ' << i << ' ' << d[i] << ' ' << m-d[i] << '\n';
    if(i%2 == 0 and d[i] != m and d[i] > m-d[i]){
      return true;
    }
  }
  return false;
}

int main(){
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
//     flag = true;
    cin >> n;
    for(int i = 0; i < 6; ++i) cin >> d[i];
    cout << "Case #" << cass << ": ";
    if(checkcaseputo()) continue;
//     if(flag){
//       cerr << n << '\n';
//       for(int j = 0; j < 6; ++j) cerr << d[j] << ' ';
//       cerr << '\n';
//       
//     }
    if(bad()){
      cout << "IMPOSSIBLE\n";
      continue;
    }
    m = n;
    for(int i = 0; i < 6; ++i){
      if(i&1){
        int i2 = (i+3)%6;
        d[i2] -= d[i];
        m -= 2*d[i];
      }
    }
    if(bad2()){
      cout << "IMPOSSIBLE\n";
      continue;
    }
    int big = 0;
    memset(ini,0,sizeof(ini));
    for(int i = 0; i < 6; ++i){
      if(i%2 == 0 and d[big] < d[i]) big = i;
    }
    int aux = (big+2)%6;
    int aux2 = (aux+2)%6;
    int k = d[aux]+d[aux2]-d[big];
    int cont = 0;
    for(int i = 0; i < k; ++i){
      cont += 3;
      cout << c[big];
      if(ini[big] == 0){
        int dbig = (big+3)%6;
        for(int j = 0; j < d[dbig]; ++j) cout << c[dbig] << c[big];
      }
      ++ini[big];
      cout << c[aux];
      if(ini[aux] == 0){
        int daux = (aux+3)%6;
        for(int j = 0; j < d[daux]; ++j) cout << c[daux] << c[aux];
      }
      ++ini[aux];
      cout << c[aux2];
      if(ini[aux2] == 0){
        int daux = (aux2+3)%6;
        for(int j = 0; j < d[daux]; ++j) cout << c[daux] << c[aux2];
      }
      ++ini[aux2];
    }
    for(int i = k; i < d[aux]; ++i){
      cont += 2;
      cout << c[big];
      if(ini[big] == 0){
        int dbig = (big+3)%6;
        for(int j = 0; j < d[dbig]; ++j) cout << c[dbig] << c[big];
      }
      ++ini[big];
      cout << c[aux];
      if(ini[aux] == 0){
        int daux = (aux+3)%6;
        for(int j = 0; j < d[daux]; ++j) cout << c[daux] << c[aux];
      }
      ++ini[aux];
    }
    for(int i = k; i < d[aux2]; ++i){
      cont += 2;
      cout << c[big];
      if(ini[big] == 0){
        int dbig = (big+3)%6;
        for(int j = 0; j < d[dbig]; ++j) cout << c[dbig] << c[big];
      }
      ++ini[big];
      cout << c[aux2];
      if(ini[aux2] == 0){
        int daux = (aux2+3)%6;
        for(int j = 0; j < d[daux]; ++j) cout << c[daux] << c[aux2];
      }
      ++ini[aux2];
    }
    cout << '\n';
    if(cont != m){
      cerr << cont << ' ' << m << '\n';
      cerr << "BAAAAD " << cass << '\n';
    }
  }
}