#include<bits/stdc++.h>
using namespace std;
string str;
int main()
{
	ifstream cin("gcj_2l.in");
	ofstream cout("gdc_2lo.txt");
	
	long long int i,j,k,l,m,n,id=1,t,ans;
	char c;
	cin>>t;
	
	while(t--)
	{
        str="";		
		cin>>n;
	
		if(n<10)
		{
			//cout<<str<<endl;
		
			c='0'+n;	
			str=c+str;
			l=1;	
		}
		else
		{
			//cout<<n<<endl;
			while(n)
			{
				c='0'+n%10;
				str=c+str;
				n/=10LL;
			}	
			
			l=str.length();
			for(i=l-2;i>=0;i--)
			{
				if(str[i]>str[i+1])
				{
					if(str[i]!='0')
					 {
					 	str[i]--;
					 	for(j=i+1;j<l;j++)
					 	str[j]='9';
					 }
					 else
					 {
					 	j=i;
					 	while(str[j]=='0')
					 	 j--;
					 	 str[j]--;
					 	 j++;
					 	 for(;j<l;j++)
					 	 str[j]='9';
					 	 
					 	
					 }
					
				}
			}
			
			
		}   
			
		i=0;
		while(str[i]=='0')
		i++;	
	    
		cout<<"Case #"<<id++<<": ";
		for(;i<l;i++)
		cout<<str[i];
		cout<<endl;
	}
	
}
