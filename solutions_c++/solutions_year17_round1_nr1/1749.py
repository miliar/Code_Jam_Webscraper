#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

/***********************/
void outputResult (int inTestCaseNum, std::vector<std::string>& result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": " << endl;
   for (int i = 0; i < result.size(); ++i)
   {
      res << result[i] << endl;
   }
   res << endl;
}
/***********************/
int main()
{
   int n = 0;

    ifstream inp;
   inp.open ("/Users/gloria/Downloads/A-large.in");
//   inp.open ("/Users/gloria/Downloads/A-small-attempt0.in");
   ofstream res;
   res.open ("res1.txt");

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      int a, b;
      inp >> a >> b;
      std::vector<std::string> grid;
      for (int j = 0; j < a; ++j)
      {
         std::string s;
         inp >> s;
         grid.push_back(s);
      }

      std::vector<int> blank(a,1);
      for (int j = 0; j < a; ++j)
      {
         int last = -1;
         int k = 0;
         while (k < b)
         {
            while ((k < b) && (grid[j][k] == '?'))
               ++k;

            if (k < b)
            {
               int m = k-1;
               while ((m >=0) && (grid[j][m] == '?'))
               {
                  grid[j][m] = grid[j][k];
                  --m;
               }
               last = k;
            }
            ++k;
         }
         if (last >= 0)
         {
            int m = b-1;
            while((m > last) && (grid[j][m] == '?'))
            {
               grid[j][m] = grid[j][last];
               --m;
            }
         }
         if (last < 0)
            blank[j] = 0;
      }
     
      int last = -1;
      int j = 0;
      while (j < a)
      {
         while ((j < a) && (blank[j] == 0))
            ++j;
         
         if (j < a)
         {
            int m = j-1;
            while ((m >= 0) && (blank[m] == 0))
            {
               grid[m] = grid[j];
               --m;
            }
            last = j;
         }
         else if (last >=0)
         {
            int m = a-1;
            while ((m > last) && (blank[m] == 0))
            {
               grid[m] = grid[last];
               --m;
            }
         }
         ++j;
      }
      outputResult (i, grid, res);
   }

   return 0;
}
