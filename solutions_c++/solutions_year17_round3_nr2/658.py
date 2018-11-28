#include <cstdio>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

/*int C[109];
int D[109];
int J[109];
int K[109];*/

pair<pair<int,int>,int> A[209];

int main(){
    freopen("B-large (2).in","r",stdin);
    freopen("1cBlarge.out","w",stdout);
    //pi = acos(-1);
    //printf("%f",pi);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int AC, AJ;
        scanf("%d %d", &AC, &AJ);
        for (int i = 0; i < AC+AJ; i++){
            scanf("%d %d", &A[i].first.first,&A[i].first.second);
            if (i<AC) A[i].second = 0;
            else A[i].second = 1;
        }
        /*for (int i = 0; i < AC; i++){
            scanf("%d %d", &C[i], &D[i]);
        }
        for (int i = 0; i < AJ; i++){
            scanf("%d %d", &J[i], &K[i]);
        }*/
        sort(A,A+AC+AJ);
        int jm = 0;
        priority_queue<int> G;
        int seg = 0;
        for (int i = 0; i < AC+AJ; i++){
            if (A[i].second == 0) {
                jm += A[i].first.second - A[i].first.first;
                seg++;
                if (i==0){
                    if (A[AC+AJ-1].second==0) G.push(-(1440+A[i].first.first-A[AC+AJ-1].first.second));
                }
                else if (A[i-1].second==0) G.push(-(A[i].first.first-A[i-1].first.second));
            }
        }
        while (!G.empty()){
            jm -= G.top();
            G.pop();
            if (jm>720){
                //printf("Case #%d: %d\n",t,2*seg);
                break;
            }
            else {
                seg--;
            }
        }
        if (jm<720){
            jm = 0;
            int lj = 0;
            for (int i = AC+AJ-1; i >= 0; i--){
                if (A[i].second==1){
                    lj = i;
                    break;
                }
            }
            int pj = lj;
            for (int i = 0; i < AC+AJ; i++){
                if (A[i].second == 1) {
                    if (!((i==0&&pj==AC+AJ-1)||(i==pj+1))){
                        jm += A[i].first.first - A[pj].first.second;
                        if (jm<0) jm += 1440;
                    }
                    pj = i;
                }
            }
        }
        //printf("%d %d\n",jm,seg);
        if (jm<720){
            priority_queue<int> Q;
            for (int i = 0; i < AC+AJ; i++){
                if (A[i].second == 1) {
                    //jm += A[i].first.second - A[i].first.first;
                    //seg++;
                    if (i==0){
                        if (A[AC+AJ-1].second==1) Q.push((1440+A[i].first.first-A[AC+AJ-1].first.second));
                    }
                    else if (A[i-1].second==1) Q.push((A[i].first.first-A[i-1].first.second));
                }
            }
            while (jm<720){
                jm += Q.top();
                Q.pop();
                //printf("%d\n",jm);
                seg++;
                if (jm>=720) break;
            }
        }
        printf("Case #%d: %d\n",t,2*seg);
    }
}
