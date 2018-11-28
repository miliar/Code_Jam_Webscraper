#include<iostream>
#include<string>
using namespace std;

bool biggerRight(char left, char right)
{
  if(left>right)return false;
  return true;
}



/*
bool isTidy(int myNum)
{
  string theNum = to_string(myNum);
  for(int i=0;i<theNum-1;i++)
  {
    if(biggerRight)
    {

    }

  }
}
*/

int main()
{
  int numCases;
  int numIn;
  int caseNum = 0;
  cin >> numCases;

  while(cin >> numIn)
  {
    caseNum++;


    bool itsTidy = false;
    bool checkDone = false;
    while(!checkDone)
    {
      string theNum = to_string(numIn);
      if(theNum.size()==1)
      {
        itsTidy = true;
        checkDone = true;
      }
      else
      {
        for(int i = 0; i<(theNum.size()-1);i++)
        {
          if(biggerRight(theNum[i],theNum[i+1]))
          {
            if(i==(theNum.size()-2))
            {
              itsTidy = true;
              checkDone = true;
            }
          }
          else
          {
            numIn--;
            itsTidy = false;
            checkDone = false;
            i = theNum.size();

          }
        }
      }

    }
    if(itsTidy)
    {
      cout << "Case #" << caseNum << ": " << numIn << endl;
    }

  }





}
