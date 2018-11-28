#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T,N,K;
string S;

int main()
{
	cin >> T;
	FOR(testCase,1,T + 1){
		cin >> S >> K;
		N = S.size();
		int ans = 0;
		FOR(i,0,N - K + 1){
			if(S [i] == '-'){
				FOR(j,i,i + K){
					if(S [j] == '+'){
						S [j] = '-';
					}
					else{
						S [j] = '+';
					}
				}
				ans++;
			}
		}
		if(count(ALL(S),'-')){
			printf("Case #%d: IMPOSSIBLE\n",testCase);
		}
		else{
			printf("Case #%d: %d\n",testCase,ans);
		}
	}

	return 0;
}
