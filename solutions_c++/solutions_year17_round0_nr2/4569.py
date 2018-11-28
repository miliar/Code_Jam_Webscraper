#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,a1=0;
	cin>>t;
	while(a1<t)
	{
		string n,k;
		cin>>n;
		k=n;		
		a1++;
		int i=0;
		
		{
			while(n[i+1]>=n[i] && i<n.size()-1)
			{
				i++;
			}
			if(i==n.size()-1)
				k=n;
			else if(i){
			
				int j=i;
				while(n[j]==n[j-1] && j>0)
				{
					j--;
				}		
				for(int s=0;s<j;s++)
				{
					k[s]=n[s];
				}	
				k[j]=n[j]-1;
				for(int s=j+1;s<n.size();s++)
				{
					k[s]='9';
				}
			}
			else
			{
				k[0]=n[0]-1;
				
				for(int s=1;s<n.size();s++)
				{
					k[s]='9';
				}
			}
		}
		if(k[0]=='0')
		{
			k[0]='9';
			int o=k.size()-1;
			k[o]='\0';
		}
		cout<<"CASE #"<<a1<<": "<<k<<endl;

	}
	
	return 0;
}
