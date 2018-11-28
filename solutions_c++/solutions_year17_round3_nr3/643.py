#include<bits/stdc++.h>
using namespace std;
//nksheokand
struct node
{
	double val;
	bool operator<(const node& r) const
	{
		return val>(r.val);
	}
};
int main()
{
	priority_queue<node,vector<node> > PQ;
	node n1,n2;
	fstream in,out;
	in.open("C-small-1-attempt0.in");
	out.open("Output.txt");
	int t,n,k;
	double u,r;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>n>>k>>u;
		while(!PQ.empty())
		PQ.pop();
		for(int i=0;i<n;i++)
		{
			in>>n1.val;
			PQ.push(n1);
		}
		if(n==1)
		r=PQ.top().val+u;
		else
		{
			while(u>0.0)
			{
				n1=PQ.top();
				PQ.pop();
				n2=PQ.top();
				r=max(0.0001,n2.val-n1.val);
				r=min(r,u);
				n1.val+=r;
				u-=r;
				PQ.push(n1);
			}
			r=PQ.top().val;
			PQ.pop();
			while(!PQ.empty())
			{
				r*=(PQ.top().val);
				PQ.pop();
			}
		}
		out<<"Case #"<<l<<": "<<fixed<<r<<endl;
	}
	in.close();
	out.close();
	return 0;
}
