#include<iostream>
#include<sstream>
#include<vector>
#include<queue>
#include<exception>

using namespace std;


string casefunc(const int N, const int K){

  //cout << "N:" << N << " K:" << K << endl;

  priority_queue<int> Q;
  Q.push(N);
  int r,l;
  for(int k = 0; k < K; k++ ){
    // k'th person entering
    int n = Q.top();
    Q.pop();
    r = n/2;
    Q.push(r);
    l = (n-1)/2;
    Q.push(l);
    //cout << "|" << l << "," << r << endl;
  }

  stringstream ss;
  ss << r << " " << l;
  return ss.str();
}

int main(){
  stringstream ss;
  int T;
  cin >> T;
  
  typedef long long int lli;
  for(int i = 1; i <= T; i++){
    int N;
    cin >> N;
    int K;
    cin >> K;
    string r = casefunc(N,K);
    cout << "Case #" << i << ": " << r << endl;
  }
  return 0;
}







