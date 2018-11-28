#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

long long notTidy(long long n)
{
  long long current, next;
  bool tidy = 0;

  current = n%10;
  if( current == n )
    return -1;

  for( int i=2; i<= ceil( log10(n+1) ); i++ )
  {
    long long adjust = pow(10,i);
    next = n % adjust - n % (adjust/10);
    next /= adjust/10;

    if( next > current )
      return i-1;
    
    current = next;
  }
  return -1;
}

int main()
{

long long num;
int cases, badIndex;

cin>>cases;

for( int i=1; i<=cases; i++)
{
  cin>>num;
  badIndex = notTidy(num);

  while( badIndex != -1 )
  {
    long long adjust = pow( 10, badIndex );
    num -= num % adjust;
    num -= 1;

    badIndex = notTidy(num);
  }

  cout<< "Case #"<< i<< ": "<< num<< endl; 
}

return 0;
}
