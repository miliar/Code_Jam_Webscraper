#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
const int SIZE = 30;
typedef pair<int,int> p;

char s[SIZE][SIZE];

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cs = 1;
    while(T--) {
        int N, M;
        scanf("%d%d",&N,&M);
        for(int i = 0; i < N; i++) scanf("%s",s[i]);
        // xia
        for(int i = 1; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(s[i][j] == '?') {
                    s[i][j] = s[i-1][j];
                }
            }
        }
        //shang
        for(int i = N - 2; i >= 0; i--) {
            for(int j = 0; j < M; j++) {
                if(s[i][j] == '?') {
                    s[i][j] = s[i+1][j];
                }
            }
        }
        for(int i = 0; i < N; i++) {
            for(int j = 1; j < M; j++) {
                if(s[i][j] == '?') {
                    s[i][j] = s[i][j-1];
                }
            }
        }
        for(int i = 0; i < N; i++) {
            for(int j = M - 2; j >= 0; j--) {
                if(s[i][j] == '?') {
                    s[i][j] = s[i][j+1];
                }
            }
        }
        printf("Case #%d:\n",cs++);
        for(int i = 0; i < N; i++) printf("%s\n",s[i]);
    }


    return 0;
}

