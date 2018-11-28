#include <bits/stdc++.h>
#define fore(i,a,n) for(int i=a,qwer=n;i<qwer;i++)
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

char s[1024];
int n,m;

int main() {
	int tn;
	scanf("%d",&tn);
	fore(tc,0,tn) {
		scanf("%s%d",s,&m);
		n=strlen(s);
		int ans=0;
		fore(i,0,n)
			if(s[i]=='-') {
				if(i+m>n) break;
				ans++;
				fore(j,i,i+m) s[j]=(s[j]=='-'?'+':'-');
			}
		bool f=1;
		fore(i,0,n) if(s[i]=='-') f=0;
		if(f) printf("Case #%d: %d\n",tc+1,ans);
		else printf("Case #%d: IMPOSSIBLE\n",tc+1);
	}	
}
