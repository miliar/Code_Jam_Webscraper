#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

/***********************/
void outputResult (int inTestCaseNum, std::string& result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
   int i = 0;
   while ((i < result.length()) && (result[i] == '0')) ++i;

   if (i == result.length())
      res << "0";
   else
 	  for (; i < result.length(); ++i)
   		res << result[i];

   res << endl;
}
/***********************/
int main()
{
   int n = 0;

    ifstream inp;
   inp.open ("/Users/gloria/Downloads/B-large.in");
//   inp.open ("/Users/gloria/Downloads/B-small-attempt1.in");
   ofstream res;
   res.open ("/Users/gloria/Downloads/res1.txt");

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      std::string testCase;
      inp >> testCase;

//      cout << testCase <<endl;
      for (int i = testCase.length()-2; i >= 0;  --i)
      {
         if (testCase[i] > testCase[i+1])
         {
            testCase[i] -= 1;
            for (int j = i+1; j < testCase.length(); ++j)
               testCase[j] = '9';
            if (testCase[i] < '0')
               testCase[i] = '9';
         }
  //       cout << testCase <<endl;
      }
      outputResult (i, testCase, res);
    //  cout << endl;
   }

   return 0;
}
