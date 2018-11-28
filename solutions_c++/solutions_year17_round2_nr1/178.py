#include <iostream>
#include <iomanip>
using namespace std;

double horses[5000][2];


int main() {
  int T;

  cin >> T ;

  for(int t=1; t<=T; t++) {
    double D;
    int N;
    cin >> D >> N;
    double low=1000000001;

    for(int i=0; i<N; i++) {
      cin >> horses[i][0] >> horses[i][1];
      double next=horses[i][1]/(D-horses[i][0]);
      if (next<low)
	low=next;
    }
    cout <<setprecision(8) <<"Case #" << t << ": " << low*D << endl;
  }

  return 0;
}
    

    
