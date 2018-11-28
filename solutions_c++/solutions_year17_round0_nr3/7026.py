#include<iostream>
#include<fstream>
using namespace std;
unsigned long long ans1(unsigned long long mind,bool a[])
{
	unsigned long long ans1;
	for (int i=mind-1; i>=0; i--)
		{
			if (a[i]==true)
			{
				ans1=mind-i; break;
			}
		}
		return ans1-1;
}
unsigned long long ans2(unsigned long long mind, bool a[],int n)
{
	unsigned long long ans2;
	for (int i=mind+1; i<n+2; i++)
		{
			if (a[i])
			{
				ans2=i-mind; break;
			}
		}
		return ans2-1;
}
int main ()
{
	int t1;
	ofstream ofs("output.txt");
	cin>>t1;
	int t=1;
	while (t<=t1)
	{
		unsigned long long n,k;
		cin>>n>>k;
		bool a[n+2];
		for (int i=0; i<n+2; i++)
		a[i]=false;
		a[n+1]=true; a[0]=true;
		int lind=0, mind, rind=n+1;
		mind=(rind+lind)/2;
		a[mind]=true; 
		for (int i=1; i<k; i++)
		{
			int max=0,curr=0;
			for (int j=1; j<n+2; j++)
			{
				curr=0; int d=j;
				while (!a[d]){
				curr++; d++;}
				if (curr>max)
				{
					max=curr;
					lind=j;
					rind=d-1;
				}
				j=d;
			}
			mind=(lind+rind)/2;
			a[mind]=true;
		}
		unsigned long long ansa=ans1(mind,a);
		unsigned long long ansb=ans2(mind,a,n);
		if (ansa<ansb)
		{
		  unsigned long long tmp=ansa;
		  ansa=ansb;
		  ansb=tmp;
		}
		ofs<<"Case #"<<t<<": "<<ansa<<" "<<ansb<<"\n";
		cout<<"Case #"<<t<<": "<<ansa<<" "<<ansb<<"\n";
		t++;
	}
}
