#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<string>
#include<queue>
#define ll long long
#define fi first
#define se second
using namespace std;
int main(void){
    //freopen("test.txt", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in","r", stdin);
    //freopen("B.out", "w",stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        int N; int M;
        scanf("%i %i", &N, &M);
        int a[N];
        int i;
        for(i=0;i<N;i++){
            scanf("%i", &a[i]);
        }
        vector<vector<int> > b;
        b.resize(N);
        int j;
        int c[N];
        int h;
        for(i=0;i<N;i++){
            c[i]=1;
            for(j=0;j<M;j++){
                scanf("%i", &h);
                b[i].push_back(h);
            }
            sort(b[i].begin(), b[i].end());
        }
        priority_queue<pair<int, int> > f;
        priority_queue<pair<int, int> > g;
        for(i=0;i<N;i++){
            j=0;
            while(j<M&&100*b[i][j]/(90*a[i])<(100*b[i][j]-1)/(110*a[i])+1) j++;
            if(j==M) break;
            f.push({-100*b[i][j]/(90*a[i]),i});
            g.push({(100*b[i][j]-1)/(110*a[i])+1,i});
            c[i]=j+1;
        }
        /*for(i=0;i<N;i++){
            printf("%i ", c[i]);
        }
        printf("\n");*/
        if(j==M){printf("Case #%i: 0\n", l+1); continue;}
        int res=0;
        while(!f.empty()){
            pair<int, int> x=f.top();
            pair<int, int> y=g.top();
            if(-x.fi>=y.fi) {
                res++;
                for(i=0;i<N;i++){
                    f.pop();
                }
                for(i=0;i<N;i++){
                    while(c[i]<M&&100*b[i][c[i]]/(90*a[i])<(100*b[i][c[i]]-1)/(110*a[i])+1) c[i]++;
                    if(c[i]==M) break;
                    f.push({-100*b[i][c[i]]/(90*a[i]), i});
                    g.push({(100*b[i][c[i]]-1)/(110*a[i])+1,i});
                    c[i]++;
                }
                if(i!=N) break;
            }
            else{
                f.pop();
                i=x.se;
                while(c[i]<M&&(100*b[i][c[i]]/(90*a[i])<(100*b[i][c[i]]-1)/(110*a[i])+1)) c[i]++;
                if(c[x.se]==M) break;
                f.push({-100*b[x.se][c[x.se]]/(90*a[x.se]), x.se});
                g.push({(100*b[x.se][c[x.se]]-1)/(110*a[x.se])+1,x.se});
                c[x.se]++;
            }
        }
        printf("Case #%i: %i\n", l+1, res);
    }
    return 0;
}
