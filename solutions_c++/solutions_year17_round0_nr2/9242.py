#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int l;
string str;

void test ();
int main ()
{
	
	ifstream in ("input.txt");
	ofstream out ("output.txt");
	int t;
	in>>t;
	for (int d=1;d<=t;d++)
	{
		in>>str;
		l=str.length();
		test ();
		out<<"Case #"<<d<<": ";
		for (int e=0;e<l;e++)
		{
			if (str[e]>48&&str[e]<58) out<<str[e];
		}
		out<<endl;
	}
	
	
	return 0;
}

void test ()
{
	bool a=0;
	if (l>1)
	{
		for (int b=0;b<l-1;b++)
		{
			if (str[b]>str[b+1])
			{
				str[b]-=1;
				for (int c=b+1;c<l;c++)
				{
					str[c]=57;
				}
				a=1;
			}
		}
	}
	if (a) test ();
}
