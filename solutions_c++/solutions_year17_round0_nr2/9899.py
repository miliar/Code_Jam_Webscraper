#include<iostream>
using namespace std;
int main()
{	freopen("B-small-attempt0.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int T;
	bool r=true;
	cin>>T;
	if(T>100||T<1)
	{
		return 0;
	}
	int a[T],b[4],k=0;
	for(int i=0;i<T;i++)
	{
		cin>>a[i];
	}
	for(int i =0;i<T;i++)
	{
		if(a[i]>1000||a[i]<1)
		{
			continue;
		}
		int temp;
		for(int j=a[i];j>0;j--)
		{	k=-1;
			r=true;
			temp=j;
			while (temp>0)
			{
				k++;
				b[k]=temp%10;
				temp /=10;
				
			}
			for(int l=k;l>0;l--)
			{
				if(b[l]>b[l-1])
				{
					r=false;
				}
			}
			if(r)
			{
				cout<<"Case #"<<i+1<<": "<<j<<"\n";
				break;
			} 
		}
	}
	return 0;
}
