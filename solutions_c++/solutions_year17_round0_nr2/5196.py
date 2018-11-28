#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <vector>

std::string removeLeadingZeros(std::string val)
{
   std::string retVal;
   for(auto it = val.begin(); it != val.end(); it++)
   {
      if (*it != '0')
      {
         retVal += *it;
      }
   }

   return retVal;
}

std::string subtractAtPos(std::string origVal, int pos)
{
   if (origVal[pos] == '0')
   {
      // Subtract 1 from previous digit, and then convert everything after to 9's
      origVal = subtractAtPos(origVal, pos - 1);

   }
   else
   {
      // Subtract 1 from this digit since it is 1 or greater, then convert everything after to 9's
      origVal[pos] = origVal[pos] - 1;
   }

   int i = pos + 1;
   while(i < origVal.length())
   {
      origVal[i++] = '9';
   }

   return origVal;
}


bool isTidy(std::string val)
{
   char largestSoFar = '9';

   for(auto curLetter = val.rbegin(); curLetter != val.rend(); curLetter++)
   {
      if (*curLetter > largestSoFar)
      {
         return false;
      }

      largestSoFar = *curLetter;
   }

   return true;
}

int positionNotTidy(std::string val)
{
   char smallestSoFar = '0';

   for(int i = 0; i < val.length(); i++)
   {
      if (val[i] >= smallestSoFar)
      {
         smallestSoFar = val[i];
      }
      else
      {
         return i;
      }
   }

   return -1;
}

std::string solveCase()
{
   std::string largeNumber;
   std::cin >> largeNumber;

   //std::cerr << largeNumber << " is " << (isTidy(largeNumber) ? "tidy" : "NOT tidy") << " at " << positionNotTidy(largeNumber) << std::endl;

   while (!isTidy(largeNumber))
   {
      largeNumber = subtractAtPos(largeNumber, positionNotTidy(largeNumber) - 1);
   }

   return removeLeadingZeros(largeNumber);
}

int main(int, char**)
{
   int numCases = 0;
   std::cin >> numCases;

   for(int i = 0; i < numCases; i++)
   {
      std::cout << "Case #" << i+1 << ": " << solveCase() << std::endl;
   }

   return 0;
}
