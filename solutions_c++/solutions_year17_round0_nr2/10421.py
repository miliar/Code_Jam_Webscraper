#include<bits/stdc++.h>

using namespace std;

#include <fstream>

int main()
{
ifstream fin ("B-small-attempt1.in");
ofstream fout("outd");

	int i,j,k,t,m,n,l,flag=0;
fin>>t;
//	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	//	scanf("%d",&n);
	fin>>n;
		m=n;
		flag=0;
		for(;m>=1;m--)
		{
			flag=0;
			l=m%10;
			j=m;
		//	printf("no----%d",m);
			while(j!=0&&flag==0)
			{
				j=j/10;
				k=j%10;
				//printf("k=%d  j=%d\n",k,j);
				if(k<=l)
			{		flag=0;
					l=k;
			}
				else
			{
					flag=1;	
			break;
			}
			}
			if(flag==0)
			break;
		}	
	//	printf("Case %d: %d\n",i+1,m);
		fout<<"Case #"<<i+1<<": "<<m<<endl;
		
	}
	
	return 0;
}
