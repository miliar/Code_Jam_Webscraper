#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
char s[50];
char ans[50];
int n,tc;
bool rec(int i,bool is) {
	if (i==n) return 1;
	if (!is) {
		ans[i]='9';
		return rec(i+1,0);
	} else {
		for (char c=s[i];c>=((i==0)?'0':ans[i-1]);c--) {
			ans[i]=c;
			if (rec(i+1,(c==s[i]))) return 1;
		}
		return 0;
	}
}
int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%s",s);
		n=strlen(s);
		memset(ans,0,sizeof(ans));
		rec(0,1);
		int x=0;
		for (int i=0;i<n;i++) {
			if (ans[i]=='0') x=i+1;
		}
		printf("Case #%d: %s\n", kk,ans+x);
	}
}