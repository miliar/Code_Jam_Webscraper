#include <iostream>
#include <assert.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
bool isTidyNumber(unsigned long long n);
int main()
{
   ofstream outFile("outputSmall.out");
   ifstream inFile("inputSmall.in");
   assert(outFile.is_open());
   assert(inFile.is_open());

   int T = 0;
   inFile >> T;

   for (int TestCase = 1; TestCase <= T; TestCase++)
   {
      unsigned long long n = 0;
      inFile >> n;
      if (n < 10)
      {
         outFile << "Case #" << TestCase << ": " << n << "\n";
      }
      else
      {
         while (!isTidyNumber(n))
         {
            n--;
         }
         outFile << "Case #" << TestCase << ": "<< n << "\n";
      }
   }

   inFile.close();
   outFile.close();
   //    system("pause");

   return 1;
}
bool isTidyNumber(unsigned long long n)
{
   if (n < 10)
      return true;
   do
   {
      int r1 = n % 10;
      n = n / 10;
      int r2 = n % 10;

      if (r2 > r1)
         return false;
   } while (n > 0);
   
   return true;
}