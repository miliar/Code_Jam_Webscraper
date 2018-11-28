#include<iostream>
#include<iomanip>

using namespace std;

int main(){
  int T;
  cin >> T;
  int D,N;
  for(int i = 0; i < T; i++){
    cin >> D >> N;
    int K,S;
    double maxTime = 0.0;
    for(int j = 0; j < N; j++){
      cin >> K >> S;
      double distLeft = D-K;
      double time = distLeft/S;
      if(time > maxTime) maxTime = time;
    }
    cout << fixed;
    cout << setprecision(6);
    cout << "Case #" << i+1 << ": " << double(D)/maxTime << endl;
  }
  return 0;
}
