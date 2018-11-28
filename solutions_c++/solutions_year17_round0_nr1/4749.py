#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <fstream>
#include <deque>
#include <string>
using namespace std;
#define fori(v) for(int i=0; i<v; i++)
#define forj(v) for(int j=0; j<v; j++)
#define fork(v) for(int k=0; k<v; k++)
#define forl(v) for(int l=0; l<v; l++)
#define forz(v) for(int z=0; z<v; z++)
#define mp(a,b) make_pair(a,b)
#define lli long long int
#define MAX 100001
int main()
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	int t;
	input>>t;
	forl(t)
	{
		string a;
		int k;
		input>>a>>k;
		bool alinir = true;
		int say = 0;
		fori(a.length())
		{
			if(a[i]=='-')
			{
				if(i+k>a.length())
				{
					alinir = false;
				}
				else if(alinir)
				{
					++say;
					for(int j=i+1; j<i+k; j++)
					{
						if(a[j]=='-')
						a[j]='+';
						else
						a[j]='-';
					}
				}
			}
		}
		output<<"Case #"<<l+1<<": ";
		if(!alinir)
		output<<"IMPOSSIBLE\n";
		else
		output<<say<<"\n";
	}
}
