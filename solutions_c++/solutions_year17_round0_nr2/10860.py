#include<bits/stdc++.h>
#include<fstream>

using namespace std;

int tidy(long int n)
{
	long int pre=n%10;
	n=n/10;
	while(n>0)
	{
		long int cur=n%10;
		n=n/10;
		if(pre<cur)
		return 0;
		pre=cur;
	}
	return 1;
}

int main()
{
	int nt;
	ifstream file;
	file.open("input.txt");
	file>>nt;
	for(int i1=0;i1<nt;i1++)
	{
		long int n;
		file>>n;
		for(long int i=n;i>0;i--)
		{
			if(tidy(i)==1)
			{
			cout<<"Case #"<<i1+1<<": "<<i<<"\n";
			break;
			}
		}
	}
	return 0;
}
