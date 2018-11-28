#include <bits/stdc++.h>
using namespace std;
int main()
{
	int cp,digit[19];
	int pos;
	bool ver;
	ifstream I("B-large.in");
	ofstream O("B-large.out");
	long long n;
	I>>cp;
	for(int t=1;t<=cp;t++)
	{
		memset(digit,0,sizeof digit);
		I>>n;
		pos=18;
		while(n!=0)
		{
			digit[pos]=n%10;
			n/=10;
			pos--;
		}
		do{
			ver=true;
			for(int i=0;i<18;i++)
			{
				if(digit[i]>digit[i+1])
				{
					ver=false;
					digit[i]-=1;
					for(int j=i+1;j<19;j++)
						digit[j]=9;
				}
			}
		}while(!ver);
		O<<"Case #"<<t<<": ";
		ver=false;
		for(int i=0;i<19;i++)
		{	
			if(digit[i]!=0 and !ver)
				ver=true;
			if(ver)
			{
				O<<digit[i];
			}
		}
		O<<endl;
	}
	return 0;
}