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
      
      cout.precision(9);
      
      for(int k0 = 0; k0 < T; k0++)
      {
         cout << "Case #" << k0+1 << ": ";
         
         //Implementation start
         int N;
         int Q;
         file >> N;
         file >> Q;
         
         int E[N];
         int S[N];
         
         //Note index shift by 1 everywhere!!!!!
         
         for(int i = 0; i < N; i++)
         {
            file >> E[i];
            file >> S[i];
         }
         
         int D[N][N];
         double time[N][N];
         
         for(int i = 0; i < N; i++)
         {
            for(int j = 0; j < N; j++)
            {
               file >> D[i][j];
               time[i][j] = -1.0;
               /*if(D[i][j] > 0 && D[i][j] >= E[i])
               {
                  time[i][j] = ((double) D[i][j])/S[i];
               }*/
            }
         }
         
         //compute all pairs shortest paths:
         for(int k = 0; k < N; k++)
         {
            for(int i = 0; i < N; i++)
            {
               if(i == k)
               {
                  continue;
               }
               for(int j = 0; j < N; j++)
               {
                  if(j != k && i != j && D[i][k] > 0 && D[k][j] > 0)
                  {
                     if(D[i][j] > D[i][k] + D[k][j] || D[i][j] < 0)
                     {
                        D[i][j] = D[i][k] + D[k][j];
                     }
                  }
               }
            }
         }
         
         for(int i = 0; i < N; i++)
         {
            for(int j = 0; j < N; j++)
            {
               if(D[i][j] > 0 && D[i][j] <= E[i])
               {
                  time[i][j] = ((double) D[i][j])/S[i];
               }
            }
         }
         
         for(int k = 0; k < N; k++)
         {
            //allow to switch to horses 0 to k in between
            for(int i = 0; i < N; i++)
            {
               if(i == k)
               {
                  continue;
               }
               
               for(int j = 0; j < N; j++)
               {
                  if(j != k && j != i && time[i][k] > 0 && time[k][j] > 0)
                  {
                     if(time[i][k] + time[k][j] < time[i][j] || time[i][j] < 0)
                     {
                        time[i][j] = time[i][k] + time[k][j];
                     }
                  }
               }
            }
         }
         
         for(int i = 0; i < Q; i++)
         {
            int U;
            int V;
            file >> U;
            file >> V;
            if(time[U-1][V-1] < 0)
            {
               cout << "ups "; //should not happen if input is correct!!!
            }
            cout << time[U-1][V-1];
            if(i < Q-1)
            {
               cout << " ";
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
