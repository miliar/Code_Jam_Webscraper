#include <string>
#include <iostream>
#include <assert.h>

using namespace std;

static int charToInt( char ch )
{
  return ch - '0';
}

static bool process( const string& maxNumber, char minDigit, string& tidyNumber )
{
  assert( maxNumber.length() > 0 );
  const char firstDigit = maxNumber[0];
  if( firstDigit < minDigit ) {
    return false;
  }
  if( maxNumber.length() == 1 ) {
    tidyNumber = firstDigit;
    return true;
  }
  string tail;
  if( process( string( maxNumber.begin() + 1, maxNumber.end() ), firstDigit, tail ) ) {
    tidyNumber = firstDigit + tail;
    return true;
  }
  if( firstDigit > minDigit ) {
    const char prevDigit = firstDigit - 1;
    if( prevDigit > '0' ) {
      tidyNumber += prevDigit;
    }
    tidyNumber += string( maxNumber.length() - 1, '9' );
    return true;
  }
  return false;
}

static string solve( const string& maxNumber )
{
  string tidyNumber;
  assert( process( maxNumber, '0', tidyNumber ) );
  return tidyNumber;
}

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    string s;
    cin >> s;

    cout << "Case #" << i+1 << ": " << solve( s ) << endl;
  }
}