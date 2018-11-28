#include <bits/stdc++.h>

using namespace std;

#define LL long long

int Test;
LL N, K;

map <LL, LL> Hash;
map <LL, LL> :: iterator cp;


int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%I64d%I64d", &N, &K);
		Hash.clear();
		Hash[N] = 1;
		printf("Case #%d: ", tt);
		while (1){
			cp = Hash.end();
			cp--;
			if (cp->second >= K){
				printf("%I64d ", cp -> first / 2);
				printf("%I64d\n", (cp -> first - 1) / 2);
				break;
			}
			K -= cp -> second;
			Hash[(cp -> first - 1) / 2] += cp -> second;
			Hash[cp -> first / 2] += cp -> second;
			Hash.erase(cp);
		}
	}
}