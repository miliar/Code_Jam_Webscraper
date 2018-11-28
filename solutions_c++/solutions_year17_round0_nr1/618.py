#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); i++)
#define FOREACH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define SIZE(v) ((int)(v).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define pii pair<int, int>

int main(){
	int T;
	cin >> T;
	REP(t, T){
		string S;
		int K;
		cin >> S >> K;
		int cnt = 0, len = SIZE(S);
		REP(i, len - K + 1){
			if(S[i] == '-'){
				cnt++;
				REP(j, K){
					S[i + j] = (S[i + j] == '+' ? '-' : '+');
				}
			}
		}
		bool p = true;
		REP(i, len) if(S[i] == '-') p = false;
		printf("Case #%d: ", t + 1);
		if(!p) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
}
