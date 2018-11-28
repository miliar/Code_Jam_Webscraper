// Programmer: Tanner Winkelman
// 4/22/2017
// Purpose: Google Code Jam Round 1B 2017 Problem A

#include <iostream>
using namespace std;



int main()
{
  
  
  long T;
  
  cin >> T;
  
  for( long t = 1; t <= T; t++ )
  {
    char * circle;
    long N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    long sum = R+O+Y+G+B+V;
    circle = new char[N+1];
    for( long k = 0; k < N; k++ )
      circle[k] = '.';
    circle[N] = '\0';
    
    short R_first = 0;
    short Y_first = 0;
    short B_first = 0;
    
    bool possible = true;
    //bool firstSwapped = false;
    
    while( sum > 0 && possible )
    {
      possible = false;
      if( !possible && R >= 1 && R + R_first >= Y + Y_first && R + R_first >= B + B_first )
      {
        long position = 0;
        bool ok = false;
        do
        {
          position = (position + 1) % N;
          if( circle[position] == '.' && circle[((position-1) + N) % N] != 'R' && circle[(position+1) % N] != 'R' )
            ok = true;
        }
        while( !ok && position != 0 );
        
        if( ok )
        {
          circle[position] = 'R';
          possible = true;
          sum--;
          R--;
          if( !R_first && !B_first && !Y_first )
            R_first = 1;
        }
      }
      
      if( !possible && Y >= 1 && Y + Y_first >= R + R_first && Y + Y_first >= B + B_first )
      {
        long position = 0;
        bool ok = false;
        do
        {
          position = (position + 1) % N;
          if( circle[position] == '.' && circle[((position-1) + N) % N] != 'Y' && circle[(position+1) % N] != 'Y' )
            ok = true;
        }
        while( !ok && position != 0 );
        
        if( ok )
        {
          circle[position] = 'Y';
          possible = true;
          sum--;
          Y--;
          if( !R_first && !B_first && !Y_first )
            Y_first = 1;
        }
      }
      
      if( !possible && B >= 1 && B + B_first >= R + R_first && B + B_first >= Y + Y_first )
      {
        long position = 0;
        bool ok = false;
        do
        {
          position = (position + 1) % N;
          if( circle[position] == '.' && circle[((position-1) + N) % N] != 'B' && circle[(position+1) % N] != 'B' )
            ok = true;
        }
        while( !ok && position != 0 );
        
        if( ok )
        {
          circle[position] = 'B';
          possible = true;
          sum--;
          B--;
          if( !R_first && !B_first && !Y_first )
            B_first = 1;
        }
      }
      
      
      /*
      if( !possible && !firstSwapped )
      {
        if( circle[2] != 'R' && circle[0] != 'R' && circle[1] != 'R' )
        {
          cout << "RED_FIRST_SWAPPED " << flush;
          switch( circle[1] )
          {
            case 'Y':
              Y++;
              break;
            case 'B':
              B++;
              break;
          }
          circle[1] = 'R';
          R--;
          possible = true;
          firstSwapped = true;
        }
        else if( circle[2] != 'Y' && circle[0] != 'Y' && circle[1] != 'Y' )
        {
          cout << "YELLOW_FIRST_SWAPPED " << flush;
          switch( circle[1] )
          {
            case 'R':
              R++;
              break;
            case 'B':
              B++;
              break;
          }
          circle[1] = 'Y';
          Y--;
          possible = true;
          firstSwapped = true;
        }
        else if( circle[2] != 'B' && circle[0] != 'B' && circle[1] != 'B' )
        {
          cout << "BLUE_FIRST_SWAPPED " << flush;
          switch( circle[1] )
          {
            case 'R':
              R++;
              break;
            case 'Y':
              Y++;
              break;
          }
          circle[1] = 'B';
          B--;
          possible = true;
          firstSwapped = true;
        }
      }*/
      
    }
    
    //cout << "SUM:" << sum << " " << flush;
    
    if( sum == 0 )
    {
      cout << "Case #" << t << ": " << circle << endl;
    }
    else
    {
      cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
    
    delete [] circle;
    circle = NULL;
  }
  
  
  return 0;
}
