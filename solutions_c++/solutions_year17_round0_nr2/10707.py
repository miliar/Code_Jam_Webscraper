#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
	int x,min=10,j=0,i=0,y=0,t;
	ifstream in;
	in.open("B-small-attempt3.in");
	ofstream out;
	out.open("output.out");
	in>>t;
	for(int k=0;k<t;k++)
	{
		in>>x;
	for(i=x;i>=1;i--)
	{
		y=i;
		min=10;
		while(y>0)
		{
			j=y%10;
			if(j<=min)
				min=j;
			else
				break;
			y/=10;
		}
		if(y<=0)
			break;
	}
	out<<"Case #"<<k+1<<": "<<i<<endl;
}
}
