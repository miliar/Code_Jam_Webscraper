#include <iostream>
#include <vector>

using namespace std;

string tidyfi(string);
bool isTidy(const string&);
string getNextTidy(string);

int main()
{
  int testCases;
  vector<string> numbers;

  string line;
  getline(cin, line);
  testCases = stoi(line);

  for(int i = 0; i < testCases; i++)
  {
    getline(cin, line);
    numbers.push_back(line);
  }

  int iter = 1;

  for(auto &num : numbers)
  {
    cout << "Case #" << iter << ": " << getNextTidy(num) << endl;
    iter++;
  }

}

string getNextTidy(string number)
{
  while(!isTidy(number))
    number = tidyfi(number);

  return number;
}

bool isTidy(const string& number)
{
  int len = number.length();
  
  bool tidy = true;
  char last;

  for(int i = 0; i < len; i++)
  {
    if(i == 0)
    {
      last = number[i];
      if(number[i] == '0')
        return false;
    }
    else
    {
      if(number[i] >= last)
        last = number[i];
      else
        return false;
    }
  }

  return true;
}

string tidyfi(string number)
{
  int length = number.length();
  
  bool cutFirst = false;

  for(int i = 0; i < length; i++)
  {
    if(i == 0)
    {
      if(number[i] == '0')
      {
        cutFirst = true;
        break;
      }
    }
    else
    {
      if(number[i] < number[i-1])
      {
        for(int j = i; j < length; j++)
          number[j] = '9';

        number[i-1] = number[i-1] - 1;

        break;
      }
    }
  }

  if(cutFirst)
    number = number.substr(1, length);

  return number;
}
