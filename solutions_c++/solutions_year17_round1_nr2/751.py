#include <iostream>
#include <vector>
#include <math.h>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <fstream>
using namespace std;
#define fori(v) for(int i=0; i<v; i++)
#define forj(v) for(int j=0; j<v; j++)
#define forl(v) for(int l=0; l<v; l++)
#define fork(v) for(int k=0; k<v; k++)
#define mp(a,b) make_pair(a,b)
#define ff first
#define ss second
#define lli long long int
int main()
{
	ifstream in;
	in.open("input.txt");
	ofstream out;
	out.open("output.txt");
	int t;
	in>>t;
	forl(t)
	{
		int n,p;
		in>>n>>p;
		int required[n];
		double available[n][p];
		int last_step[n];
		fori(n)
		{
			in>>required[i];
			last_step[i] = 0;
		}
		fori(n)
		{
			forj(p)
			{
				in>>available[i][j];
			}
			sort(available[i],available[i]+p);
		}
		int say = 0;
		int maxx = 1;
		int i = 0 ;
			while(i<n)
			{
				int j = last_step[i];
				bool alindi = false;
				bool dogurdan = true;
				double eded = maxx*required[i];
				double a = eded - eded/10;
				a-=0.0000000000001;
				double b = eded + eded/10;
				b+=0.0000000000001;
				while(j<p && !alindi)
				{
					if(available[i][j]<a)
					{
						++j;
						last_step[i] = j;
					}
					else if(available[i][j]>b)
					{
						alindi = true;
						dogurdan = false;
					}
					else
					{
						alindi = true;
					}
				}
				if(!alindi)
				{
					i = n+1;
				}
				else if(!dogurdan)
				{
					++maxx;
					i = -1;
				}
				else if(i==n-1)
				{
					fork(n)
					last_step[k]++;
					i = -1;
					++say;
				}
				++i;
			}
		out<<"Case #"<<l+1<<": "<<say<<endl;
	}
}
