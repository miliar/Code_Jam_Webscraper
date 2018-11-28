#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <vector>
#include <stdlib.h>

void flipCakes(int pos, int flipper, std::string* stateBefore)
{
   if ( (pos < 0) || ((pos + flipper) > stateBefore->length()) )
   {
      std::cerr << "Illegal cake flipping!" << std::endl;
      exit(1);
   }

   for (int i = 0; i < flipper; i++)
   {
      if ((*stateBefore)[pos] == '-')
      {
         (*stateBefore)[pos] = '+';
      }
      else
      {
         (*stateBefore)[pos] = '-';
      }

      pos++;
   }
}

std::string happyDay(int numCakes)
{
   std::string retVal;
   for(int i = 0; i < numCakes; i++)
   {
      retVal += '+';
   }

   return retVal;
}

std::string solveCase()
{
   std::string pancakeStates;
   std::cin >> pancakeStates;

   int flipperSize;
   std::cin >> flipperSize;

   std::cerr << "State=" << pancakeStates << " and size=" << flipperSize << std::endl;

   int numFlips = 0;
   for(int i = 0; i <= pancakeStates.length() - flipperSize; i++)
   {
      if (pancakeStates[i] == '-')
      {
         // Need to flip!
         flipCakes(i, flipperSize, &pancakeStates);
         numFlips++;
      }
   }

   if (pancakeStates == happyDay(pancakeStates.length()))
   {
      std::ostringstream oss;
      oss << numFlips;
      return oss.str();
   }
   else
   {
      return "IMPOSSIBLE";
   }


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
