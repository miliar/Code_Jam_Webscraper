#include<bits/stdc++.h>
using namespace std;


int main()
{
	int flag;
	string X;
	int t;

	long long int k=0;
	long long int n;

    cin>>t;
	while(t--)
	{
		k++;
		cin>>X;

		cin>>n;

		long long int len=X.size();

         long long int ans=0,j;


		for(long long int i=0;i<len-n+1;i++)
		{
			if(X[i]=='-')
			{
				ans++;
			for(j=i;j<i+n;j++)
			{
				if(X[j]=='-')
				X[j]='+';
			   else if(X[j]=='+')
			   	X[j]='-';
				
			}
			//printf("%lld \n",j);
			
		  }

		  
		}
         
         flag=0;
       for(long long int i=0;i<len;i++)
		{
			if(X[i]=='-')
				flag=1;
		}

		//cout<<X<<endl;
		if(flag==0)
			printf("Case #%lld: %lld\n",k,ans);
		else
			printf("Case #%lld: IMPOSSIBLE\n",k);
	}

	return 0;
}