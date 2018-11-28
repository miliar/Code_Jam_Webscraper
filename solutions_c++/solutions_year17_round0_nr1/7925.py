#include<bits/stdc++.h>

using namespace std;

#define ll 							long long
#define boost 						ios_base::sync_with_stdio(false); //to synchronize the input of cin and scanf
#define fileio 						freopen("in.in","r",stdin); freopen("out.txt","w",stdout);
#define inf 	0x7fffffff
ll t,i,j,ans,r,c,m,n,k,u,v;
int main(){
	fileio
	cin>>t;
	for(u=1;u<=t;u++){
		string s,m;
		cin>>s>>k;
		n = s.length();
		m=s;
		r=0;
		for(i=0;i<=n-k;i++){
			if(s[i]=='-'){
				r++;
				for(j=0;j<k;j++){
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
			}
		}
		c=0;
		for(i=n-1;i>=k-1;i--){
			if(m[i]=='-'){
				c++;
				for(j=0;j<k;j++){
					if(m[i-j]=='-')
						m[i-j]='+';
					else
						m[i-j]='-';
				}
			}
		}
		v=0;
		for(i=0;i<n;i++){
			if(s[i]=='-'){
				v=1;
				break;
			}
		}
		if(v==1)r=inf;
		ans=0;
		for(i=0;i<n;i++){
			if(m[i]=='-'){
				ans=1;
				break;
			}
		}
		if(ans==1)c=inf;
		if(v==1 && ans==1)
			cout<<"Case #"<<u<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<u<<": "<<min(r,c)<<endl;
	}
	return 0;
}
