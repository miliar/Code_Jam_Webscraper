#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair

using namespace std;


int main()
{
	 int t,n,i,k,len,j,pos,maxm,it,c,p,jp,x,prev;
	
	
	cin>>t;
	
	string str;
	bool flag;
	
	x=1;
	
	while(t--)
	{
		cin>>str;
		
		len=str.length();
		
		pos=-1;
		
		cout<<"Case #"<<x<<": ";
		
		for(i=1;i<len;i++)
		{
			if(str[i]>=str[i-1])
			continue;
			
			pos=i-1;
			p=i;
			break;
		}
		
		if(pos!=-1)
		{
			
			if(str[p]=='0')
			{
				bool fl=0;
				
				if(str[pos]=='1')
				{
					for(j=pos;j>=0;j--)
					{
						str[j]='9';
					}
				}
				else
				{
					j=pos-1;
					while(str[j]==str[j+1] && j>=0)
					{
						j--;
					}
					j++;
					p=j+1;
					str[j]=str[j]-1;
				for(j=p-2;j>=0;j--)
		       {
		       	  
			if(str[j]>str[j+1])
			{
				
					str[j]=str[j+1];
			}
			else
			break;
			
		      }
		  }
		
		for(i=p;i<len;i++)
		str[i]='9';
		
		if(str[p-1]=='9')
		{
			for(i=1;i<len;i++)
        	cout<<str[i];
		}
		else
		{
			for(i=0;i<len;i++)
	        cout<<str[i];
		}
		
		}
		else
		{
			bool fl=0;
			j=pos-1;
					while(str[j]==str[j+1] && j>=0)
					{
						j--;
					}
					j++;
					p=j+1;
					str[j]=str[j]-1;
		for(j=p-2;j>=0;j--)
		{
	
			if(str[j]>str[j+1])
			{
				str[j]=str[j+1];
			}
			else
			break;
			
		}
		
		for(i=p;i<len;i++)
		str[i]='9';
		
		pos=0;
		
		for(i=0;i<len;i++)
		{
			if(str[i]=='0')
			continue;
			else
			{
				pos=i;
				break;
			}
		}
	
	
	
	for(i=pos;i<len;i++)
	cout<<str[i];
}
	
    }
    else
    {
    	for(i=0;i<len;i++)
	    cout<<str[i];
	}
	
	cout<<"\n";
	
	x++;
}

return 0;
}