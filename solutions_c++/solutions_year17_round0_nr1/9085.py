//editor: Jan Tang
//problem:
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <cstdlib>
using namespace std;
#define set0(a) memset(a,0,sizeof(a));
#define CIN(a,n) for(int i=1;i<=n;i++) cin>>a[i];
typedef long long ll;
typedef unsigned long long ull;
const int Mod = 1e9+7;
const int maxn = 1005;
const int inf = 0x3f3f3f3f;
int m,n,t;
char s[maxn];
/*==============================head==========================*/
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);	
	scanf("%d",&n);
	for(int knt = 1; knt <= n; knt++){
		scanf("%s%d",s+1,&t);
		int len = strlen(s+1);
		int ans = 0;
		for(int i = t; i <= len; i++){
//			cout<<i<<endl;
			if(s[i-t+1]=='-'){
				ans++;
				for(int j = i-t+1;j<=i;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		int f=1;
		printf("Case #%d: ", knt);
		for(int i = 1; i <=len;i++){
			if(s[i]=='-')f=0;
		}
		if(f)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}