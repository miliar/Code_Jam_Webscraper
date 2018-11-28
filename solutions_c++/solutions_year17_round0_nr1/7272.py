#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	freopen("input1large.in", "r", stdin);
	freopen("output1large.in", "w", stdout);
	string s;
	int n,k, c=1;
	cin>>n;
	getchar();
	while(n--){
		cin>>s>>k;
		getchar();
		int ans=0;
		vector<int> a(s.size(), 0);
		for (int i = 0; i < s.size(); ++i)
		{
			if(s[i]=='+')a[i]=1;
		}
		for (int i = 0; i <= s.size()-k; ++i)
		{
			if(a[i]==0){
				ans++;
				for(int j=i;j<i+k;j++){
					a[j]=1-a[j];
				}
			}
		}
		int flag=1;
		for(int i=s.size()-k;i<s.size();i++){
			if(a[i]==0){
				flag=0;
				break;
			}
		}
		
		cout<<"Case #"<<c<<": ";
		c++;
		if(flag){
			cout<<ans<<endl;
		}
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}