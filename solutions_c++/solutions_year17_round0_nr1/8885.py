#include <bits/stdc++.h>
#define ll long long
#define INF 1000000005
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

typedef pair<int,int>P;

const int MAX_N = 100005;

int ans,n,T,K;
string s;

int main()
{
	scanf("%d",&T);
	rep(t,T){
		cin >> s >> K;
		ans = 0;
		n = s.length();
		rep(i,n-K+1){
			if(s[i] == '-'){
				rep(j,K){
					if(s[i+j] == '+'){
						s[i+j] = '-';
					}else{
						s[i+j] = '+';
					}
				}
				ans++;
			}
		}
		bool flag = true;
		for(int i=n-K+1;i<n;i++){
			if(s[i] == '-'){
				flag = false;
				break;
			}
		}
		if(flag){
			printf("Case #%d: %d\n",t+1,ans);
		}else{
			printf("Case #%d: IMPOSSIBLE\n",t+1);
		}
	}
	return 0;
}
