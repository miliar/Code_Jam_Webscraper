#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
using namespace std;
 
long long int n,k,num,temp;
long long int dp[100],f[100];
int main()
{
	int t,i;
	cin >> t;
	for(i=1;i<=t;i++)
	{
		cin >> n >> k ;
		int count=-1;
		f[0]=n/2;
		if(n%2==0){dp[0]=1;}
		else{dp[0]=2;}
		num=k;
		while(num!=0)
		{
			num=num/2;
			count++;
		}
		for(int j=0;j<count;j++)
		{
			if(f[j]%2==0){dp[j+1]=dp[j];}
			else{ dp[j+1]=dp[j] + pow(2,j+1);}
			f[j+1]=f[j]/2;
		}
		if(dp[count] >= k+1){cout << "Case #" << i << ": " << f[count] << " " << f[count] << endl;}
		else if ( dp[count] < k + 1 - pow(2,count)){cout << "Case #" << i << ": " << f[count]-1 << " " << f[count]-1 << endl;}
		else{cout << "Case #" << i << ": " <<f[count]  << " " << f[count]-1 << endl;}
	}
	return 0;
}