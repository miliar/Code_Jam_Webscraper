//Joey Klix
//Google Code Jam 2017
//A. Oversized Pancake Flipper

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  //vars
  const string sfileinput = "A-large.in";
  const string sfileoutput = "output.txt";
  ifstream in;
  ofstream out;
  int iCases = 0;
  string sInput = "";
  int iFlipperWidth = 0;
  int iFlipCount = 0;
  bool bPossible = true;

  //open files and read in number of cases
  in.open(sfileinput.c_str());
  out.open(sfileoutput.c_str());
  in >> iCases;

  //loop for each case
  for (int i = 0; i < iCases; i++)
  {
    //input string and flipperwidth
    in >> sInput >> iFlipperWidth;

    //loop through each pancake
    for (unsigned int j = 0; j < sInput.length() - iFlipperWidth + 1; j++)
    {
      //is next pancake smiley side down
      if (sInput[j] == '-')
      {
        //flip next k pancakes
        for (int k = 0; k < iFlipperWidth; k++)
        {
          if (sInput[j+k] == '-')
            sInput[j+k] = '+';
          else //sInput[j+k] == '+'
            sInput[j+k] = '-';
        }//end for k
        //incrament flip cound
        iFlipCount++;
      }//end if
    }//end for j

    //check if possible
    for (unsigned int j = sInput.length() - iFlipperWidth + 1; j < sInput.length(); j++)
    {
      if (sInput[j] == '-')
      {
        bPossible = false;
        j = sInput.length();
      }//end if
    }//end for j

    //output
    if (bPossible)
      out << "Case #" << (i + 1) << ": " << iFlipCount << endl;
    else
      out << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
    //reset flip count and bool possible
    iFlipCount = 0;
    bPossible = true;
  }//end for i

  //close filestreams
  out.close();
  in.close();
  return 0;
}//end main