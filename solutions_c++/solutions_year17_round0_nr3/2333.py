// Programmer: Tanner Winkelman
// 4/8/2017
// Purpose: Solve bathroom stalls problem:
//   Google Code Jam Qualification Round 2017 Problem C
// Uses class bigInt, which I had prepared.


#include <iostream>
#include <cmath>
#include <vector>
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
  
  
  bigInt operator-( const bigInt & rhs )
  {
    bigInt returnable;
    returnable.digits = this->digits;
    long thisIndex = digits.length() - 1;
    long rhsIndex = rhs.digits.length() - 1;
    while( rhsIndex >= 0 )
    {
      returnable.digits[thisIndex] = (returnable.digits[thisIndex] - '0') - (rhs.digits[rhsIndex] - '0') + '0';
      if( returnable.digits[thisIndex] < '0' )
      {
        long t = thisIndex;
        while( returnable.digits[t] < '0' )
        {
          returnable.digits[t] += 10;
          t--;
          returnable.digits[t] -= 1;
        }
      }
      rhsIndex -= 1;
      thisIndex -= 1;
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
  
  
  // rounds down
  bigInt half() const
  {
    bigInt returnable;
    long index = 0;
    long strLen = digits.length();
    long remainder = 0;
    while( index < strLen )
    {
      remainder = remainder + (digits[index] - '0');
      returnable.digits += static_cast<char>((remainder / 2) + static_cast<long>('0'));
      remainder -= (returnable.digits[index] - '0') * 2;
      if( index + 1 < strLen )
        remainder = remainder * 10;
      index++;
    }
    
    while( returnable.digits[0] == '0' )
    {
      returnable.digits.erase(0,1);
    }
    
    return returnable;
  }
  
  
  bool operator>( const bigInt & rhs )
  {
    bigInt rhsCopy = rhs;
    while( digits[0] == '0' )
    {
      digits.erase(0,1);
    }
    while( rhsCopy.digits[0] == '0' )
    {
      rhsCopy.digits.erase(0,1);
    }
    long thisLength = digits.length();
    long rhsLength = rhsCopy.digits.length();
    if( thisLength > rhsLength )
    {
      return true;
    }
    if( thisLength < rhsLength )
    {
      return false;
    }
    // thisLength == rhsLength
    long index = 0;
    while( digits[index] == rhsCopy.digits[index] && index < thisLength )
    {
      index++;
    }
    if( index == thisLength ) // equal
    {
      return false;
    }
    return digits[index] > rhsCopy.digits[index];
  }
  
  bool operator<( const bigInt & rhs )
  {
    bigInt rhsCopy = rhs;
    return rhsCopy > *this;
  }
  
  bool operator==( const bigInt & rhs )
  {
    bigInt rhsCopy = rhs;
    while( digits[0] == '0' )
    {
      digits.erase(digits.begin());
    }
    while( rhsCopy.digits[0] == '0' )
    {
      rhsCopy.digits.erase(rhsCopy.digits.begin());
    }
    long thisLength = digits.length();
    long rhsLength = rhsCopy.digits.length();
    if( thisLength != rhsLength )
    {
      return false;
    }
    // thisLength == rhsLength
    long index = 0;
    while( digits[index] == rhsCopy.digits[index] && index < thisLength )
    {
      index++;
    }
    return index == thisLength;
  }
  
  
  friend ostream & operator<<( ostream & lhs, const bigInt & rhs );
};



bigInt operator+( const long lhs, const bigInt & rhs )
{
  bigInt l ( lhs );
  return l + rhs;
}

bigInt operator-( const long lhs, const bigInt & rhs )
{
  bigInt l ( lhs );
  return l - rhs;
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


const bigInt ONE = 1;

struct lengthAndCount
{
  bigInt length;
  bigInt count;
};

int main()
{
  /* operator- test
  bigInt asdf;
  asdf = factorial(100);
  bigInt zxcv;
  zxcv = asdf - factorial(99);
  cout << zxcv << endl;
  */
  
  /* half() test
  bigInt asdf;
  asdf = factorial(100);
  asdf = asdf.half();
  cout << asdf << endl;
  */
  
  
  long vectorIndex;
  bigInt Count;
  lengthAndCount min;
  lengthAndCount max;
  
  long numCases;
  cin >> numCases;
  for( long i = 0; i < numCases; i++ )
  {
    vector<lengthAndCount> stallSequences;
    
    bigInt N;
    bigInt K;
    cin >> N.digits >> K.digits;
    
    stallSequences.push_back( lengthAndCount() );
    stallSequences[0].length.digits = N.digits;
    stallSequences[0].count = 1;
    while( K > bigInt(0) )
    {
      min.length = stallSequences[0].length - ONE;
      min.length = min.length.half();
      max.length = stallSequences[0].length;
      max.length = max.length.half();
      
      //cout << stallSequences[0].length << " " << max.length << " " << min.length << endl;
      
      if( stallSequences[0].count < K )
        Count = stallSequences[0].count;
      else
        Count = K;
      min.count = Count;
      max.count = Count;
      
      for( long k = 0; k < 2; k++ )
      {
      
        lengthAndCount insertable;
        if( k )
          insertable = max;
        else
          insertable = min;
        vectorIndex = 0;
        while( vectorIndex < stallSequences.size() && insertable.length < stallSequences[vectorIndex].length )
        {
          vectorIndex++;
        }
        if( vectorIndex == stallSequences.size() )
        {
          stallSequences.push_back(insertable);
        }
        else
        {
          if( insertable.length > stallSequences[vectorIndex].length )
          {
            stallSequences.push_back( stallSequences[stallSequences.size() - 1] );
            for( long k = stallSequences.size() - 2; k > vectorIndex; k-- )
            {
              stallSequences[k] = stallSequences[k-1];
            }
            stallSequences[vectorIndex] = insertable;
          }
          else // min.length == stallSequences[vectorIndex].length
          {
            stallSequences[vectorIndex].count = stallSequences[vectorIndex].count + insertable.count;
          }
        }
      }
      
      K = K - Count;
      stallSequences[0].count = stallSequences[0].count - Count;
      if( stallSequences[0].count == bigInt(0) )
        stallSequences.erase( stallSequences.begin() );
      else if( stallSequences[0].count < bigInt(0) )
        cout << "ERROR:stallSequences[0].count==" << stallSequences[0].count << endl;
      
      
    } // end while( K > bigInt(0) )
    
    
    
    cout << "Case #" << (i+1) << ": " << max.length << " " << min.length << endl;
    
    
  }
  
  
  
  return 0;
}
