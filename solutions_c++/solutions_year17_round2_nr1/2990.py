#include <iostream>  
#include <iomanip>  
#include <string>
#include <vector>

using namespace std;  

float getTime( int d, int k, int s ) {
    return float(d-k)/float(s); 
}

int main() {
  int t;
  
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int d, n;
    cin >> d >> n;
    float max_time = 0;
    for (int j = 1; j <= n; ++j) {
        int k, s;
        cin >> k >> s;

        float cur_time = getTime(d, k, s);

        if ( max_time < cur_time )
            max_time = cur_time; 
    }

    cout << "Case #" << i << ": " << fixed << setprecision(6) << float(d)/max_time << endl;
  }

  return 0;
}
