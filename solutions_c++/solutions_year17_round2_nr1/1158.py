#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;


int main(){
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for(int ind=0; ind<T; ind++){
    int d, n, k, s;
    cin >> d >> n;
    double v=-1;
    for(int i=0; i<n; i++){
      cin >> k >> s;
      if(v<0){
        v = (d+0.0)*s/(d-k);
      } else{
        v=  min(v, (d+0.0)*s/(d-k));
      }
    }
    
    cout << "Case #" << (ind+1) << ": " << setprecision(10) << v << endl;
  }
  return 0;
}