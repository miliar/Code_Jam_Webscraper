#include <iostream>
#include <fstream>
#include <string>

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
      
      
      for(int k0 = 0; k0 < T; k0++)
      {
         cout << "Case #" << k0+1 << ": ";
         
         //Implementation start
         string S;
         file >> S;
         
         int n = S.length();
         
         int equalSince = 0;
         bool onlyNine = false;
         
         for(int i = 1; i < n; i++)
         {
            if(onlyNine)
            {
               S[i] = '9';
               continue;
            }
            
            if(S[i] > S[i-1])
            {
               equalSince = i;
            }
            else if(S[i] < S[i-1])
            {
               S[equalSince] = (char) ((int) S[equalSince] - 1);
               onlyNine = true;
               i = equalSince;
            }
         }
         
         if(S[0] == '0')
         {
           S = S.substr(1,n-1);
         }
         
         cout << S;
         
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
