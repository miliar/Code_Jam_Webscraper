#include<bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t,n;
	string s;
	int k,ans,flag,cc,i,j;
	cin>>t;
	for(cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": ";
		ans=0;
		flag=0;
		s.clear();
			
		cin>>s>>k;
		n=s.length();
		for(i=0;i<=n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(j=i;j<i+k;j++){
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}

		for(i=0;i<n;i++){
			if(s[i]=='-'){
				flag=1;
				break;
			}
		}

		if(flag==1){
			cout<<"IMPOSSIBLE\n";
		}	
		else{
			cout<<ans<<endl;
		}
	}	
	

	return 0;
}
