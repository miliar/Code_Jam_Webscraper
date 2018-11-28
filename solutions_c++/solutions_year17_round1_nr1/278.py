#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T,N,M;

int main()
{
	cin >> T;
	FOR(testCase,1,T + 1){
		cin >> N >> M;
		vector<string> S(N);
		FOR(i,0,N){
			cin >> S [i];
		}
		FOR(i,0,N) FOR(j,1,M){
			if(S [i] [j] == '?'){
				S [i] [j] = S [i] [j - 1];
			}
		}
		FOR(i,0,N) for(int j = M - 2;j >= 0;j--){
			if(S [i] [j] == '?'){
				S [i] [j] = S [i] [j + 1];
			}
		}
		FOR(i,1,N) FOR(j,0,M){
			if(S [i] [j] == '?'){
				S [i] [j] = S [i - 1] [j];
			}
		}
		for(int i = N - 2;i >= 0;i--) FOR(j,0,M){
			if(S [i] [j] == '?'){
				S [i] [j] = S [i + 1] [j];
			}
		}
		printf("Case #%d:\n",testCase);
		FOR(i,0,N){
			cout << S [i] << endl;
		}
	}

	return 0;
}
