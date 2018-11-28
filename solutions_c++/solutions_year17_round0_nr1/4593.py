#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define pb push_back
#define vint vector<int>

int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt", "w", stdout);

	string s;
	int n,m,k,t,i,j,l,ans;
	sd(t);
	for(n=1;n<=t;n++){
		cin>>s;
		ans=0;
		l = s.size();
		sd(m);
		for(i=0;i<l-m+1;i++){
			if(s[i]=='-'){
				for(j=i;j<i+m;j++){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
				ans++;
			}
		}
		for(i=l-m+1;i<l;i++){
			if(s[i]=='-')
				ans=-1;
		}
		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n",n);
		else
			printf("Case #%d: %d\n",n,ans);
	}

	return 0;
}