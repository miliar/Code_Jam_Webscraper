#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int ceil(int n, int d) {
  return (n+d-1)/d;
}

int main(){
  ios_base::sync_with_stdio(false);
  int T;
  int n, c, m;
  int P, C;
  cin >> T;
  for(int ind=0; ind<T; ind++){
    cin >> n >> c >> m;
    vector<int> b_p_c(c+1, 0);
    vector<int> b_p_p(n+1, 0);
    for (int i=0; i<m; i++) {
      cin >> P >> C;
      b_p_c[C]++;
      b_p_p[P]++;
    }
    int A=0; // max of b_p_c
    for (int i=1; i<=c; i++) A = max(A, b_p_c[i]);
    int sum = 0;
    int B=0; //max of ratios
    for (int i=1; i<=n; i++) {
      sum += b_p_p[i];
      B = max(B, ceil(sum, i));
    }
    int X = max(A, B); // n of vagons
    int n_p = 0;
    int space = 0;
    for (int i=1; i<=n; i++) {
      if (X >= b_p_p[i]) space += (X - b_p_p[i]);
      else {
        space -= (b_p_p[i]-X);
        n_p += (b_p_p[i]-X);
      }      
    }
    cout << "Case #" << (ind+1) << ": " << X << " " << n_p << endl;
 
  }
  return 0;
}