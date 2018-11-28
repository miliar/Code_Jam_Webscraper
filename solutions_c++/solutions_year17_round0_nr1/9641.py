//code Jam (A)

#include<bits/stdc++.h>

using namespace std;

int t,k,ans,sz,flag;
string s;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>t;
	
	for(int m=1;m<=t;m++){
		flag=0;
		ans=0;
		cin>>s>>k;
		sz=s.size();
		for(int i=0;i<sz;i++){
			if(s[i]=='-' && i<=sz-k){
				ans++;
				for(int j=i;j<k+i;j++)
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
			}else if(s[i]=='+'){
				continue;
			}else{
				flag=1;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<m<<": "<<ans<<endl;
	}
	return 0;
}










































	































