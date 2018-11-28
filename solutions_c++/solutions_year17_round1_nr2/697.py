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

pair<int, int> foo(int q, int r) {
    return make_pair((q*10+11*r-1)/(11*r), (q*10)/(9*r));
}

int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, M;
                int R[60];
                pair<int, int> Q[60][60];
		scanf("%d%d", &N, &M);
                for (int i=0; i<N; i++)
                    scanf("%d", R+i);
                for (int i=0; i<N; i++) {
                    for (int j=0; j<M; j++) {
                        int q;
                        scanf("%d", &q);
                        Q[i][j]=foo(q, R[i]);
                        
                    }
                    sort(Q[i], Q[i] + M);
                }
                vector<int> I(N, 0);
                int res=0;
                while(1) {
                    if (*max_element(I.begin(), I.end()) >=M) break;
                    pair<int, int>  a=Q[0][I[0]];
                    for (int i=1; i<N; i++) {
                        a.first=max(a.first, Q[i][I[i]].first);
                        a.second=min(a.second, Q[i][I[i]].second);
                    }
                    if (a.first>a.second) {
                        for (int i=0; i<N; i++) {
                            if(Q[i][I[i]].second<a.first) I[i]++;
                        }
                        continue;
                    }
                    for (int i=0; i<N; i++) {
                        I[i]++;
                    }
                    res++;
                    
                }
                
		printf("Case #%d: %d\n", t, res);


	}
	return 0;
}
