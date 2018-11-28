#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>
#include <unordered_map>

using namespace std;

/***********************/
void outputResult (long long int inTestCaseNum, vector<long long int>& result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
   for (int i = 0; i < result.size(); ++i)
   {
      res << result[i] << " ";
   }
   res << endl;
}

bool myfunction (long long int i, long long int j) { return (i>j); }

/***********************/
int main()
{
   long long int n = 0;

    ifstream inp;
   inp.open ("/Users/gloria/Downloads/C-large.in");
//   inp.open ("/Users/gloria/Downloads/C-small-2-attempt1.in");
   ofstream res;
   res.open ("/Users/gloria/Downloads/res1.txt");

   inp >> n;

   for (long long int i = 0; i < n; ++i)
   {
      long long int n, k;
      inp >> n >> k;

      std::unordered_map<long long int, long long int> inter, inter2;
      std::unordered_map<long long int, long long int>* cur = &inter, * old = &inter2;
      (*old)[n] = 1;
      long long int p = 1;
      long long int visitors = 0;
//      cout << endl;
      while ((visitors + p) < k )
      {
         for (std::unordered_map<long long int, long long int>::iterator it = old->begin(); it != old->end(); ++it)
         {
            long long int a = it->first / 2;
            long long int b = it->first - a - 1;
           // cout << a << " " << b << " ";
            if (a == b)
            {
               if (!cur->count(a))
               	  (*cur)[a] = 0;
               (*cur)[a] += it->second*2;
            }
            else
            {
               if (!cur->count(a))
               	  (*cur)[a] = 0;
               if (!cur->count(b))
               	  (*cur)[b] = 0;
               (*cur)[a] += it->second;
               (*cur)[b] += it->second;
            }
         //   cout << a << " " << (*cur)[a] << " " << b << " "<< (*cur)[b] << endl;
         }

//         for (std::unordered_map<int,int>::iterator it = cur->begin(); it != cur->end(); ++it)
//         {
//            cout << "(" << it->first << " " << it->second << ") ";
//         }

         old->clear();
         std::unordered_map<long long int, long long int> *temp = old;
         old = cur;
         cur = temp;
//	 cout << endl;
         visitors += p;
         p *= 2;
      }

      std::vector< long long int> interV;
      for (std::unordered_map< long long int, long long int>::iterator it = old->begin(); it != old->end(); ++it)
      {
         interV.push_back(it->first);
        // cout << "(" << it->first << " " << it->second << ") ";
      }
  //    cout << endl;
      std::sort(interV.begin(), interV.end(), myfunction);

      long long int count = 0;
      long long int goal = k - visitors - 1;
    //  cout << visitors << " " << goal << endl;
      long long int j = 0;
      while (count < goal)
      {
         count += (*old)[interV[j++]];
      }
      if (j && (count > goal)) --j;

     // cout << interV[j] << endl;
      long long int distMin = interV[j] / 2;
      long long int distMax = interV[j] - distMin - 1;
//      cout << inter[k-visitors-1] << endl;
      if (distMax < distMin)
      {
         long long int temp = distMax;
         distMax = distMin;
         distMin = temp;
      }

      vector<long long int> result;
      result.push_back(distMax);
      result.push_back(distMin);
//      cout << endl;
      outputResult (i, result, res);
//      cout << endl;
   }

   return 0;
}
