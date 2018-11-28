#include <iostream>
#include<bits/stdc++.h>
#include<vector>
#include<math.h>
using namespace std;

int main()
{
	int c,i2,j2,r,i,l,pre,p,d1,k,j,t,n;
int md,mx,ms,s,a[1000][2];
double d,time[1000],mnt;
scanf("%d",&t);
int x1=1;
while(t--)
{
md=INT_MAX;
ms=INT_MAX;
mx=INT_MIN;
cin>>d>>n;

for(i=0;i<n;i++)
{
cin>>a[i][0]>>a[i][1];
time[i]=(float)(d-a[i][0])/a[i][1];
}

mnt=INT_MIN;



for(i=0;i<n;i++)
{

if(time[i]>mnt)
mnt=time[i];
}
cout<<fixed;
cout<<"Case #"<<x1<<": "<<setprecision(6)<<d/mnt<<"\n";



	    
x1++;

}
	return 0;
}
