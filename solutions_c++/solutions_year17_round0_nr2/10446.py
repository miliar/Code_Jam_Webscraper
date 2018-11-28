#include <iostream>
using namespace std;

int main() {
	int T,i,N,j,k=0,c1,tid,num;
	int a[18];
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>N;
		for(j=N;j>=1;j--)
		{
			if(j%10!=0)
			{
				num=j;
				k=0;
				c1=0;
				while(num>0)
				{
					a[k]=num%10;
					num=num/10;
					k++;
				}
				for(int l=k-1;l>=1;l--)
				{
					if(a[l-1]>=a[l])
					{
						c1++;
					}
					else
					{
						break;
					}
				}
				if(c1==k-1)
				{
					tid=j;
					break;
				}
				else
				{
					int pow=1;
					int n1=k-(c1+1);
					for(int l=1;l<=n1;l++)
					{
						pow=pow*10;
					}
					i=i-(i%pow);
				}
			}
		}	
		cout<<"Case #"<<i<<": "<<tid<<"\n";
	}
	return 0;
}