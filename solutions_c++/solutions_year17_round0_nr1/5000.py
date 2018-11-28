#include<iostream>
#include<sstream>
#include<vector>
#include<exception>

using namespace std;

void flip(char & c){
  if( c == '-'){
    c = '+';
  }
  else if (c == '+'){
    c = '-';
  }
  else {
      throw domain_error("neither plus nor minus");
  }
}


string casefunc(string S, int K){
  //cout << "{" << S << "}" << K << endl;
  const int n = S.size();
  int nflips = 0;
  for(int i = 0; i < n; i++){
    char & c = S[i];
    if( c == '+' ){}
    else if( c == '-' ){
      for(int k = 0; k < K; k++){
        int j = i+k;
        char & c = S[j];
        if( j >= n ){
          return "IMPOSSIBLE";
        } else {
          flip(c);
        }
      }
      nflips += 1;
    }
    else{
      throw domain_error("neither plus nor minus");
    }
  }

  stringstream ss;
  ss << nflips;
  return ss.str();
}

int main(){
  stringstream ss;
  int N;
  cin >> N;
  
  typedef long long int lli;
  for(int i = 1; i <= N; i++){
    string s;
    cin >> s;
    int k;
    cin >> k;
    string r = casefunc(s,k);
    cout << "Case #" << i << ": " << r << endl;
  }
  return 0;
}







