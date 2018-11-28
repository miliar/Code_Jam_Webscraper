#include<iostream>
#include<algorithm>
using namespace std;
int n,k;
int a[1005];
int main()
{
	int test;
	string s;
	cin>>test;
	for(int index=1;index<=test;++index)
	{
		bool check=false;
		int ans=0;
		cin>>s>>k;
		n=s.length();
		for(int i=1;i<=n;++i){
			if(s[i-1]=='+'){
				a[i]=0;
			}
			else a[i]=1;
		}
		for(int i=1;i<=n-k+1;++i){
			if(a[i]==0) continue;
			else{
				ans++;
				for(int j=i;j<i+k;++j){
					a[j]=1-a[j];
				}
			}
		}
		for(int i=1;i<=n;++i) if(a[i]==1) check=true;
		cout<<"Case #"<<index<<": ";
		if(check) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
