#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool isDone(vector<char> values)
{
  int i;
  for(i = 0; i < values.size(); i++)
  {
    if(values[i] != '+')
      return false;
  }
  return true;
}
void flip(vector<char>& values, int start, int stop)
{
  for(int i = start; i < stop; i++)
  {
    if(values[i] == '+')
      values[i] = '-';
    else
      values[i] = '+';
  }
}
void printVector(vector<char> values)
{
  for(int i = 0; i < values.size(); i++)
  {
    cout << values[i];
  }
  cout << endl;
}
void readIn(vector<char>& values, string str)
{
  for(int i = 0; i < str.length(); i++)
  {
    values.push_back(str[i]);
  }
}
int main()
{
  ifstream in;
  in.open("A-large.in");
  ofstream out;
  out.open("output.txt");
  int testCases = 0;
  in >> testCases;
  for(int n = 0; n < testCases; n++)
  {
    vector<char> values;
    int size;
    string valStr;
    in >> valStr;
    readIn(values, valStr);
    in >> size;
    int flips = 0;
    for(int i = 0; i <= values.size() - size; i++)
    {
      if(values[i] == '-')
      {
        flip(values, i, i + size);
        flips++;
      }
    }
    out << "Case #" << n + 1 << ": ";
    if(isDone(values))
      out << flips << endl;
    else
      out << "IMPOSSIBLE" << endl;
  }
}
