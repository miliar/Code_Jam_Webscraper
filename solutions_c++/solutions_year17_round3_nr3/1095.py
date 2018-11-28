#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int t, no = 1;
  cin >> t;
  while(t--){
    int n,k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector<double> cores;
    for(int i = 0; i < n; i++){
      double tmp;
      cin >> tmp;
      cores.emplace_back(tmp);
    }
    sort(cores.begin(), cores.end());
    int first = 0, last = 0;
    while(u > 0 && last != n-1){
      while(last != n-1 && cores[first] == cores[last]){
        last++;
      }
      if(last == n-1 && cores[first] == cores[last]) break;
      if(u > (cores[last]-cores[first])*(last-first)){
        double tmp = cores[last]-cores[first];
        for(int i = first; i < last; i++){
          cores[i] += tmp;
          u -= tmp;
        }
      } else {
        double tmp = (double) u/(last-first);
        for(int i = first; i < last; i++){
          cores[i] += tmp;
        }
        u = 0;
      }
    }
    double left_over = 0;
    if(cores[n-1] == cores[0]){
      left_over = (double) u/n;
    }
    double probability = 1;
    for(int i = 0; i < n; i++){
      probability*=(cores[i]+left_over);
    }
    if(probability > 1){
      for(int i = 0; i < n; i++){
        cout << cores[i] << " ";
      }
      cout << endl;
    }
    cout.precision(9);
    cout << "Case #" << no++ << ": " << fixed << probability << endl;
  }
  return 0;
}

