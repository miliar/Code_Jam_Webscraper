#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MS(a) memset(a,0,sizeof(a))
#define MP make_pair
#define PB push_back
const int INF = 0x3f3f3f3f;
const ll INFLL = 0x3f3f3f3f3f3f3f3fLL;
inline ll read(){
    ll x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
//////////////////////////////////////////////////////////////////////////
const int maxn = 1e5+10;

char s[1005];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T = read();
	for(int cas=1; cas<=T; cas++){
		int k,ans=0;
		cin >> s >> k;
		int len = strlen(s);
		for(int i=0; i<len; i++){
			if(s[i] == '-'){
				if(i+k > len) continue;
				int j;
				for(j=i; j<len; j++){
					if(j-i < k){
						if(s[j] == '-') s[j] = '+';
						else s[j] = '-';
					}else break;
				}
				ans++;
			}
		}
		bool f = 1;
		for(int i=0; i<len; i++) if(s[i]=='-') f=0;
		printf("Case #%d: ",cas);
		if(f) printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}

    return 0;
}
