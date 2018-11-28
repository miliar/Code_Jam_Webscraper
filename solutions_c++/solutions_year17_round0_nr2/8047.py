#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool isTidy(long int num)
{
  long int lastDigit = num%10;
  num /= 10;
  while(num > 0)
  {
    if(num%10 > lastDigit)
      return false;
    lastDigit = num%10;
    num /= 10;
  }
  return true;
}
void printVector(vector<int> num)
{
  for(int i = 0; i < num.size(); i++)
  {
    cout << num[i];
  }
  cout << endl;
}
void setNums(int start, int end, vector<int> &num, int value)
{
  for(int i = start; i < end; i++)
  {
    num[start] = value;
  }
}
int main()
{
  ifstream fin;
  fin.open("B-large.in");
  ofstream fout;
  fout.open("output.txt");
  int testCases;
  fin >> testCases;
  for(int loop = 0; loop < testCases; loop++)
  {
    string input;
    fin >> input;
    vector<int> num;
    int i;
    for(i = 0; i < input.length(); i++)
    {
      num.push_back(input[i] - '0');
    }
    for(i = 0; i < num.size() - 1; i++)
    {
      printVector(num);
      if(num[i] > num[i+1])
      {
        num[i] = num[i] - 1;
        for(int x = i+1; x < num.size(); x++)
        {
          num[x] = 9;
        }
        i = -1;
      }
    }
    /*
    for(int index = 0; index < num.size() - 1; index++)
    {
      for(int n = index + 1; n < num.size(); n++)
      {
        printVector(num);
        if(num[index] > num[n])
        {
          if(num[0] != 0)
            num[n-1] = num[n-1] - 1;
          num[n] = 9;
        }
      }
    }
    */
    /*
    for(i = 0; i < num.size(); i++)
    {
      printVector(num);
      if(num[index] > num[i])
      {
        num[i-1] = num[i-1] - 1;
        num[i] = 9;
      }
      /*
      if(num[i] > num[i+1])
      {

        num[i] = num[i] - 1;
        num[i+1] = 9;

        //num[i] = 9;
        //num[i-1] = num[i-1] - 1;

      }
      */
    //}

    if(num[0] < 1)
      num.erase(num.begin());
    fout << "Case #" << loop + 1 << ": ";
    for(i = 0; i < num.size(); i++)
    {
      fout << num[i];
    }
    fout << endl;
    /*
    cout << n << endl;;
    for(long int i = n; i > 0; i--)
    {
      if(i == 99999999999999999) {
        cout << "df" << endl;
      }
      if(isTidy(i))
      {
        fout << "Case #" << loop + 1 << ": " << i << endl;
        i = 0;
      }
    }
    */
  }
}
