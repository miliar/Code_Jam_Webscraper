//Joey Klix
//Google Code Jam 2017
//A. Steed 2: Cruise Control

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
  //vars
  const string sfileinput = "A-large.in";
  const string sfileoutput = "output.txt";
  ifstream in;
  ofstream out;
  int iCases = 0;
  int iDestination = 0, iNumofHorses = 0;
  double dStartPos = 0, dSpeed = 0;
  double dMaxTime = 0, dTime = 0;

  //open files and read in number of cases
  in.open(sfileinput.c_str());
  out.open(sfileoutput.c_str());
  in >> iCases;

  for (int i = 0; i < iCases; i++)
  {
    in >> iDestination >> iNumofHorses;
    for (int j = 0; j < iNumofHorses; j++)
    {
      in >> dStartPos >> dSpeed;
      dTime = (iDestination - dStartPos) / dSpeed;
      if (dTime > dMaxTime)
        dMaxTime = dTime;
    }//end for j

    //output
    out << fixed;
    out << setprecision(6);
    out << "Case #" << (i + 1) << ": " << (iDestination / dMaxTime) << endl;

    //reset vars
    dMaxTime = 0;
  }//end for i


  //close filestreams
  out.close();
  in.close();
  return 0;
}//end main