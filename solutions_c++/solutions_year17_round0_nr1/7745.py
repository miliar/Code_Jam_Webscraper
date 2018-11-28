#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
typedef long long ll;
#define F first
#define S second
#define N 2020

int t[N];

int main(){
  int T; cin >> T;
  for(int j=0; j<T; ++j){
    int k; string s;
    cin >> s >> k;
    int n = s.size(), V=0;
    for(int i=0; i+k <= n; ++i){
      t[i+1] += t[i];
      t[i] += (s[i]=='+'?1:0);
      if(t[i]%2 == 0) ++V, ++t[i+1], --t[i+k];
      t[i]=0;
    }
    int f = 1;
    for(int i =n-k+1; i<n; ++i) {
      t[i+1] += t[i];
      t[i] += (s[i]=='+'?1:0);
      if(t[i]%2 == 0) f=0;
      t[i] = 0;
    }
    for(int i=0; i<N; ++i) t[i] =0;
    cout << "Case #" << j+1 << ": ";
    if(f) cout << V << "\n";
    else cout << "IMPOSSIBLE\n";
  }
}
