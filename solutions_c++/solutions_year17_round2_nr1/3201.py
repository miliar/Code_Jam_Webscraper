#include<iostream>
#include<iomanip>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<exception>

using namespace std;

typedef long double lld;

int i, debug=0;

string problem(int D, int N, vector<int> K, vector<int> S){
  lld tmax = 0;
  for(int i = 0; i < N; i++){
    
    lld t = (D-K[i])/lld(S[i]);
    if( debug ) cout << "t:" << t << " :" << D << "," << K[i] << "," << S[i] << endl;
    tmax = t > tmax ? t : tmax;
  }
  lld smax = D/tmax;
  stringstream ss;
  ss << fixed << setprecision(13) << smax;
  return ss.str();
}

int main(){
  int T;
  cin >> T;
  for(i = 1; i <= T; i++){
    int D,N;
    //debug = 0 ; //i == 36;
    cin >> D >> N;
    if(debug) cout << "D,N: " << D << " " << N << endl;
    vector<int> k, s;
    for(int j = 0; j < N; j++){
      int K, S;
      cin >> K >> S;
      if(debug) cout << "::: K,S:" << K << ", " << S << endl;
      k.push_back(K);
      s.push_back(S);
    }
    string result = problem(D,N,k,s);
    cout << "Case #" << i << ": " <<result << endl;
  }
  return 0;
}
