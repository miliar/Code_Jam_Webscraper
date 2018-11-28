#include<iostream>
#include <algorithm>
#include<cstdio>
using namespace std;

int main()
{
	
	freopen("C-small-1-attempt2.in","r",stdin);
	freopen("bathoutput5.out","w",stdout);
	
	int t;
	cin>>t;
		
	int b,p;
	for(int i=0;i<t;i++)
	{
		
		cin>>b;
		cin>>p;
		int ar[b+2];
		int oc[b+2]={0};
		
		oc[0]=1;oc[b+1]=1;
		
		int l[b+2]={0};
		int r[b+2]={0};
		
		
		int km=0;
		int lm,rm;
		for(int j=0;j<p;j++)
		{
			//cout<<j;
			int minim=-1;
			int maxim=-1;int minim2,maxim2;
			int flag=0;
			for(int k=1;k<=b;k++)
			{
				if(oc[k]!=1)
				{
					
					l[k]=0;r[k]=0;
					for(int ki=k;ki>0&&oc[ki-1]!=1;ki--)
						l[k]++;
					for(int kj=k;oc[kj+1]!=1;kj++)
						r[k]++;
					minim2=min(l[k],r[k]);
					//maxim=maxim2;
					maxim2=max(l[k],r[k]);
					if(minim2>minim)
					{	
						flag=1;
						minim=minim2;
						maxim=maxim2;
						km=k;
						lm=l[k];
						rm=r[k];
					}
					else if(minim2==minim&&maxim2>maxim)
					{
						flag=1;
						maxim=maxim2;
						km=k;
						lm=l[k];
						rm=r[k];
					}
				}
			}
	
			if(flag==1)
				oc[km]=1;
			//for(int x=0;x<b+2;x++)
			//	cout<<oc[x]<<" ";
			//cout<<endl;

		}
		cout<<"Case #"<<i+1<<": "<<max(lm,rm)<<" "<<min(lm,rm)<<endl;
	}
}	
