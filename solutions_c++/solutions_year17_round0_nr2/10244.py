#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

bool isTidy(int a)
{
  string s=to_string(a);
  for (int i=0; i<s.size()-1;++i)
    {
      if (s[i]>s[i+1])
	return false;
    }
  return true;
}
int main()
{
  ifstream fin;
  ofstream fout;
  fin.open("input.txt"); fout.open("output.txt", ofstream::trunc); 
  int lines; fin>>lines; //cout<<lines<<endl;
  int temp;
  for (int i=0; i<lines; ++i)
  {
    fin>>temp;// cout<<temp<<endl;
    int j;
    for (j=temp; j>=1; --j)
      {
	if (isTidy(j)) break;
      }
    fout<<"Case #"<<i+1<<": "<<j<<endl;
  }
}
