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
		input>>a;
		for(int i=a.length()-2; i>-1; i--)
		{
			if(a[i]>a[i+1])
			{
				a[i] = a[i] - '0'  - 1 + '0';
				for(int j=i+1; j<a.length(); j++)
				{
					a[j] = '9';
				}
			}
		}
		if(a[0]=='0')
		a.erase(a.begin());
		output<<"Case #"<<l+1<<": "<<a<<"\n";
	}
}
