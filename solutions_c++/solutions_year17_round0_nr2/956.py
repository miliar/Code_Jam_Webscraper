#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>
using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

void solve() {
  uint64_t N;
  cin >> N;

  if (N < 10) {
    cout << N << endl; return;
  }

  vector<int> v;

  while (N > 0) {
    v.push_back(N % 10);
    N = N / 10;
  }

  reverse(v.begin(), v.end());

  for (int i = v.size()-1; i >=1; i--) {
    if (v[i-1] > v[i]) {
      v[i-1] = v[i-1]-1;
      for (int j = i; j < v.size(); j++)
	v[j] = 9;
    }
  }
  int i = 0;
  while (v[i] == 0)
    i++;
  while (i < v.size()) {
    cout << v[i]; 
    i++;
  }
  cout << endl;
}
       
int main(){
  int T;
  cin >> T; 
  string s; 

  for (int i = 0; i < T; i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  return 0;
}


