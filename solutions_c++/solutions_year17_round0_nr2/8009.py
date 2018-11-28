//Joey Klix
//Google Code Jam 2017
//B. Tidy Numbers

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  //vars
  const string sfileinput = "B-large.in";
  const string sfileoutput = "output.txt";
  ifstream in;
  ofstream out;
  int iCases = 0;
  string sLastNumber = "";
  bool bReplaceWithNine = false;

  //open files and read in number of cases
  in.open(sfileinput.c_str());
  out.open(sfileoutput.c_str());
  in >> iCases;

  //loop for each case
  for (int i = 0; i < iCases; i++)
  {
    //reading LastNumber Counted
    in >> sLastNumber;

    //loop through each number in string
    for (unsigned int j = 1; j < sLastNumber.length(); j++)
    {
      //replace number with 9 if previous number was changed
      if (bReplaceWithNine)
        sLastNumber[j] = '9';
      //if zero is found or previous number is bigger
      else if (sLastNumber[j] == '0' || sLastNumber[j] < sLastNumber[j-1])
      {
        //make sure decrementing previous number doesn't break rules
        while (j > 1 && (sLastNumber[j-1] - 1) < sLastNumber[j-2])
          j--;
        sLastNumber[j-1]--;
        sLastNumber[j] = '9';
        bReplaceWithNine = true;
      }//end else if
    }//end for j

    //if first number is 0
    if (sLastNumber[0] == '0')
     sLastNumber.erase(0, 1);

    //output
    out << "Case #" << (i + 1) << ": " << sLastNumber << endl;
    //reset bool
    bReplaceWithNine = false;
  }//end for i  

  //close filestreams
  out.close();
  in.close();
  return 0;
}//end main