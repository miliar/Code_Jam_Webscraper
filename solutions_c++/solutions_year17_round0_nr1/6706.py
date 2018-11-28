#include <bits/stdc++.h>
#define MAXL 100010
using namespace std;
int t,n;
string s;
int main() {
	//freopen("easy.in","r",stdin);
	//freopen("easy.out","w",stdout);
	scanf("%d",&t);
	for (int k=1;k<=t;k++){
		cin>>s;
		int ans=0,bo=1;
		scanf("%d",&n);
		for (int i=0;i<=s.length()-n;i++)
		if (s[i]=='-'){
			for (int j=i;j<i+n;j++)
			if (s[j]=='-') s[j]='+';
			else s[j]='-';
			ans++;
		}
		for (int i=s.length()-n;i<s.length();i++)
		if (s[i]=='-') bo=0;
		printf("Case #%d: ",k);
		if (bo) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
}
