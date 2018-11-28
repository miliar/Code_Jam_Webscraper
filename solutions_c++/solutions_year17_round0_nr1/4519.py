#include <bits/stdc++.h>
#define max 1000000

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    freopen("l117.in","r",stdin);
	freopen("lo117.out","w",stdout);

	int t;
	cin>>t;
	for(int u=1;u<=t;u++){
		
		string str;
		int l,k;
		cin>>str>>k;
		l=str.size();
		bool flag=0;
		int i,ans=0;
		for(i=0;i<=l-k;i++){
			
			if(str[i]=='-'){
				
				ans++;
				for(int j=i;j<i+k;j++)
				{
					if(str[j]=='-')
						str[j]='+';
					else
						str[j]='-';
				}
				
			}
					
		}
		
		for(;i<l;i++){
			if(str[i]!='+')
				break;
		}
		cout<<"Case #"<<u;
		if(i==l){
			
			cout<<": "<<ans<<"\n";
			
		}
		else
			cout<<": IMPOSSIBLE\n";
		
	}
	

	return 0;
}
