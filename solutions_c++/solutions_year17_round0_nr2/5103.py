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
		char S[20];
		scanf("%s", S);
                int N=strlen(S);
                int a=0, b=0;
                while (a<N){
                    while (b<N && S[a]==S[b]) b++;
                    if (b<N && S[a]>S[b]) break;
                    a=b;
                }
                if (a<N) S[a++]--;
                while (a<N) {
                    S[a++]='9';
                }
                char *SS=S;
                while (*SS == '0') SS++;
                printf("Case #%d: %s\n", t, SS);
	}
	return 0;
}
