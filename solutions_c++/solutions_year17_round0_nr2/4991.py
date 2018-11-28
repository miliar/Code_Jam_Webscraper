#include<iostream>
#include<sstream>
#include<vector>

using namespace std;


string casefunc(string snumber){

  const int n = snumber.size();

  //cout << "snumber:" << snumber << endl;
  //cout << "size:" << n << endl;

  vector<int> number;
  for(int i = 0; i < n; i++) number.push_back(snumber[i]-'0');

  int test;
  do {
    test = 0;
    for(int i = 0; i < n; i++){
      int & c = number[i];
      if(i > 0){
        int & cp = number[i-1];
        if( cp > c ){
          cp--;
          for(int j = i; j < n; j++){
            number[j] = 9;
          }
          test++;
        }
      }
    }
  }
  while( test > 0 );

  stringstream ss;
  bool started = false;
  for(int i = 0; i < n; i++){
    int c = number[i];
    if ( c > 0 ) started = true;
    if( started ){
      ss << c;
    }
  }
  if( ! started ){
    ss << 0;
  }
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
    string r = casefunc(s);
    cout << "Case #" << i << ": " << r << endl;
  }
  return 0;
}



// number:111111111111111110
// number:111111111111111119
