#include<iostream>
#include<stdio.h>
using namespace std;
int main() {
	freopen("q1.in","r",stdin);
	freopen("q1.out","w",stdout);
  int p,c,j,t,k,count=0,m,u;
  cin >> t; 
  for (int i = 1; i <= t; ++i) {
  u=0;
  	count=0;
  	char a[1005]={},l;
  	for(j=0;;++j)
  	{
  		scanf("%c",&l);
  		if(l!=' ')
  		{
  			a[j]=l;
  		}
  		else
  		{
  		break;
  		}
  	}
  	cin>>k;
  	for(m=0;m<j-k+1;m++)
  	{
  		if(a[m]=='-')
  		{
  			for(int w=m;w<k+m;w++)
  			{
  				if(a[w]=='+')
  				{
  					a[w]='-';
  				}
  				else
  				{
  					a[w]='+';
  				}
  			}
  			count++;
  		}
  	}
  	p=0;
  	c=0;
  	for(m=0;m<j;m++)
	{
  	if(a[m]=='-')
  	{
  	u=1;
  	break;
  	}
  	}
  	if(u==0)
  	{
  		cout << "Case #" << i << ": " <<count<<endl;
  	}
  	else
  	{
  		cout << "Case #" << i << ": " <<"IMPOSSIBLE"<<endl;
  	}
  }
  return 0;
}
