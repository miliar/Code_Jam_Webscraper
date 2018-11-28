#include <bits/stdc++.h>
using namespace std;
int s1[1050];
int s2[1050];
int s3[1050];
int main()
{
	freopen("Input.txt", "r", stdin);
    freopen("Output.out", "w", stdout);
    int t,k,i,j,cas=0;
    long long int n;
    string s;
    scanf("%d",&t);
    while(t--)
    {
    cas++;
    cin>>s;

    int k=s.length();
    for(i=0;i<s.length();i++)
    {
    	s1[i]=s[i]-'0';
    	s2[i]=s1[i];
    }
    for(i=k-2;i>=0;i--)
	    { 
	  		if(s1[i]>s1[i+1])
	  		{
	  			for(j=i+1;j<k;j++)
	  				s1[j]=9;
	  			s1[i]=s1[i]-1;
	   		}

	    }
	      
	printf("Case #%d: ",cas);
	int flag1=0;
	for(i=0;i<=k-1;i++)
	{
		if((s1[i]==0)&&(flag1==0))
			continue;
		else
		{
			flag1=1;
			printf("%d",s1[i]);
		}

	}
	printf("\n");    
    }
    
}