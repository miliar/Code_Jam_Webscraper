#include<bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin>>T;
	
	for(int t=1;t<=T;t++){
		
		string s;
		cin>>s;
		
		int k;
		cin>>k;
		
		int ans = 0;
		
		for(int i=0;i<((int)s.length()-k+1);i++){
			
			if(s[i]=='+')
				continue;
			
			for(int j=i;j<i+k;j++)
			{
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		
			ans++;
		}
		
		//cout<<s<<'\n';
		
		for(int i=0;i<(int)s.length();i++)
		{
			if(s[i] == '-')
			{
				ans = -1;
				break;
			}
		}
		
		if(ans == -1){
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		}
		else
			cout<<"Case #"<<t<<": "<<ans<<"\n";
			
	}
	
	return 0;
}
