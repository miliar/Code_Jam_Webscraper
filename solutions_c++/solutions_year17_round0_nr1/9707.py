#include <iostream>
#include <string>

using namespace std;

int main()
{

int cases;
cin>>cases;

bool valid;
string S;
int flipperSize, flippVal, cakeVal, cakeSize, steps;

for( int i=1; i<=cases; i++ )
{
  cakeSize = 0;  cakeVal = 0; flippVal = 0; steps = 0;
  valid = true;
  cin>> S;
  for( int j=0; j<S.size(); j++)
  {
    cakeVal = cakeVal<<1; 
    cakeVal+= (S.at(j)=='+')?1:0; 
  }
    cakeSize = S.size(); 

  cin>> flipperSize;

  for( int j=0; j<flipperSize; j++)
  {
    flippVal = flippVal<<1; 
    flippVal++;
  }

  for( int j=0; j<cakeSize-flipperSize+1; j++)
  {
    if( !((1<<j) & cakeVal) )
    {
      cakeVal = cakeVal ^ (flippVal<<j); 
      steps+=1; 
    }
  }

  for( int j=0; j<cakeSize; j++)
    if( (cakeVal>>j)%2 == 0 )
      valid = false;

  if( valid )
    cout<< "Case #"<< i<< ": "<< steps<< endl;
  else
    cout<< "Case #"<< i<< ": "<< "IMPOSSIBLE"<< endl;
}

return 0;
}
