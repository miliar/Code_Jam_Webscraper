#include<bits/stdc++.h>
using namespace std;
int main()
{
	
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-Output.out","w",stdout);
	
	int t,n,p;
	cin>>t;
	for(int y=1;y<=t;y++)
	{
		cin>>n;
		cin>>p;
		cout<<"Case #"<<y<<": ";
	
		int pro[n+2],a[n+1],b[n+1];
		pro[0]=1;
		pro[n+1]=1;
		for(int i=1;i<=n;i++)
		{
			pro[i]=0;
		}
		for(int i=0;i<=n;i++)
		{
			a[i]=0;
			b[i]=0;
		}
		int add=0;
		for(int s=1;s<=p;s++)
		{
			add++;
			int c=0,z=0,max=0,test,r=0,l=0;
			for(int i=0;i<n+1;i++)
			{
				if(pro[i+1]==0)
				{
					if(z==0)
					{
				
						a[c]=i+1;
						c++;
					}
					z++;
				}
				else
				{
				
					b[c-1]=z;
					z=0;
				}
			}
			int pos =0;
			max=b[0];
			for(int i=0;i<=n;i++)
			{
				if(b[i]>max)
				{
					max=b[i];
					pos=i;
				}
			}
	
			if(max%2==0)
			{
				test=max/2+a[pos]-1;
				pro[test]=1;
				if(add==p)
				{
					for(int w=test+1;w<n+1;w++)
					{
						if(pro[w]==0)
						{
					
							r++;
							
						}
						else
							break;
					}
					for(int q=test-1;q>0;q--)
					{
						if(pro[q]==0)
						{
							l++;
							
						}
						else
							
							break;
					}
					if(r>l)
						cout<<r<<" "<<l<<endl;
					else
						cout<<l<<" "<<r<<endl;
				}
				
			}
			if(max%2!=0)
			{
				test=max/2+a[pos];
				pro[test]=1;
			
				if(add==p)
				{
					for(int w=test+1;w<n+1;w++)
					{
						if(pro[w]==0)
						{
					
							r++;
							
						}
						else
							
							break;
					}
					for(int q=test-1;q>0;q--)
					{
						if(pro[q]==0)
						{
							l++;
						}
						else
							break;
					}
					if(r>l)
						cout<<r<<" "<<l<<endl;
					else
						cout<<l<<" "<<r<<endl;
				}
			}
		}
	
		
	}
	
}
