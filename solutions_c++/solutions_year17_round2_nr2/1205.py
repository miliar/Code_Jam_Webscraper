#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char *argv[])
{
  //input filename as parameter or via stdin
   char* filename;
   if(argc > 1)
   {
      filename = argv[1];
   }
   else
   {
      char buffer[256];
      cout << "Input file name (up to 255 Characters): " << endl;
      cin >> buffer;
      filename = buffer;
   }
   
   int T = 0;
   
   try
   {    
      ifstream file(filename);
      if(!file.is_open())
         throw 1;
      
      if(!file.good())
         throw 2;
      file >> T;
      if(T <= 0)
         throw 3;
      
      cout.precision(9);
      
      for(int k0 = 0; k0 < T; k0++)
      {
         cout << "Case #" << k0+1 << ": ";
         
         //Implementation start
         int N;
         file >> N;
         
         int R;
         file >> R;
         
         int O;
         file >> O;
         
         int Y;
         file >> Y;
         
         int G;
         file >> G;
         
         int B;
         file >> B;
         
         int V;
         file >> V;
         
         //for SMALL:
         
         int max = 0;
         int min = N+1;
         int other = -1;
         char maxLetter = '?';
         char minLetter = '?';
         char otherLetter = '?';
         
         if(Y > R)
         {
            max = Y;
            min = R;
            maxLetter = 'Y';
            minLetter = 'R';
         }
         else
         {
            max = R;
            min = Y;
            maxLetter = 'R';
            minLetter = 'Y';
         }
         
         if(B > max)
         {
            other = max;
            otherLetter = maxLetter;
            max = B;
            maxLetter = 'B';
         }
         else
         {
            if(B < min)
            {
               other = min;
               otherLetter = minLetter;
               min = B;
               minLetter = 'B';
            }
            else
            {
               other = B;
               otherLetter = 'B';
            }
         }
         
         if(max > other + min)
         {
            cout << "IMPOSSIBLE";
         }
         else
         {
            int both = other + min - max;
            int single = other - both;
            int last = max - other;
            for(int i = 0; i < both; i++)
            {
               cout << maxLetter << otherLetter << minLetter;
            }
            for(int i = 0; i < single; i++)
            {
               cout << maxLetter << otherLetter;
            }
            for(int i = 0; i < last; i++)
            {
               cout << maxLetter << minLetter;
            }
         }
         
         
         //Implementation end
         cout << endl;
      }
   }
   catch(int e)
   {
      cout << "Error (no. " << e << ") when reading file.";
      int a;
      cin >> a;
      return 1;
   }
    
    return 0;    
}
