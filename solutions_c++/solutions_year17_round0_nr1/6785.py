#include <bits/stdc++.h>
using namespace std;

#define ri(x) scanf("%d",&x)
#define rii(x,y) scanf("%d %d",&x,&y)
#define riii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define FOR(i,j,k) for(int i = j; i<k; i++)
#define ROF(i,j,k) for(int i = j; i>=k; i--)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define pb push_back
string S;
int K;
char invert(char c){return c == '-' ? '+' : '-';}
int main(){
	int T;ri(T);for(int t = 1; t<=T; t++){
		printf("Case #%d: ",t);
		cin >> S >> K;
		int N = S.size();
		int ans = 0;
		for(int i = 0; i+K-1<N; i++){
			if(S[i] == '-'){
				for(int j = 0; j<K; j++) S[i+j] = invert(S[i+j]);
				ans++;
			}
		}
		bool can = true;
		for(int i = 0; i<N; i++) if(S[i] == '-') {printf("IMPOSSIBLE\n");can = false;break;}
		if(can) printf("%d\n",ans);
	}
}
