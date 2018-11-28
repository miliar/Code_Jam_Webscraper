#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;

vector<vector<bool> > input;
int testnum;
vector<int> sizeofflipper;

bool getInput()
{
  string testcases;
  string onecase;
  ifstream inputfile("input.txt");
  if (inputfile.is_open())
  {
    getline (inputfile, testcases);
    testnum = atoi(testcases.c_str());
    for (int i=0;i<testnum;i++)
    {
      getline (inputfile, onecase);
      vector<bool> arr;
      {
        for (int i=0;i<onecase.size();i++)
        {
          if (onecase[i]=='+')
          {
            arr.push_back(true);
          }
          else if (onecase[i]=='-')
          {
            arr.push_back(false);
          }
          else if (onecase[i] == ' ')
          {
            sizeofflipper.push_back(atoi(onecase.substr(i+1,onecase.length()-1).c_str()));
          }
        }
        input.push_back(arr);
      }
    }
    inputfile.close();
    return true;
  }
  else
  {
      cout << "Unable to open file";
      return false;
  }
}
int main()
{
  testnum=0;
  getInput();
  ofstream filename ("output.txt");
  filename.is_open();
  for (int j=0;j<testnum;j++)
  {
    int switchcounter=0;
    int length = input[j].size();

    for (int k=0;k<length-sizeofflipper[j]+1;k++)
    {
      if (input[j][k])
      {
        continue;
      }
      else
      {
        for (int l=0;l<sizeofflipper[j];l++)
        {
          input[j][k+l]=!input[j][k+l];
        }
        switchcounter++;
      }
    }
    bool impossible = false;
    for (int l=length;l>length-sizeofflipper[j];l--)
    {
      if (!input[j][l-1])
      {
        impossible = true;
      }
    }

    if (impossible)
    {
      filename << "Case #"<<j+1<<": IMPOSSIBLE";
    }
    else
    {
      filename << "Case #"<<j+1<<": "<<switchcounter;
    }
    //if (j!=testnum-1)
      {
          filename <<"\n";
      }
  }
  return 0;
}
