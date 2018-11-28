#include<iostream>
#include<string>
using namespace std;

int numIn;
string theNum;
bool allNine = false;


char toggle(char inChar)
{

  if(inChar == '+')inChar = '-';
  else inChar = '+';

  return inChar;
}

bool areAllPlus(string array)
{
    for(int i = 0;i<array.size();i++)
    {
      if(array[i]=='-') return false;
    }
    return true;
}

int main()
{
    int numToggles;
    int caseNum=0;
    int numCases;
    string pattern;
    int spadeSize;
    cin >> numCases;

    while(cin >> pattern)
    {
      caseNum++;
      numToggles=0;
      cin >> spadeSize;

      if(areAllPlus(pattern))
      {
        cout << "Case #" << caseNum << ": " << numToggles << endl;
      }
      else
      {
        for(int i = 0;i<=pattern.size()-spadeSize;i++)
        {
          if(pattern[i]=='-')
          {
            numToggles++;
            for(int j = 0; j<spadeSize;j++)
            {
              pattern[i+j]=toggle(pattern[i+j]);
            }
            if(areAllPlus(pattern))
            {
                cout << "Case #" << caseNum << ": " << numToggles << endl;
            }
          }
        }
        if(!areAllPlus(pattern))
        {
          cout << "Case #" << caseNum << ": " << "IMPOSSIBLE" << endl;
        }
      }

    }
}
