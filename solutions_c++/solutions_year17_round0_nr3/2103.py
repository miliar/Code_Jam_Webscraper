#include<bits/stdc++.h>
using namespace std;
//nksheokand
vector<long long> V;
int main()
{
	fstream in,out;
	in.open("C-large.in");
	out.open("Output.txt");
	long long t,n,k,ni,no,po,ro;
	in>>t;
	for(long long l=1;l<=t;l++)
	{
		in>>n>>k;
		ro=1;
		po=0;
		while(po+ro<k)
		{
			po=po+ro;
			ro=ro*2;
		}
		k-=po;
		n-=po;
		po++;
		if(n%po)
		{
			if(n%po>=k)
			n=n/po+1;
			else
			n=n/po;
		}
		else
		n=n/po;
		if(n%2)
		{
			no=n/2;
			ni=no+1;
		}
		else
		no=ni=n/2;
		if(no==ni)
		no-=1;
		else
		ni-=1;
		out<<"Case #"<<l<<": "<<ni<<" "<<no<<endl;
	}
	in.close();
	out.close();
	return 0;
}
