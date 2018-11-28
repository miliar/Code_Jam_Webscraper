# include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int n[t],num1[10],num2[10],final[t],num;
	for(int i=0;i<t;i++)
	{
		cin>>n[i];
	}
	for(int i=0;i<t;i++)
	{
		int flag=1;
		int ct=0,x;
		for(int l=1;l<=n[i];l++)
		{
			x=l;
			ct=0;
			flag=1;
		while(x!=0)
		{
			num=x%10;
			x=x/10;
			num1[ct]=num;
			num2[ct]=num;
			ct++;
		}
		
		for(int j=0;j<ct;j++)
		{
			for(int k=0;k<ct-1;k++)
			{
				if(num1[k]<num1[k+1])
				{
					int temp=num1[k];
					num1[k]=num1[k+1];
					num1[k+1]=temp;
				}
			}
		}
		for(int j=0;j<ct;j++)
		{
			if(num1[j]!=num2[j])
			{
				flag=0;
				break;
			}
			
		}
		if(flag==1)
		{
			final[i]=l;
		}
	}
	}
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": "<<final[i]<<"\n";
	}
}
