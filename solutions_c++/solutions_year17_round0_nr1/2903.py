#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>

using namespace std;

bool isInside(string str, char c)
{
    return str.find(c) != string::npos;
}

string flip(string pancakes, int pos, int size)
{
  cout << "flipping " << pos << endl; 
  for(int i = 0; i < size; i++)
  {
    if(pancakes[pos + i] == '+')
      pancakes[pos + i] = '-';
    else
      pancakes[pos + i] = '+';
  }

  cout << pancakes << endl;
  return pancakes;
}
//
// main function
//
int main()
{
  int Tests, count = 0; // Counting which test case
  string pancakes = "";
  cin >> Tests; // Taking input
  
  ofstream output;
  output.open("bigPancakesOutput.txt");

  while(Tests != 0)
    {
      int solution = 0, turn = 0, size = 0, check = 0;
      count++;
      cin >> pancakes >> size;

      int leftPos = 0, rightPos = pancakes.length();

      while(isInside(pancakes, '-')) // till there is - in the string
      {
        if(leftPos + size > pancakes.size())
        {
          output << "Case #" << count << ": IMPOSSIBLE" << endl;
          check = 1;
          break;
        }

        while(pancakes[leftPos] != '-') // finding '-' or end the program
        {
          if(leftPos + size > pancakes.length()) // if nothing end it
            break;
          leftPos++;
        }


        if(leftPos + size <=  pancakes.length())
        {
          pancakes = flip(pancakes, leftPos, size); //  flipping the appropriate
          solution++;
        }

      }

      if(check == 0)
        output << "Case #" << count << ": " << solution << endl;
      Tests--;
    }

    return 0;
}