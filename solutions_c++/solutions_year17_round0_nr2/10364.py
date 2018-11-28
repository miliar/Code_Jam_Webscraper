#include<bits/stdc++.h>
#include<fstream>
#define endl "\n"
using namespace std;
int main()
{
	ifstream fin("B-small-attempt1.in");
	ofstream fout("output.txt");
	int t,x,n,y,f=0,bk,d,d1;
	fin>>t;
	for(x=1;x<=t;x++)
	{
		fout<<"Case #"<<x<<": "; 
		fin>>n;
		for(y=n;y>=1;y--)
		{
			f=0;
			bk=y;
			d=bk%10;
			bk/=10;
			while(bk>0)
			{
				d1=bk%10;
				bk/=10;
				if(d1<=d)
				{
					d=d1;
				}
				else
				{
					f=1;
					break;
				}
			}
			if(!f)
			{
				break;
			}
		}
		fout<<y<<endl;
	}
	return 0;
}
