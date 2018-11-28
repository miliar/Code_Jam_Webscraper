#include<iostream>
using namespace std;
int main()
{
	int test;
	int n;
	int j=0,i,d;
	cin>>test;
	while(test--)
	{j++;
	cin>>n;
	int k;
	for(i=n;i>=0;i--)
	{k=i;d=3;
	int a[4]={0};
	while(k)
	{a[d--]=k%10;
	k/=10;
	}
	int c=0;
	for(int t=0;t<3;t++)
if(a[t]<=a[t+1])
c++;
if(c==3)
{

cout<<"Case #"<<j<<": "<<i<<endl;
break;
}
}

}
	return 0;
}
