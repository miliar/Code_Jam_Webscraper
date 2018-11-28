#include <iostream>
#include<cstdio>
#include<algorithm>
#include <iomanip>
using namespace std;
#include <bits/stdc++.h>

int main() {
     long long a,b,c,i,j,x,m,k,z,T,arr[100];
    scanf("%lld", &T);
    for (int k=0;k<T;k++) {
        fprintf(stderr, "test %lld\n", k+1);
        cin>>a;
        j=0;
        z=a;
        while(a>0)
        {
        	arr[j++]=a%10;
        	a=a/10;
		}
		//cout<<j;
		for(i=j-2;i>=0;i--)
		{
			if(arr[i]>=arr[i+1])
			{
				continue;
			}
			else
			{
				x=arr[i+1];
				c=i+2;
				while(arr[c]==x && c<j)
				{
					c++;
				}
				c--;
				arr[c]--;
				for(m=0;m<c;m++)
				{
					arr[m]=9;
				}
			}
		}
		cout<<"Case #"<<k+1<<": ";
		for(i=j-1;i>=0;i--)
		{
			if(arr[i]==0)
			continue;
			cout<<arr[i];
		}
		cout<<"\n";
    }
}

