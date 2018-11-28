#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>

using namespace std;

int main(){
  
  int t, no_of_cases = 1;
  cin >> t;
  while(t--){

    int d,n;
    cin >> d >> n;
    long double max_time = 0;
    for(int i = 0; i < n; i++){
      int k, s;
      cin >> k >> s;
      max_time = max(max_time, (d - k)/((long double) s));
    }
    cout.precision(6);
    cout << "Case #" << no_of_cases << ": " << fixed << d/max_time << endl;
    no_of_cases++;
  }

  return 0;
}

