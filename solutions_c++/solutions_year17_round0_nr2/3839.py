#include <fstream>
#define ll long long
using namespace std;

ll toLL(string s)
{
  ll p10 = 1;
  ll t = 0;
  for(int i=s.length()-1; i>=0; i--)
  {
    t += (s[i] - '0') * p10;
    p10 *= 10;
  }
  return t;
}

int main()
{
  int T;
  ifstream in("B-large.in");
  ofstream out("output.txt");
  in>>T;

  for(int t=0; t<T; t++)
  {
    string str;
    in>>str;
    int ind = str.length();
    for(int i=str.length()-1; i>=1; i--)
     if(str[i-1] > str[i])
     {
       ind = i;
       str[i-1]--;
     }

    for(int i=ind; i<str.length(); i++)
     str[i] = '9';

    out<<"Case #"<<(t+1)<<": "<<toLL(str)<<"\n";
  }

  in.close();
  out.close();
  return 0;
}
