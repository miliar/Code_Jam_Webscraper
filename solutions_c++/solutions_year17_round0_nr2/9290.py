/*This code is a copyright of princess23*/
/*Write the name of the program*/
#include<bits/stdc++.h>
using namespace std;
vector<int> v1;
int main()
{
	freopen("f1.txt","r",stdin);
freopen("f2.txt","w",stdout);
long long t,n,num,i,j,k;
cin>>t;
vector<int>::iterator it;
for(k=1;k<=t;k++)
{
	cin>>num;
	while(1)
	{
	v1.clear();
    n=num;
	while(n!=0)
	{
		v1.push_back(n%10);
	     n=n/10;
	}
	n=v1.size();
	j=1;
	while(j<n)
	{
		if(v1[j-1]>=v1[j])
		  j++;
		  else
		  break;
	}
	if(j<n)
	num=num-1;
	else
	break;
    }
 cout<<"Case #"<<k<<": "<<num<<endl;
}
return 0;
}

