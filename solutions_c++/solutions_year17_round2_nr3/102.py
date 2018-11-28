#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
#define INF 0x7fffffffffffffff

using namespace std;

typedef pair <double,int> ppair;
priority_queue <ppair,vector<ppair>,greater<ppair> > Q;
int T, N, Qu, E[101], S[101], U[101], V[101];
long long D[101][101];
double Dy[101];

double calc(int s, int e) {

    int i, now;
    double t;

    for(i=1 ; i<=N ; i++)
        Dy[i]=INF;
    Dy[s]=0;
    Q.push(make_pair(Dy[s],s));
    while(!Q.empty()) {
        t=Q.top().first;
        now=Q.top().second;
        Q.pop();
        for(i=1 ; i<=N ; i++)
            if(D[now][i]<=E[now] && Dy[i]>t+(double)D[now][i]/S[now]) {
                Dy[i]=t+(double)D[now][i]/S[now];
                Q.push(make_pair(Dy[i],i));
            }
    }
    return Dy[e];
}

int main(void) {

    int i, j, k, l;

    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%d %d",&N,&Qu);
        for(j=1 ; j<=N ; j++)
            scanf("%d %d",&E[j],&S[j]);
        for(j=1 ; j<=N ; j++)
            for(k=1 ; k<=N ; k++) {
                scanf("%lld",&D[j][k]);
                if(D[j][k]==-1)
                    D[j][k]=INF;
            }
        for(l=1 ; l<=N ; l++)
            for(j=1 ; j<=N ; j++)
                for(k=1 ; k<=N ; k++)
                    if(D[j][l]!=INF && D[l][k]!=INF && D[j][k]>D[j][l]+D[l][k])
                        D[j][k]=D[j][l]+D[l][k];
        for(j=1 ; j<=Qu ; j++)
            scanf("%d %d",&U[j],&V[j]);
        printf("Case #%d: ",i);
        for(j=1 ; j<=Qu ; j++)
            printf("%.9lf ",calc(U[j],V[j]));
        printf("\n");
    }

    return 0;
}
