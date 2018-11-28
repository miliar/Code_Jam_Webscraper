#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

struct Pair
{
    int index;
    double p;

    Pair(double p0, int i) : p(p0), index(i) {}
    Pair() : p(0.0), index(-1) {}

    bool operator < (const Pair& pair) const
    {
        return (p < pair.p);
    }
};

/*bool compRRH (const Pair& p1, const Pair& p2)
{
   return ( ((long long) p1.r)*(p1.r+2*p1.h) > ((long long) p2.r)*(p2.r+2*p2.h));
}*/

/*bool compRH (const Pair& p1, const Pair& p2)
{
   return ( ((long long) p1.h)*p1.r > ((long long) p2.h)*p2.r );
}*/

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
         
         double U;
         file >> U;
         
         Pair mP[N];
         for(int i = 0; i < N; i++)
         {
            double p;
            file >> p;
            mP[i] = Pair(p, i);
         }
         
         sort(mP, mP+N);
         
         int currMinNum = 1;
         double currMin = mP[0].p;
         for(int i = 1; i <= N; i++)
         {
            if(i < N && U + i*mP[0].p >= i*mP[i].p)
            {
               U += i*mP[0].p - i*mP[i].p;
               for(int j = 0; j < i; j++)
               {
                  mP[j].p = mP[i].p;
               }
            }
            else
            {
               for(int j = 0; j < i; j++)
               {
                  mP[j].p += U/i;
               }
               break;
            }
         }
         
         /*cout << "Q: ";
         for(int i = 0; i < N; i++)
         {
            cout << mP[i].p << " ";
         }
         cout << endl;*/
         
         
         double prob = 1.0;
         
         for(int i = 0; i < N; i++)
         {
            prob *= mP[i].p;
         }
         printf("%.9f", prob);
         
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
