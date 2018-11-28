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
		cin>>k;
		
		c=0;
		
		len=str.length();
		pos=99999;
		
		for(i=0;i<len;i++)
		{
			if(str[i]=='+')
			continue;
	
			if((i+k-1)<len)
			{
				flag=0;
				prev=pos;
				
			for(j=i;j<(i+k);j++)
			{
				if(str[j]=='-')
				{
					str[j]='+';
				}
				else
				{
					pos=min(pos,j);
					flag=1;
					str[j]='-';
				}
			}
			if(flag==0)
			i=j-1;
			else
			i=pos-1;
			
			
			c++;
			
			if(pos==99999)
			pos=min(prev,pos);
			
			//cout<<"pos="<<pos<<"\n";
		}
		
	}
	
	//cout<<"string="<<str<<"\n";
	
	//cout<<"pos="<<pos<<"\n";
	
	flag=0;
	
	for(i=0;i<len;i++)
	{
		if(str[i]=='-')
		{
			flag=1;
			break;
		}
	}
	
	//pos=pos+k-1;
	
	cout<<"Case #"<<x<<": ";
	
	if(flag)
	{
		cout<<"IMPOSSIBLE\n";
	}
	else
	{
		cout<<c<<"\n";
	}
	
	x++;
}

return 0;
}