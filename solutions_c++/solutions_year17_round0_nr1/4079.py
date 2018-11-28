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
         
         int k;
         file >> k;
         
         int n = S.length();
         
         bool T[n+1];
         T[0] = (S[0] == '+');
         for(int i = 1; i < n; i++)
         {
           T[i] = (S[i] == S[i-1]);
         }
         T[n] = (S[n-1] == '+');
         

         
         
         int count = 0;
         
         for(int i = 0; i < n-k+1; i++)
         {
            if(!T[i])
            {
               //T[i] = !(T[i]);
               T[i+k] = !(T[i+k]);
               count++;
            }
         }
         
         for(int i = n-k+1; i < n+1; i++)
         {
            if(!T[i])
            {
               count = -1;
               break;
            }
         }
         if(count >= 0)
         {
            cout << count;
         }
         else
         {
            cout << "IMPOSSIBLE";
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
