#include <iostream>
#include <vector>
using namespace std;


const long DIRECTIONS[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

bool validCoords( const long row, const long col, const long R, const long C )
{
  return (row >= 0) && (row < R) && (col >= 0) && (col < C);
}

struct Slice
{
  char letter;
  long r;
  long c;
  long left;
  long right;
  long up;
  long down;
};


int main()
{
  long T;
  cin >> T;
  
  long R;
  long C;
  
  
  
  
  for( long a = 0; a < T; a++ )
  {
    cin >> R >> C;
    vector<string> lines (R,"");
    vector<Slice> slices;
    for( long k = 0; k < R; k++ )
    {
      cin >> lines[k];
    }
    
    for( long row = 0; row < R; row++ )
    {
      for( long col = 0; col < C; col++ )
      {
        if( lines[row][col] != '?' )
        {
          slices.push_back( Slice() );
          slices[slices.size() - 1].letter = lines[row][col];
          slices[slices.size() - 1].r = row;
          slices[slices.size() - 1].c = col;
          slices[slices.size() - 1].left = 0;
          slices[slices.size() - 1].right = 0;
          slices[slices.size() - 1].up = 0;
          slices[slices.size() - 1].down = 0;
        }
      }
    }
    
    long numSlices = slices.size();

    bool done = false;
    
    while( !done )
    {
      done = true;
      for( long sliceIndex = 0; sliceIndex < numSlices; sliceIndex++ )
      {
        bool clear = true;
        long k;
        k = 0;
        clear = true;
        while( clear && ( k < slices[sliceIndex].right + slices[sliceIndex].left + 1 ) )
        {
          if( 
            !validCoords(
              slices[sliceIndex].r - slices[sliceIndex].up - 1,
              slices[sliceIndex].c - slices[sliceIndex].left + k,
              R, C )
          )
            clear = false;
          if(
            clear
            &&
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up - 1]
            [slices[sliceIndex].c - slices[sliceIndex].left + k]
            != '?')
            clear = false;
          k++;
        }
        if( clear )
        {
          done = false;
          slices[sliceIndex].up += 1;
          for( k = 0; k < slices[sliceIndex].right + slices[sliceIndex].left + 1; k++ )
          {
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up]
            [slices[sliceIndex].c - slices[sliceIndex].left + k]
            = slices[sliceIndex].letter;
          }
        }
        k = 0;
        clear = true;
        while( clear && ( k < slices[sliceIndex].right + slices[sliceIndex].left + 1 ) )
        {
          if(
            !validCoords(
              slices[sliceIndex].r + slices[sliceIndex].down + 1,
              slices[sliceIndex].c - slices[sliceIndex].left + k,
              R, C )
          )
            clear = false;
          if(
            clear
            &&
            lines
            [slices[sliceIndex].r + slices[sliceIndex].down + 1]
            [slices[sliceIndex].c - slices[sliceIndex].left + k]
            != '?')
            clear = false;
          k++;
        }
        if( clear )
        {
          done = false;
          slices[sliceIndex].down += 1;
          for( k = 0; k < slices[sliceIndex].right + slices[sliceIndex].left + 1; k++ )
          {
            lines
            [slices[sliceIndex].r + slices[sliceIndex].down]
            [slices[sliceIndex].c - slices[sliceIndex].left + k]
            = slices[sliceIndex].letter;
          }
        }
        k = 0;
        clear = true;
        while( clear && ( k < slices[sliceIndex].up + slices[sliceIndex].down + 1 ) )
        {
          if(
            !validCoords(
              slices[sliceIndex].r - slices[sliceIndex].up + k,
              slices[sliceIndex].c - slices[sliceIndex].left - 1,
              R, C )
          )
            clear = false;
          if(
            clear
            &&
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up + k]
            [slices[sliceIndex].c - slices[sliceIndex].left - 1]
            != '?')
            clear = false;
          k++;
        }
        if( clear )
        {
          done = false;
          slices[sliceIndex].left += 1;
          for( k = 0; k < slices[sliceIndex].up + slices[sliceIndex].down + 1; k++ )
          {
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up + k]
            [slices[sliceIndex].c - slices[sliceIndex].left]
            = slices[sliceIndex].letter;
          }
        }
        k = 0;
        clear = true;
        while( clear && ( k < slices[sliceIndex].up + slices[sliceIndex].down + 1 ) )
        {
          if(
            !validCoords(
              slices[sliceIndex].r - slices[sliceIndex].up + k,
              slices[sliceIndex].c + slices[sliceIndex].right + 1,
              R, C )
          )
            clear = false;
          if(
            clear
            &&
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up + k]
            [slices[sliceIndex].c + slices[sliceIndex].right + 1]
            != '?')
            clear = false;
          k++;
        }
        if( clear )
        {
          done = false;
          slices[sliceIndex].right += 1;
          for( k = 0; k < slices[sliceIndex].up + slices[sliceIndex].down + 1; k++ )
          {
            lines
            [slices[sliceIndex].r - slices[sliceIndex].up + k]
            [slices[sliceIndex].c + slices[sliceIndex].right]
            = slices[sliceIndex].letter;
          }
        }
        
      }  // end for each slice
      
    }  // end while( !done )
    
    cout << "Case #" << (a+1) << ":" << endl;
    for( long j = 0; j < lines.size(); j++ )
    {
      cout << lines[j] << endl;
    }
    
    /*
    for( long row = 0; row < R; row++ )
    {
      for( long col = 0; col < C; col++ )
      {
        if( lines[row][col] != '?' )
        {
          for( short dir = 0; dir < 4; dir++ )
          {
            if(
              validCoords(
                row + DIRECTIONS[dir][0],
                col + DIRECTIONS[dir][1],
                R, C )
            )
            {
              
            }
          }
        }
      }
    }
    */
    
  }
  
  
  return 0;
}
