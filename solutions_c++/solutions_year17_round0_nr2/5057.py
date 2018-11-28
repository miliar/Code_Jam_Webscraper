#include<bits/stdc++.h>
using namespace std;
typedef long long ll; 
const int maxn=20;
int d[maxn],c[maxn],len;
bool flag;

void init(ll n){
	len=0;
	while(n>0){
		d[len++]=n%10;
		n/=10;
	}
}


void dfs(int dep,bool ok,int last){
	//cout<<dep<<" "<<ok<<" "<<last<<endl;
	if(dep==len)flag=1;
	if(flag)return ;
	int Max=ok?d[len-dep-1]:9;
	for(int i=Max;i>=last&&!flag;i--)
		c[dep]=i,dfs(dep+1,ok&&i==d[len-dep-1],i);
}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large-out","w",stdout);
	int t,cas=1;ll n;
	cin>>t;
	while(t--){
		cin>>n;
		flag=0;
		init(n);	
		dfs(0,1,0);
		int i=0;
		printf("Case #%d: ",cas++);
		while(c[i]==0)i++;
		for(;i<len;i++)putchar('0'+c[i]);
		cout<<endl;
	}
	return 0;
}