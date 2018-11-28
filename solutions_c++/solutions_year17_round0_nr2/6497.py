#include <bits/stdc++.h>
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
using namespace std;
typedef pair<int, int> pii;
const ll MOD=1e9+7;
const int N=25;

char s[N];
int main(){
	int t,test,n,i;
	scanf("%d",&test);
	for(t=0;t<test;++t){
		scanf(" %s", s); n=strlen(s);
		for(i=0;i<n;++i)
			if(i<n-1 && s[i]>s[i+1]){
				for(;i>=1 && s[i]==s[i-1]; --i);
				--s[i];
				for(++i;i<n;++i)
					s[i]='9';
				break;
			}
		for(i=0;i<n && s[i]=='0';++i);
		printf("Case #%d: %s\n",t+1,s+i);
	}
	return 0;
}