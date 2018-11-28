//Joey Klix
//Google Code Jam 2017
//B. Stable Neigh-bors

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  //vars
  const string sfileinput = "B-small-attempt1.in";
  const string sfileoutput = "output.txt";
  ifstream in;
  ofstream out;
  int iCases = 0;
  int iNumHorses = 0, iR = 0, iO = 0, iY = 0, iG = 0, iB = 0, iV = 0;
  bool bPossible = true;
  string sSolution = "";

  //open files and read in number of cases
  in.open(sfileinput.c_str());
  out.open(sfileoutput.c_str());
  in >> iCases;

  for (int i = 0; i < iCases; i++)
  {
    in >> iNumHorses >> iR >> iO >> iY >> iG >> iB >> iV;

    //set first color
    if (iR > 0)
    {
      sSolution = "R";
      iR--;
    }
    else if (iO > 0)
    {
      sSolution = "O";
      iO--;
    }
    else if (iY > 0)
    {
      sSolution = "Y";
      iY--;
    }
    else if (iG > 0)
    {
      sSolution = "G";
      iG--;
    }
    else if (iB > 0)
    {
      sSolution = "B";
      iB--;
    }
    else if (iV > 0)
    {
      sSolution = "V";
      iV--;
    }

    for (int j = 1; j < iNumHorses; j++)
    {
      if (sSolution[j-1] == 'R')
      {
        if (iG > 0)
        {
          sSolution += 'G';
          iG--;
        }
        else if (iY > 0 && iB <= iY)
        {
          sSolution += 'Y';
          iY--;
        }
        else if (iB > 0)
        {
          sSolution += 'B';
          iB--;
        }
      }
      else if (sSolution[j-1] == 'O')
      {
        if (iB == 0)
        {
          bPossible = false;
          j = iNumHorses;
        }
        else
        {
          sSolution += 'B';
          iB--;
        }
      }
      else if (sSolution[j-1] == 'Y')
      {
        if (iV > 0)
        {
          sSolution += 'V';
          iV--;
        }
        else if (iR > 0 && iB <= iR)
        {
          sSolution += 'R';
          iR--;
        }
        else if (iB > 0)
        {
          sSolution += 'B';
          iB--;
        }        
      }
      else if (sSolution[j-1] == 'G')
      {
        if (iR == 0)
        {
          bPossible = false;
          j = iNumHorses;
        }
        else
        {
          sSolution += 'R';
          iR--;
        }
      }
      else if (sSolution[j-1] == 'B')
      {
        if (iO > 0)
        {
          sSolution += 'O';
          iO--;
        }
        else if (iY > 0 && iR <= iY)
        {
          sSolution += 'Y';
          iY--;
        }
        else if (iR > 0)
        {
          sSolution += 'R';
          iR--;
        }
      }
      else if (sSolution[j-1] == 'V')
      {
        if (iY == 0)
        {
          bPossible = false;
          j = iNumHorses;
        }
        else
        {
          sSolution += 'Y';
          iY--;
        }
      }
    }//end for j

    //check if valid stable
    if (sSolution[0] == sSolution[iNumHorses-1]
      || (sSolution[0] == 'R' && sSolution[iNumHorses-1] == 'O') || (sSolution[0] == 'R' && sSolution[iNumHorses-1] == 'V')
      || (sSolution[0] == 'O' && sSolution[iNumHorses-1] == 'Y') || (sSolution[0] == 'O' && sSolution[iNumHorses-1] == 'R')
      || (sSolution[0] == 'Y' && sSolution[iNumHorses-1] == 'G') || (sSolution[0] == 'Y' && sSolution[iNumHorses-1] == 'O')
      || (sSolution[0] == 'G' && sSolution[iNumHorses-1] == 'B') || (sSolution[0] == 'G' && sSolution[iNumHorses-1] == 'Y')
      || (sSolution[0] == 'B' && sSolution[iNumHorses-1] == 'V') || (sSolution[0] == 'B' && sSolution[iNumHorses-1] == 'G')
      || (sSolution[0] == 'V' && sSolution[iNumHorses-1] == 'R') || (sSolution[0] == 'V' && sSolution[iNumHorses-1] == 'B')
      || iR > 0 || iO > 0 || iY > 0 || iG > 0 || iB > 0 || iV > 0)
      bPossible = false;

    
    //output
    if (bPossible)
      out << "Case #" << (i + 1) << ": " << sSolution << endl;
    else
      out << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;

    //reset vars
    bPossible = true;
    sSolution = "";
  }//end for i


  //close filestreams
  out.close();
  in.close();
  return 0;
}//end main