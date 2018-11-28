#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
	ifstream in("test.in");
	ofstream out("output.out");
	unsigned long long n,i,j,temp,t,x,div;
	int flag,count;
	in>>t;
	for(i=1;i<=t;i++)
	{
		in>>n;
		if(n/10==0)
		{
			out<<"Case #"<<i<<": "<<n<<endl;
			continue;
		}
		for(j=n;j>0;j--)
		{
			temp=j;
			flag=0;
			x=temp%10;
			count=1;
			temp/=10;
			for(;temp>0;temp/=10)
			{
				if((temp%10)>x)
				{
					div=pow(10,count);
					j-=j%div;
					flag=1;
					break;
				}
				x=temp%10;
				count++;
			}
			if(flag==0)
			{
				out<<"Case #"<<i<<": "<<j<<endl;
				break;
			}
		}
	}
	in.close();
	out.close();
	return 0;
}