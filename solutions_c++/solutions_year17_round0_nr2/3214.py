#include <iostream>
#include <sstream>
using namespace std;

bool isTidy(unsigned long long l)
{
  ostringstream os;
  os << l;
  string digits = os.str();
  for(int i = 0; i < digits.length() - 1; i++)
    {
      if(digits[i] > digits[i+1])
	return false;
    }
  return true;
}	   

unsigned long long adjustNum(unsigned long long l)
{
  ostringstream os;
  os << l;
  string digits = os.str();
  int adjIdx;
  for(int i = digits.length()-1; i > 0; i--)
    {
      if(digits[i-1] > digits[i])
	adjIdx = i - 1;
    }
  digits[adjIdx] = digits[adjIdx] - 1;
  for(int j = adjIdx + 1; j < digits.length(); j++)
    {
      digits[j] = '9';
    }
  return stoull(digits);
}

unsigned long long lastTidyNum(unsigned long long l)
{
  while(l > 10)
    {
      if(isTidy(l))
	return l;
      l = adjustNum(l);
    }
  return l;
}

int main() {

  int t;
  unsigned long long l;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> l;
    cout << "Case #" << i << ": " << lastTidyNum(l) << endl;
  }

  return 0;
}
