#include<iostream>
#include<conio.h>
#include<vector>
#include<algorithm>
#include<conio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i=0;
	float n[1000],k[1000];
	int res[1000];
	int count=0;
	for(int m=0;m <t;m ++)
	{
			cin>>n[m]>>k[m];
	}
	for(int m=0;m<t;m++)
	{
			vector<int> a(10000,0);
			a[0]=n[m];
			int r1,r2;
			int i=1;
			if(n[m]/k[m]<1.3)
			{
				r2=r1=0;
				goto a1;
			}
			for(int j=0;j<k[m];j++)
			{
				sort(a.rbegin(),a.rend());
				int temp=a[0];
				if(a[0]%2==0)
				{
					r1=a[i]=temp/2;
					r2=a[i+1]=temp/2 - 1;
					if(r2<0)r2=0;
				}	
				else
				{
					r1=r2=a[i]=a[i+1]=temp/2;
				}
				i+=2;
				a[0]=0;
			}
			a1:
			res[count]=r1;
			res[count+1]=r2;
			count+=2;
	}
	for(int i=0;i<count;i+=2)
	{
		cout<<"Case #"<<(i/2)+1<<": "<<res[i]<<" "<<res[i+1]<<endl;
	}
	getch();
	getch();
}
