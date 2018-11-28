#include<bits/stdc++.h>
using namespace std;
//nksheokand
vector<pair<int,int> > C;
vector<pair<int,int> > J;
int main()
{
	fstream in,out;
	in.open("B-small-attempt0.in");
	out.open("Output.txt");
	int t,ac,aj,a,b,c,d;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>ac>>aj;
		C.clear();
		C.resize(ac);
		J.clear();
		J.resize(aj);
		for(int i=0;i<ac;i++)
		{
			in>>C[i].first>>C[i].second;
		}
		for(int i=0;i<aj;i++)
		{
			in>>J[i].first>>J[i].second;
		}
		if(ac<=1 && aj<=1)
		out<<"Case #"<<l<<": 2"<<endl;
		else if(ac==2)
		{
			if(C[0].first<C[1].first)
			{
				a=C[0].first;
				b=C[0].second;
				c=C[1].first;
				d=C[1].second;
			}
			else
			{
				a=C[1].first;
				b=C[1].second;
				c=C[0].first;
				d=C[0].second;
			}
			if(d-a<=720 || c-b>=720)
			out<<"Case #"<<l<<": 2"<<endl;
			else
			out<<"Case #"<<l<<": 4"<<endl;
		}
		else if(aj==2)
		{
			if(J[0].first<J[1].first)
			{
				a=J[0].first;
				b=J[0].second;
				c=J[1].first;
				d=J[1].second;
			}
			else
			{
				a=J[1].first;
				b=J[1].second;
				c=J[0].first;
				d=J[0].second;
			}
			if(d-a<=720 || c-b>=720)
			out<<"Case #"<<l<<": 2"<<endl;
			else
			out<<"Case #"<<l<<": 4"<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}
