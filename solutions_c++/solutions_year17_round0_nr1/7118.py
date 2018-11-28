#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,k,l,f,ans,a=1;
	char s[1010];
	cin>>n;
	while(n--){
		ans=f=0;
		cin>>s>>k;
		l=strlen(s);
		for(int q=0;q<=l-k;++q)
			if(s[q]=='-'){
				ans++;
				for(int w=0;w<k;++w){
					if(s[q+w]=='-')s[q+w]='+';
					else s[q+w]='-';
				}
			}
		for(int q=0;q<l;++q)if(s[q]=='-')f=1;
		cout<<"Case #"<<a++<<": ";
		if(f)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}

