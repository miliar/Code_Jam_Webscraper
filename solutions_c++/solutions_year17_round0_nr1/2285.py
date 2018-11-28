// Programmer: Tanner Winkelman
// 4/7/2017
// Purpose: Solve pancake problem:
//   Google Code Jam Qualification Round 2017 Problem A


#include <iostream>
using namespace std;


void flipOne( char & pancake, long & numMinuses )
{
  if( pancake == '+' )
  {
    pancake = '-';
    numMinuses++;
  }
  else
  {
    pancake = '+';
    numMinuses--;
  }
  return;
}

void flip( string & pancakes, const long flipWidth, const long leftMostPancake, long & numMinuses )
{
  for( long k = 0; k<flipWidth; k++ )
    flipOne( pancakes[leftMostPancake + k], numMinuses );
  
  return;
}


int main()
{
  
  long num_cases;
  cin >> num_cases;
  
  string pancakes;
  long flipWidth;
  long highestMinus;
  long numMinuses;
  long flipCount;
  bool consecutive;
  
  for( long k = 0; k < num_cases; k++ )
  {
    pancakes = "";
    numMinuses = 0;
    flipCount = 0;
    //consecutive = true;
    cin >> pancakes >> flipWidth;
    highestMinus = pancakes.length() - 1;
    while( highestMinus >= 0 && pancakes[highestMinus] != '-' )
    {
      highestMinus--;
    }
    
    for( long k = 0; k <= highestMinus; k++ )
    {
      //if( numMinuses > 0 && pancakes[k] == '-' && pancakes[k-1] == '+' )
      //  consecutive = false;
      if( pancakes[k] == '-' )
        numMinuses++;
    }
    
    while( highestMinus >= flipWidth - 1  )
    {
      flip( pancakes, flipWidth, highestMinus - flipWidth + 1, numMinuses );
      flipCount++;
      while( highestMinus >= 0 && pancakes[highestMinus] != '-' )
      {
        highestMinus--;
      }
    }
    
    if( numMinuses == 0 )
      cout << "Case #" << (k+1) << ": " << flipCount << endl;
    else if( numMinuses > 0 )
      cout << "Case #" << (k+1) << ": IMPOSSIBLE" << endl;
    else
      cout << "ERROR:numMinuses==" << numMinuses << endl;
    
    
  }
  
  
  
  return 0;
}
