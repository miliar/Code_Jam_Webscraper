#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

int T,N,R,O,Y,G,B,V;
char jawab[1005];
pair<int,char> banyak[5];

int main() {
    scanf("%d",&T);
    for (int l=1;l<=T;++l) {
        scanf("%d %d %d %d %d %d %d",&N,&R,&O,&Y,&G,&B,&V);
        if (2*R > N || 2*Y > N || 2*B > N) printf("Case #%d: IMPOSSIBLE\n",l);
        else {
            memset(jawab,0,sizeof(jawab));
            
            banyak[0] = make_pair(R,'R');
            banyak[1] = make_pair(B,'B');
            banyak[2] = make_pair(Y,'Y');
            sort(banyak,banyak+3);
            
            int idx = 0;
            for (int j=2;j>-1;--j) {
                for (int i=1;i<=banyak[j].first;++i) {
                    jawab[idx] = banyak[j].second;
                    idx += 2;
                    if (idx >= N) idx = 1;
                }
            }

            printf("Case #%d: %s\n",l,jawab);
        }
    }
    return 0;
}
