#include<bits/stdc++.h>
using namespace std;
bool dir[1000];
int f[1000];
int main(){
	int t;
	cin>>t;
	for(int times=0;times<t;times++){
		memset(dir,0,sizeof(dir));
		memset(f,0,sizeof(f));
		string s;
		int k,n;
		cin>>s>>k;
		n=(int)s.size();
		for(int i=0;i<n;i++){
			if(s[i]=='-')dir[i]=1;
			else{
				dir[i]=0;
			}
		}
		
		int ans=0,sum=0;
		for(int i=0;i+k<=n;i++){
			if((dir[i]+sum)%2!=0){
				ans++;
				f[i]=1;
			}
			sum+=f[i];
			if(i-k+1>=0){
				sum-=f[i-k+1];
			}
		}
		
		bool possible=true;
		for(int i=n-k+1;i<n;i++){
			if((dir[i]+sum)%2!=0){
				possible=false;
				break;
			}
			if(i-k+1>=0){
				sum-=f[i-k+1];
			}
		}
		
		cout<<"Case #"<<times+1<<": ";
		if(possible){
			cout<<ans;
		}
		else{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
	return 0;
}

