#include <iostream>
#include<bits/stdc++.h>
#include<vector>
#include<math.h>
using namespace std;

int main()
{
	int i,l,pre,p,d1,k,j,t,a[30],x;
string n;

	scanf("%d",&t);
x=1;
while(t--)
{
cin>>n;
l=n.size();
for(i=l-2;i>=0;i--)
{
if(n[i]<=n[i+1])
continue;
else
{
n[i]=n[i]-1;
for(j=i+1;j<l;j++)
n[j]='9';

}

}
for(i=0;i<l;i++)
{
if(n[i]!='0')
break;

}
printf("Case #%d: ",x);
for(j=i;j<l;j++)
cout<<n[j];
//printf("Case #%d: %lld",x,i);
printf("\n");
	    
x++;

}
	return 0;
}
