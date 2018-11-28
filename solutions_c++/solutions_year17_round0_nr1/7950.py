#include<bits/stdc++.h>
using namespace std ;

int min1 =0 ;

int main()
{
	freopen("A-large.in","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	
	int t ,c;
	cin>>t ;
	c=1; 
	while(t--)
	{
		string s ;
		
		int n , flag = 0;
		 min1= 0 ;
		 
		cin>>s;
		cin>>n;
		
		for(int i=0;i<s.size();i++)
		{
			if(s[i] == '-')
			{
				//cout<<i<<"\n";
				if(i+n-1 >= s.size())
				{
					flag =1 ;
					break ;
				}
				for(int j=i;j<i+n;j++)
					{
						if(s[j] == '+')
						s[j] = '-' ;
						else
						s[j] ='+' ;
					}
					
					min1++ ;
			}
		}
		if(flag!=1)
		printf("Case #%d: %d\n",c,min1);
		else
		printf("Case #%d: IMPOSSIBLE\n",c) ; 
		c++ ;
	}
}
