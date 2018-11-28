#include<iostream>
#include<iomanip>
using namespace std;

const int MAX = 1010;

double solve(){
   int D, N;
   cin >> D >> N;
   int K[MAX],S[MAX];
   long double t = 0;
   for(int i = 0; i < N; i++){
      cin >> K[i] >> S[i];
      t = max(t, (long double)(D- K[i]) / (long double) S[i]);
   }
   return D/t;
}

int main(){
   int T; cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": " << fixed << setprecision(10) << solve() << endl;
   }   
   return 0;
}
