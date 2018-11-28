#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef long long ll;

#define fi first
#define se second
#define pb push_back
#define rep(i, a, b) for(int (i)=(a); (i)<(b); (i)++)

const int INF = 0x3f3f3f3f;


int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  
  int T, m, n;
  string tmp;
  cin >> T;
  rep(kase, 1, T+1){
    vector<string> V;
    cin >> m >> n;
    rep(i, 0, m){
      cin >> tmp;
      V.push_back(tmp);
    }
    rep(j, 0, n){
      rep(i, 0, m){
        if (V[i][j] != '?'){
          char cur = V[i][j];
          if (i>0 && V[i-1][j] == '?'){
            for (int i2=i-1; i2>=0 && V[i2][j] == '?'; i2--){
              V[i2][j] = cur;
            }
          }
          if (i<m-1 && V[i+1][j] == '?'){
            for (i=i+1; i<m && V[i][j] == '?'; i++){
              V[i][j] = cur;
            }
            i--;
          }
        }
      }
    }
    
    
    rep(i, 0, m){
      rep(j, 0, n){
        if (V[i][j] != '?'){
          char cur = V[i][j];
          if (j>0 && V[i][j-1] == '?'){
            for (int j2=j-1; j2>=0 && V[i][j2] == '?'; j2--){
              V[i][j2] = cur;
            }
          }
          if (j<n-1 && V[i][j+1] == '?'){
            // cout << V[i] << endl;
            for (j=j+1; j<n && V[i][j] == '?'; j++){
              V[i][j] = cur;
            }
            j--;
          }
        }
      }
    }
    
    cout << "Case #" << kase << ":\n";
    for (auto s : V){
      cout << s << "\n";
    }
  }
  return 0;
}  

/*
    Test for speed:

    #include <chrono>
    using namespace std::chrono;
    high_resolution_clock::time_point start, end;
    start = high_resolution_clock::now();
    //
    end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds> (end - start).count();
    cout << duration << '\n';
*/
