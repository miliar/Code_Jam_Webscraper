#include<stdio.h>
#include<queue>
using namespace std;

int n, q;
int e[100]={0};
double s[100]={0};
int d[100][100]={0};
long long min_dist[100][100]={0};
double min_time[100][100]={0};

double time[100]={0};
bool check[100]={0};
priority_queue< pair<double, int> > pq;

const long long MAX = 10000000000000;
int main()
{
    int t,test;
    int k,i,j;
    int start;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    scanf("%d",&test);
    for(t=1;t<=test;t++){
        scanf("%d%d",&n,&q);
        for(i=0;i<n;i++)
            scanf("%d%lf",&e[i],&s[i]);
        for(i=0;i<n;i++){
            for(j=0;j<n;j++) scanf("%d",&d[i][j]);
        }
        for(start=0;start<n;start++){
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    if(i==j) min_dist[i][j] = 0;
                    else if(d[i][j] == -1) min_dist[i][j] = MAX;
                    else min_dist[i][j] = d[i][j];
                }
            }
            for(k=0;k<n;k++){
                for(i=0;i<n;i++){
                    for(j=0;j<n;j++){
                        if(min_dist[i][j] > min_dist[i][k] + min_dist[k][j]){
                            min_dist[i][j] = min_dist[i][k] + min_dist[k][j];
                        }
                    }
                }
            }
        }

        for(start=0;start<n;start++){
            for(i=0;i<n;i++){
                time[i] = (double) MAX;
                check[i] = false;
            }
            time[start] = 0.0;
            pq.push(make_pair(0.0, start));

            while(!pq.empty()){
                int cur = pq.top().second;
                pq.pop();
                if(check[cur]) continue;
                check[cur] = true;

                for(i=0;i<n;i++){
                    if(min_dist[cur][i] > (long long)e[cur]) continue;
                    if( ((double) min_dist[cur][i] / s[cur]) + time[cur] < time[i]){
                        time[i] = ((double) min_dist[cur][i] / s[cur]) + time[cur];
                        pq.push(make_pair( -time[i], i ));
                    }
                }
            }
            for(i=0;i<n;i++)
                min_time[start][i] = time[i];
        }

        printf("Case #%d: ", t);
        for(i=0;i<q;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            a--; b--;
            printf("%.8lf ", min_time[a][b]);
        }
        printf("\n");
    }
    return 0;
}
