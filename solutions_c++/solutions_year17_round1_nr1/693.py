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
		int N, M;
                char S[30][30];
		scanf("%d%d", &N, &M);
                for (int n=0; n<N; n++) {
                    scanf("%s", S[n]);
                }
                for (int n=0; n<N; n++) {
                    for (int m=1; m<M; m++) {
                        if (S[n][m]=='?') S[n][m]=S[n][m-1];
                    }
                    for (int m=M-2; m>=0; m--) {
                        if (S[n][m]=='?') S[n][m]=S[n][m+1];
                    }
                }
                for (int m=0; m<M; m++) {
                    for (int n=1; n<N; n++) {
                        if (S[n][m]=='?') S[n][m]=S[n-1][m];
                    }
                    for (int n=N-2; n>=0; n--) {
                        if (S[n][m]=='?') S[n][m]=S[n+1][m];
                    }
                }                
                
		printf("Case #%d:\n", t);
                for (int n=0; n<N; n++) {
                    printf("%s\n", S[n]);
                }

	}
	return 0;
}
