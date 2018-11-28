#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <fstream>

using namespace std;

int testnum;
vector<string> inputs;

bool getInputs()
{
  string testcases;
  string onecasestring;
  ifstream inputfile("input.txt");
  if (inputfile.is_open())
  {
    getline (inputfile, testcases);
    testnum = atoi(testcases.c_str());
    for (int i=0;i<testnum;i++)
    {
      getline (inputfile, onecasestring);
      inputs.push_back(onecasestring);
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
  //getInput();
  getInputs();
  ofstream filename ("output.txt");
  filename.is_open();
  for(int i=0;i<testnum;i++)
  {
    bool l=true;
    string str = inputs[i];

    for (int j=str.length()-1;j>0;j--)
    {
      if (str[j]<str[j-1]){
        int number = str[j-1]-'0';

        number--;
        str[j-1] = number +'0';
        for (int k=j;k<str.length();k++)
        {
          str[k]='9';
        }
      }

    }

    if (str[0] == '0')
    {
      str = str.substr(1,str.length()-1);
    }
    filename << "Case #"<<i+1<<": "<<str;
    filename <<"\n";
  }

    return 0;
}
