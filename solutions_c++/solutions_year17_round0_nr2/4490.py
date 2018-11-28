#include<bits/stdc++.h>
#define mod 1000000007
#define mx 100001
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define ll long long 

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    
	freopen("B-172.in","r",stdin);
	freopen("BO-172.out","w",stdout);
    
	int t;
	cin>>t;
	for(int u=1;u<=t;u++){

		string str,ans="";
		
		cin>>str;
		int l=str.size();
		int i,idx=0,flag=0;
		
		for(i=1;i<l;i++){
			
			if(str[i]>str[idx])
			{
			//	ans += str[i];
				idx=i;
			}
			else if(str[i]<str[idx]){
				
				flag=1;
				break;
				
			}
		
		}
		if(flag){
			
			ans = str.substr(0,idx);
		
			if((idx==0 && str[idx]!='1') || idx)
				ans += (str[idx]-1);
			for(int i=idx+1;i<l;i++)
				ans+='9';
				
			
		}
		else{
			ans = str;
		}
		
		cout<<"Case #"<<u<<": "<<ans<<"\n";
		
	}
	
	return 0;	

}

