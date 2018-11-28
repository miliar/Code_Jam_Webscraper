#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

class Pair
{
   public:
      int width;
      int mult;
      
      Pair(int x, int y)
      {
         width = x;
         mult = y;
      };
};

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
         int N, K;
         file >> N;
         file >> K;
         
         //int n = N+1;
         
         list<Pair> myList;
         myList.push_front(Pair(N, 1));
         
         while(true)
         {
            int n = myList.front().width;
            int k = myList.front().mult;
            myList.pop_front();
            if(K > k)
            {
               K -= k;
               int m = (n-1)-((n-1)/2);
               if(myList.back().width == m)
               {
                  myList.back().mult += k;
               }
               else
               {
                  myList.push_back(Pair(m,k));
               }
               
               m = (n-1)/2;
               if(myList.back().width == m)
               {
                  myList.back().mult += k;
               }
               else
               {
                  myList.push_back(Pair(m,k));
               }
            }
            else
            {
               cout << (n-1)-((n-1)/2) << " " << (n-1)/2;
               break;
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
