#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		char S[1024];
		int K;
		scanf("%s%d", S, &K);
                int N=strlen(S);
                int flipCnt=0;
		for (int i=0; i<=N-K; i++) {
                    if (S[i]=='-') {
                        flipCnt++;
                        for (int j=i; j<i+K; j++) S[j]=( (S[j]=='-')?'+':'-');
                    }
		}
		for (int i=N-K+1; i<N; i++) {
                    if (S[i]=='-') flipCnt=-1;
                }
		if (flipCnt==-1) printf("Case #%d: %s\n", t, "IMPOSSIBLE");
		else printf("Case #%d: %d\n", t, flipCnt);
	}
	return 0;
}
