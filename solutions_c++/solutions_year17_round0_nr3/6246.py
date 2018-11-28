#include<iostream>
#include<iomanip>
#include<cstring>
#include<cmath>
using namespace std;
int main()
{
	freopen("C-small-2-attempt1.in","rt",stdin);
  	freopen("out2.txt","wt",stdout);
	long long t,n,k,i,j,count,rem,size,sum,s,max,min,val;
	int flg,f;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		count=0;
		for(j=0;j<k;)
		{
			j+=pow(2,count);
			count+=1;
		}
		rem=n-pow(2,count)+1;
		if(rem<0)	rem=0;
		size=pow(2,count);
		val=rem/size;
		rem%=size;
		s=k-pow(2,count-1)+1;
		if(s<=rem)
			cout<<val+1<<" ";
		else
			cout<<val<<" ";
		rem-=size/2;
		if(rem<0)	rem=0;
		if(s<=rem)
			cout<<val+1<<endl;
		else
			cout<<val<<endl;
	}
	return 0;
}






		

