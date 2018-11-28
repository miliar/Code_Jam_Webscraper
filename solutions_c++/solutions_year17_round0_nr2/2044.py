#include<bits/stdc++.h>
using namespace std;
//nksheokand
vector<long long> V;
int main()
{
	fstream in,out;
	in.open("B-large.in");
	out.open("Output.txt");
	long long t,n,s,b,d;
	in>>t;
	for(long long l=1;l<=t;l++)
	{
		in>>n;
		V.clear();
		while(n>0)
		{
			V.push_back(n%10);
			n/=10;
		}
		s=V.size();
		b=-1;
		for(int i=s-2;i>=0;i--)
		if(V[i]<V[i+1])
		{
			b=i;
			break;
		}
		if(b!=-1)
		{
			b++;
			while(b<s-1 && V[b+1]==V[b])
			b++;
			V[b]--;
			for(int i=0;i<b;i++)
			V[i]=9;
		}
		n=0;
		for(int i=s-1;i>=0;i--)
		{
			n=n*10+V[i];
		}
		out<<"Case #"<<l<<": "<<n<<endl;
	}
	in.close();
	out.close();
	return 0;
}
