#include <bits/stdc++.h>
using namespace std;
string s;

int main()
{
	int t;
	scanf("%d",&t);
	for (int asd=1;asd<=t;asd++){
		cin>>s;
		long long ans=0;
		if (s[0]>1) ans=s[0]-'1';
		for (int i=0;i<s.size()-1;i++){
			ans*=10;
			ans+=9;
		}
		long long cur=0;
		for (int i=1;i<s.size();i++){
			if (s[i]<s[i-1]) break;
			cur*=10;
			cur+=s[i-1]-'0';
			if (i==s.size()-1) ans=cur*10+s[i]-'0';
			if (s[i]>s[i-1]){
				long long tmp=cur;
				tmp*=10;
				tmp+=s[i]-'1';
				for (int j=i+1;j<s.size();j++){
					tmp*=10;
					tmp+=9;
				}
				ans=max(ans,tmp);
			}
		}
		ans=max(ans,(long long)s[0]-'0');
		printf("Case #%d: %lld\n",asd,ans);
	}
}