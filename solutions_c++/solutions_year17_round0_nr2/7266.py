#include<bits/stdc++.h>
using namespace std;
long long ans;

void dfs(string s, int p,long long cur, long long z, int prev){
	if(z>cur)return;
	if(p==s.size()){
		if(z>ans)ans=z;
		return;
	}
	long long int t1, t2;
	cur=cur*10+s[p]-'0';
	p++;
	for(int i=prev;i<=9;i++){
		t1=z*10+i;
		dfs(s, p, cur, t1, i);
	}
	return;
}

int main(int argc, char const *argv[])
{
	freopen("input2large.in", "r", stdin);
	freopen("output2large.in", "w", stdout);
	int n, c=1;
	string s;
	long long int num;
	cin>>n;
	
	getchar();
	while(n--){
		ans=0;
		cin>>s;
		for (int i = 1; i < s.size(); ++i)
		{
			ans=ans*10+9;
		}
		dfs(s, 0, 0, 0, 0);
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}