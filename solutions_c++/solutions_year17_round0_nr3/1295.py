//https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#include<bits/stdc++.h>
using namespace std;
long long int a[66];
//map<long long int,long long int> m_min;//count,value
//map<long long int,long long int> m_max;//count,value
long long int count1,num1,temp1,even1=0,tempcount1;//small
long long int count2,num2,temp2,even2=0,tempcount2;//big
int main()
{
	//  freopen("C-large.in","r",stdin);
	 // freopen("clarge.txt","w",stdout);
	int tc;
	cin>>tc;
	
	
	for(int t=1;t<=tc;t++)
	{
		
		long long int n,k;
		cin>>n>>k;
		long long int c=0,temp=1,ans,chk,number;
		while((temp-1)<k)
		{
			chk=temp;
			temp*=2;
			if(temp/2!=chk)
			break;
			c++;
		}
		c--;
		number=k-chk+1;
		
		//cout<<"\nchk="<<chk;
		//cout<<"\nnumber="<<number;
		//cout<<"\n";
		
		ans=n;
		if(k!=1)
		{	
			if(n%2==0)
			{
				num1=n/2-1;
				count1=1;
				num2=n/2;
				count2=1;
			}
			else
			{
				num1=n/2;
				count1=1;
				num2=n/2;
				count2=1;
			}
			 for(int i=1;i<c;i++)
			{
				if(num1%2==0)
				{
					temp1=num1/2-1;
					num1=temp1;
					tempcount1=count1;
					even1=1;
				}
				else
				{
					temp1=num1/2;
					num1=temp1;
					count1=2*count1;
				}
				
				
				
				if(num2%2==0)
				{
					temp2=num2/2-1;
					num2=temp2+1;
					even2=1;
					tempcount2=count2;
				}
				else
				{
					temp2=num2/2;
					num2=temp2;
					count2=2*count2;
				}
				
				if(even1)
				{
					count2+=tempcount1;
				}
				if(even2)
				{
					count1+=tempcount2;
				}
				even1=0;
				even2=0;
				
			}
			
			if(number>count2)
			ans=num1;
			else
			ans=num2;
			
			
		}
		
		long long total=ans;
		if(total%2==0)
		 cout<<"Case #"<<t<<": "<<total/2<<" "<<total/2-1<<"\n";
		 else
		 cout<<"Case #"<<t<<": "<<total/2<<" "<<total/2<<"\n";
		
	}
}
