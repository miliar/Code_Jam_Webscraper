#include<iostream>
#include<math.h>
using namespace std;
int len(int x) {
    /*if(x>=1000000000) return 10;
    if(x>=100000000) return 9;
    if(x>=10000000) return 8;
    if(x>=1000000) return 7;
    if(x>=100000) return 6;
    if(x>=10000) return 5;*/
    if(x>=1000) return 4;
    if(x>=100) return 3;
    if(x>=10) return 2;
    return 1;
}
int main()
{
	int t;
	cin>>t;
	int n[t],out[t];
	int i,k,j,p,q,flag,num;
	for(i=0;i<t;i++)
		cin>>n[i];
	for(i=0;i<t;i++)
	{
		if(len(n[i])==1)
			out[i]=n[i];
		else
		{
			for(k=n[i];k>0;k--)
			{
				flag=0;
				q=9;
				num=k;
				for(j=0;j<len(k);j++)
				{
					p=num%10;
					if(p<=q)
						flag=1;
					else{
						flag=0;
						break; }
					q=p;
					num=num/10;
				}
				if(flag==1)
				{
					out[i]=k;
					break;
				}
			}
		}
	}
	for(i=0;i<t;i++)
		cout<<"Case #"<<i+1<<": "<<out[i]<<"\n";
	return 0;
}