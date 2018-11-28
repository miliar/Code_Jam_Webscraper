#include <iostream>
#include <string>

using namespace std;

int main(){
  int T;
  cin >> T;
  
  for( int t=1; t<=T; ++t ){
    string number;
    cin >> number;

    for( int i=number.length() - 1; i>0; --i ){
      if( number[i-1] > number[i] ){
        number[i-1] = number[i-1]-1;
        for( int j=i; j<number.length(); ++j ){
          number[j] = '9';
        }
      }
    }

    if( number[0] == '0' ){
      number = number.substr(1);
    }

    cout << "Case #" << t << ": " << number << endl;
  }
}
