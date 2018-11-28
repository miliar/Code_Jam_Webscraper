/*  Problem B. Tidy Numbers
    Jesus Alejandro Galvan Villarreal
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isTiny(string s)
{
  for(int i = 0; i < s.length()-1; i++)
  {
    if(s[i] > s[i+1])
      return false;
  }
  return true;
}

void solver(const int &caseNum)
{
  long long n;
  cin >> n;

  string s = to_string(n);
  int last = s.length()-1;

  for(int i = 0; i < last; i++)
  {
    if(!isTiny(s))
    {
      s[last-i-1]-= 1;
      s[last-i] = '9';
    }
  }

  if(s[0] == '0')
    cout << "Case #" << caseNum << ": " << s.substr(1) << endl;
  else
    cout << "Case #" << caseNum << ": " << s << endl;
}

int main()
{
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    solver(i);
  }
}