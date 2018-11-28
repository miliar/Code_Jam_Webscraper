#include <cstdio>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

int E[109];
int S[109];
vector<pair<long double,int> > A[109];
vector<pair<int,int> > D[109];
long double Y[109];
int Z[109];
bool V[109];

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("Csmallout.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, Q;
        scanf("%d %d", &N, &Q);
        for (int i = 1; i <= N; i++){
            scanf("%d %d", &E[i], &S[i]);
        }
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                int x;
                scanf("%d", &x);
                if (x != -1){
                    D[i].push_back(make_pair(x,j));
                }
            }
        }
        for (int i = 1; i <= N; i++){
            priority_queue<pair<int,int> > PQ;
            for (int j = 1; j <= N; j++){
                Z[j] = 1000000000;
                V[j] = false;
            }
            Z[i] = 0;
            V[i] = true;
            for (vector<pair<int,int> >::iterator j = D[i].begin(); j != D[i].end(); j++){
                PQ.push(make_pair(-j->first,j->second));
            }
            while (!PQ.empty()){
                pair<int,int> p = PQ.top();
                PQ.pop();
                if (V[p.second]) continue;
                p.first = -p.first;
                V[p.second] = true;
                Z[p.second] = p.first;
                A[i].push_back(make_pair(((long double)Z[p.second]/S[i]),p.second));
                //printf("%d\n",p.second);
                for (vector<pair<int,int> >::iterator j = D[p.second].begin(); j != D[p.second].end(); j++){
                    if (!V[j->second]&&(j->first+Z[p.second])<=E[i]){
                        PQ.push(make_pair(-(j->first+Z[p.second]),j->second));
                    }
                }
            }
            /*for (vector<pair<long double,int> >::iterator j = A[i].begin(); j != A[i].end(); j++){
                printf("(%f,%d) ",(double)j->first,j->second);
            }
            printf("\n");*/
        }
        //Q;
        //scanf("%d", &Q);
        printf("Case #%d: ", t);
        for (int q = 1; q <= Q; q++){
            int u, v;
            scanf("%d %d", &u, &v);
            priority_queue<pair<long double,int> > PQ;
            for (int j = 1; j <= N; j++){
                V[j] = false;
            }
            Y[u] = (long double)0.0;
            V[u] = true;
            for (vector<pair<long double,int> >::iterator j = A[u].begin(); j != A[u].end(); j++){
                PQ.push(make_pair(-j->first,j->second));
                //printf("%f %d\n",(double)j->first,j->second);
            }
            while (!PQ.empty()){
                pair<long double,int> p = PQ.top();
                PQ.pop();
                if (V[p.second]) continue;
                p.first = -p.first;
                //printf("%f\n",(double)p.first);
                V[p.second] = true;
                Y[p.second] = p.first;
                //printf("%d %f\n", p.second,(double)Y[p.second]);
                //printf("%d\n",A[p.second].size());
                for (vector<pair<long double,int> >::iterator j = A[p.second].begin(); j != A[p.second].end(); j++){
                    //printf("%d\n",j->second);
                    if (!V[j->second]){
                        PQ.push(make_pair(-(j->first+Y[p.second]),j->second));

                    }
                }
            }
            printf("%f ",(double)Y[v]);
        }
        printf("\n");
        for (int i = 1; i <= N; i++){
            A[i].clear();
            D[i].clear();
        }
    }
}
