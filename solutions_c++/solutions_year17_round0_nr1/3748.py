#include<bits/stdc++.h>
using namespace std;

int ar[1005];
int ch[1005];
int nxt[1005];

int sol(int n,int tr){
	int cnt=0;
	for(int i=1;i<=n;i++){
		int x=ch[i];
	//	cout<<i<<" "<<ar[i]<<" "<<ch[i]<<endl;
		//if(nxt[i-1]==0) x=0;
		if((x+ar[i])%2==0){
			cnt++;
			int lm=i+tr-1;
			if(lm>n) return -1;
			for(int j=i;j<=lm;j++)
				ch[j]++;
		}
	}
	return cnt;
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("out1.txt","w",stdout);
	long long t;
	cin>>t;
	for(long long qq=1;qq<=t;qq++){
		string s;
		cin>>s;
		int sz=s.size();
		for(int i=0;i<sz;i++){
			if(s[i]=='-') ar[i+1]=0;
			else ar[i+1]=1;
		}
	//	for(int i=1;i<=sz;i++) cout<<ar[i]<<" ";
	//	cout<<endl;
	//	cout<<s<<endl;
		int tr;
		cin>>tr;
		printf("Case #%d: ",qq);
		memset(ch,0,sizeof(ch));
		memset(nxt,0,sizeof(nxt));
		int ans=sol(sz,tr);
		if(ans==-1) cout<<"IMPOSSIBLE\n";
		else{
			cout<<ans<<endl;
		}
	}
}
