// Example program
#include <iostream>
#include <string>
#include<fstream>
using namespace std;
int main()
{
	int cse = 1;
	 string s;
	ifstream ifile;
	ofstream ofile;
	ifile.open("B-small-attempt2.in");
	ofile.open("output.txt");
	ofile.clear();
	int k;
	ifile >> k;
	for(int m = 0; m < k; m++)
	{
		ifile>> s;
		bool f2;
		do
		  {
			  f2 = true;
			  for(int i = 1; i < s.length() && f2; i++)
				if (s[i-1] > s[i])
					f2 = false;
			if (!f2)
			{
				int a = atoi(s.c_str());
				a--;
				s = to_string(a);
			}
		  }  while(!f2);
		  ofile <<"Case #" << cse << ": " << s << endl;
		cse++;
	}
	ifile.close();
	ofile.close();
 system("pause");
  return 0;
}

