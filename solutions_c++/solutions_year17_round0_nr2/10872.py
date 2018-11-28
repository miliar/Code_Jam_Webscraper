#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n;
		cin>>n;
		while(n>0)
		{   int temp=n; 
			int tidy=0;
			vector <int> v;
			while(temp>0)
			{	
				v.push_back(temp%10);
				temp/=10;
			}
            
            for(int i=0,len=v.size();i<len;i++)
            {
            	for(int j=i+1;j<len;j++)
            	{
            		if(v[i]<v[j]) 
            		{
            			tidy=1;
            			break;
            		}
            	}
            	if(tidy==1) break;
            }
			if(tidy==0) 
			{
			    cout<<"Case #"<<k<<": "<<n<<endl;
		        break;
		    }
			else 
			    n--;
		}
	}
	return 0;
}