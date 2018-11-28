#include<bits/stdc++.h>
using namespace std;



long long int func(long long int x)
{
 	long long int nm[20];
	long long int p,n,res=0;
	int cnt=0;
	int flag=0;
	long long int zz=0;
	while(x)
	{
		nm[cnt++]=x%10;
		x/=10;
	}
	for(int j=0;j<cnt;++j){
	for(int i=cnt-2;i>=0;--i)
	{
		if(flag==0 && nm[i+1]>nm[i])
		{
			nm[i+1]--;
			flag=1;
	
		}
		if(flag==1)
		nm[i]=9;
	}
   flag=0;
    }
	
	
	
	
	for(int i=cnt-1;i>=0;--i)
	{
		res=res*10 + nm[i];
	}
return res;
	
}

int main()
{
	
	freopen("file.txt", "r", stdin);
    freopen("file1.txt", "w", stdout);
	int t;
	long long int n;
	cin>>t;
	for(int T=1;T<=t;++T)
	{
		printf("Case #%d: ",T);
		cin>>n;
		printf("%lld\n",func(n));
		
	}
	return 0;
	
}
