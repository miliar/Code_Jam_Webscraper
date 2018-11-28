// Programmer: Tanner Winkelman
// 4/7/2017
// Purpose: Solve tidy number problem:
//   Google Code Jam Qualification Round 2017 Problem B
// Uses class bigInt, which I had prepared.

#include <iostream>
#include <cmath>
using namespace std;




class bigInt
{

public:
  string digits;

  
  bigInt( const long source )
  {
    long exp = 0;
    while( pow( 10, exp ) <= source )
      exp++;
    while( exp )
    {
      exp--;
      digits += '0' + ((source / static_cast<long>(pow( 10, exp ))) % 10);
    }
  }
  
  bigInt() : digits("") {}
  
  bigInt operator+( const bigInt & rhs )
  {
    long ourIndex = digits.length();
    long rhsIndex = rhs.digits.length();
    short sum = 0;
    bool carry = 0;
    short ourDigitValue;
    short rhsDigitValue;
    bigInt returnable (0);
    if( !ourIndex )
      return rhs;
    else if( !rhsIndex )
      return *this;
    while( ourIndex || rhsIndex || carry )
    {
      if( ourIndex )
      {
        ourIndex--;
        ourDigitValue = digits[ourIndex] - '0';
      }
      else
        ourDigitValue = 0;
      if( rhsIndex )
      {
        rhsIndex--;
        rhsDigitValue = rhs.digits[rhsIndex] - '0';
      }
      else
        rhsDigitValue = 0;
      sum = ourDigitValue + rhsDigitValue;
      sum += carry;
      carry = (sum >= 10);
      sum %= 10;
      returnable.digits += (sum + '0');
    }
    
    char swapSpace;
    for( long k = 0; k < returnable.digits.length() / 2; k++ )
    {
      swapSpace = returnable.digits[k];
      returnable.digits[k] = returnable.digits[returnable.digits.length() - k - 1];
      returnable.digits[returnable.digits.length() - k - 1] = swapSpace;
    }
    
    return returnable;
  }
  
  
  bigInt operator*( const bigInt & rhs )
  {
    bigInt returnable (0);
    for( long k = 0; k < digits.length() + rhs.digits.length(); k++ )
      returnable.digits += "0";
    for( long thisIndex = 0; thisIndex < digits.length(); thisIndex++ )
    {
      for( long rhsIndex = 0; rhsIndex < rhs.digits.length(); rhsIndex++ )
      {
        
        long product = ( digits[thisIndex] - '0' ) * ( rhs.digits[rhsIndex] - '0' );
        long retIndex = returnable.digits.length() - 1 - (digits.length() - thisIndex - 1) - (rhs.digits.length() - rhsIndex - 1);
        while( product > 0 )
        {
          product += returnable.digits[retIndex] - '0';
          returnable.digits[retIndex] = (product % 10) + '0';
          product /= 10;
          
          retIndex--;
        }
      }
    }
    
    if( returnable.digits[0] == '0' )
      returnable.digits.erase(0,1);
    
    return returnable;
  }
  
  // decrementDigit() decrements the digit at the exponentOf10
  // decrementDigit() recursively decrements the digit to the left
  // if the digit at the exponentOf10 is 0
  // decrementDigit() also turns all digits to the right to '9'
  void decrementDigit( const long exponentOf10 )
  {
    long digitsLength = digits.length();
    long targetDigitIndex = digitsLength - exponentOf10 - 1;
    if( digits[targetDigitIndex] > '0' )
    {
      digits[targetDigitIndex] -= 1;
    }
    else
    {
      for( long k = targetDigitIndex; k < digitsLength; k++ )
        digits[k] = '9';
      decrementDigit( exponentOf10 + 1 );
    }
    while( digits.length() && digits[0] == '0' )
      digits.erase(digits.begin());
    return;
  }
  
  // returns the exponent of 10 where tidyness ends
  // (321 -> 0)(322 -> 1)(100 -> 0)
  // returns -1 if tidy
  long tidy()
  {
    bool tidySoFar = true;
    long digitsLength = digits.length();
    long index = digitsLength;
    char firstDigit = '0';
    long k = 0;
    while( digits[k] == '0' )
      k++;
    firstDigit = digits[k];
    while( tidySoFar && index > 1 )
    {
      index--;
      if( digits[index] < digits[index - 1] || digits[index] < firstDigit )
        tidySoFar = false;
    }
    if( tidySoFar )
      index = -1;
    return (digits.length() - index - 1);
  }
  
  
  
  friend ostream & operator<<( ostream & lhs, const bigInt & rhs );
};



bigInt operator+( const long lhs, const bigInt & rhs )
{
  bigInt l ( lhs );
  return l + rhs;
}

bigInt operator*( const long lhs, const bigInt & rhs )
{
  bigInt l ( lhs );
  return l * rhs;
}

bigInt factorial( const long argument )
{
  long counter = argument;
  bigInt returnable = 1;
  while( counter > 1 )
  {
    returnable = returnable * counter;
    counter--;
  }
  return returnable;
}



ostream & operator<<( ostream& lhs, const bigInt & rhs )
{
  if( rhs.digits.length() )
    lhs << rhs.digits;
  else
    lhs << '0';
  return lhs;
}




int main()
{
  long numCases;
  cin >> numCases;
  bigInt N;
  for( long k = 1; k <= numCases; k++ )
  {
    cin >> N.digits;
    bool cont = true;
    long expWhereTidynessBroken;
    while( cont )
    {
      expWhereTidynessBroken = N.tidy();
      
      if( expWhereTidynessBroken >= N.digits.length() )
        cont = false;
      else
      {
        //cout << N << " " << flush;
        N.decrementDigit( expWhereTidynessBroken );
        //cout << N << " " << flush;
      }
    }
    
    cout << "Case #" << k << ": " << N << endl;
    
  }
  
  return 0;
}
