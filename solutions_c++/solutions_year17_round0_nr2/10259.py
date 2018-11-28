#include<iostream>
using namespace std;
int desc(long long int a[],long long int n)
{
	for(int i = 0 ; i < n - 1 ; i++ )
   {
      if( a[i] < a[i+1] )
      {
      	return 0;
      }
   }
   return 1;
}
int main()
{
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		long long int n;
		long long int a[30];
		cin>>n;
		for(long long int i=n;i>=1;i--)
		{
			long long int temp=i,j=0;
			while(temp>0)
			{
				a[j++]=temp%10;
				temp=temp/10;		
			}
			if(desc(a,j)==1)
			{
				cout<<"Case "<<"#"<<l<<": "<< i<<endl;
				break;
			}
		}
	}
	return 0;
}
