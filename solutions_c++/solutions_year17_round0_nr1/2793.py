#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

/***********************/
template<typename T>
void outputResult (int inTestCaseNum, T result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
   res << result;
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
   res.open ("/Users/gloria/Downloads/res1.txt");

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      std::string testCase;
      inp >> testCase;

      int k = 0;
      inp >> k;
      int flips = 0;
      
      for (int j = 0; j < testCase.length(); ++j)
      {
         if (testCase[j] == '-')
         {
	    if ((j + k) > testCase.length())
            {
               flips = -1;
               break;
            }
            else
            {
               for (int l = 0; l < k; ++l)
               {
                  testCase[j+l] = testCase[j+l] == '-' ? '+' : '-';
               }
               ++flips;
            }
         }
      }

      if (flips >= 0)
      	outputResult (i, flips, res);
      else
	outputResult (i, "IMPOSSIBLE", res);
   }

   return 0;
}
