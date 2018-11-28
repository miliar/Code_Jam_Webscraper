
#include <iostream>

#define INF 100000

using namespace std;

void swap(string &pank, int p, int k){
  for(int i = p; i < p + k; i++){
    if(pank[i] == '-')
      pank[i] = '+';
    else
      pank[i] = '-';
  }
}


int compute(string &pank, int k, int p){
  if(pank.size() < p + k){
    for(int i = 0; i < pank.length(); i++){
      if(pank[i] == '-')
        return INF;
    }
    return 0;
  }

  for(int i = 0; i < p; i++){
    if(pank[i] == '-')
      return INF;
  }

  int m = INF;
  swap(pank, p, k);
  m = min(m, compute(pank, k, p + 1) + 1);
  swap(pank, p, k);
  m = min(m, compute(pank, k, p + 1));

  return m;
}

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++){
    string pank;
    int k;
    cin >> pank >> k;
    int n = compute(pank, k, 0);
    cout << "Case #" << i << ": ";
    if(n == INF)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << n << endl;
  }

  return 0;
}
