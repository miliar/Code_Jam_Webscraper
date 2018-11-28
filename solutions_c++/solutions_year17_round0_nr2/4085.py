#include <iostream>
#include <string>
#include <vector>
using namespace std;

string str;
vector<int> number;

void solve() {
  int j = -1;
  for( int i = 1; i < number.size(); i++ ) {
    if( number[i - 1] > number[i] ) {
      j = i - 1;
      while( j > 0 && number[j - 1] == number[j] ) {
        j--;
      }
      break;
    }
  }
  if( j == -1 ) {
    return;
  }
  number[j] -= 1;
  for( int i = j + 1; i < number.size(); i++ ) {
    number[i] = 9;
  }
}

string printTidyNumber() {
  string tidyNumber = "";
  int i = 0;
  for( ; i < number.size(); i++ ) {
    if( number[i] != 0 ) {
      break;
    }
  }
  for( ; i < number.size(); i++ ) {
    tidyNumber.push_back( to_string( number[i] )[0] );
  }
  return tidyNumber;
}

void setNumber() {
  number.clear();
  int i = 0;
  for( ; i < str.size(); i++ ) {
    if( str[i] != '0' ) {
      break;
    }
  }
  for( ; i < str.size(); i++ ) {
    int n = stoi( string( 1, str[i] ) );
    number.push_back( n );
  }
  if( number.size() == 0 ) {
    number.push_back( 0 );
  }
}

void main() {
  int t;
  cin >> t;
  const int NumOfCases = t + 1;

  for( int i = 1; i < NumOfCases; i++ ) {
    cin >> str;
    setNumber();
    solve();
    cout << "\nCase #" << i << ": " << printTidyNumber();
  }
}
