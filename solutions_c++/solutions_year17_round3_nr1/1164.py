#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

struct Pair
{
    int index;
    int r;
    int h;

    Pair(int r0, int h0, int i) : r(r0), h(h0), index(i) {}
    Pair() : r(0), h(0), index(-1) {}

    /*bool operator < (const Pair& pair) const
    {
        return (r < pair.r);
    }*/
};

/*bool compRRH (const Pair& p1, const Pair& p2)
{
   return ( ((long long) p1.r)*(p1.r+2*p1.h) > ((long long) p2.r)*(p2.r+2*p2.h));
}*/

bool compRH (const Pair& p1, const Pair& p2)
{
   return ( ((long long) p1.h)*p1.r > ((long long) p2.h)*p2.r );
}

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
         int N;
         file >> N;
         
         int K;
         file >> K;
         
         Pair pancake[N];
         
         for(int i = 0; i < N; i++)
         {
            int R;
            file >> R;
            int H;
            file >> H;
            pancake[i] = Pair(R, H, i);
         }
         
         sort(pancake, pancake+N, compRH);
         
         long long sum = 0;
         
         int maxR = 0;         
         long long maxArea = 0;
         
         for(int i = 0; i < N; i++)
         {
            if(i < K-1)
            {
               sum += 2*((long long) pancake[i].r) * pancake[i].h;
               if(pancake[i].r > maxR)
               {
                  sum -= ((long long) maxR)*maxR;
                  maxR = pancake[i].r;
                  sum += ((long long) maxR)*maxR;
               }
            }
            else
            {
               long long area = sum + 2*((long long) pancake[i].r) * pancake[i].h;
               if(pancake[i].r > maxR)
               {
                  area +=  ((long long) pancake[i].r)*pancake[i].r - ((long long) maxR)*maxR;
               }
               if(area > maxArea)
               {
                  maxArea = area;
               }
            }
         }
         
         double output = (3.1415926535897932384626433832795) * maxArea;
         printf("%.9f", output);
         
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
