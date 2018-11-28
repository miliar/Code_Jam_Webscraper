#include<bits/stdc++.h>
using namespace std ;

long long n ;
string s ;
int a[109] ;

int main()
{
	freopen("B-large.in" ,"r",stdin) ;
	freopen("out.txt", "w" ,stdout) ;
	
	int t,c=0 ;
	cin>>t;
	
	while(t--)
	{
	//	v.clear() ;
		cin>>s; 
		c++ ;
		int flag = 0 , check = 0;
		
		for(int i=0;i<s.size()-1;i++)
		{
			if(i!=0 && s[i]!=s[i-1])
				{
					check = i ;
				}
				else if(i == 0) 
				{
					check = i ;
				}
				
			if(s[i] -'0' > s[i+1] - '0')
			{
				a[i] = s[i] - '0' - 1 ;
				for(int j=i+1;j<s.size();j++)
				a[j] = 9 ;
				
				for(int j = check+1 ; j<=i;j++)
				a[j] = 9 ;
				a[check] = s[i] - '0' - 1;  
				flag = 1 ;
				break ;
			}
			  else
			   a[i] = s[i] - '0' ;	
			
			
		}
		
		if(flag == 0)
		a[s.size() - 1] = s[s.size() - 1] - '0' ;
		
		int mark =0 ; 
		printf("Case #%d: ",c) ;
		
 		for(int i=0;i<s.size();i++)
		{
			if(mark == 0 && a[i] == 0)
			{
				continue ;
			}
			else if(mark == 0 && a[i]!=0)
			{
				mark = 1 ;
				cout<<a[i]; 
			}
			else if(mark!=0)
			cout<<a[i] ;
		}
		
		cout<<"\n" ;
	}
	
	return 0 ;
}
