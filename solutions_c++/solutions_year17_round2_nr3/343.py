#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

int n,q;
int e[110];
int s[110];
int d[110][110];
int u[110];
int k[110];
double t[110][110];
double t2[110][110];
bool visited[110];
using ll=long long;
void mark(int from){
    fill(visited,visited+110,false);
    fill(t[from],t[from]+110,-1);
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>> pq;
    pq.push({0,from});
    while(!pq.empty()){
        auto now = pq.top();
        pq.pop();
        auto nowv=now.second;
        auto nowd=now.first;
        if(visited[nowv])continue;
        visited[nowv]=true;
        t[from][nowv]=double(nowd)/s[from];
        for(int i = 0 ; i < n ; i ++){
            if(d[nowv][i]!=-1&&(!visited[i])&&(nowd+d[nowv][i]<=e[from])){
                pq.push({nowd+d[nowv][i],i});
            }
        }
    }
}
void mark2(int from){
    fill(visited,visited+110,false);
    fill(t2[from],t2[from]+110,-1);
    priority_queue<pair<double,int>,vector<pair<double,int>>,greater<pair<double,int>>> pq;
    pq.push({0,from});
    while(!pq.empty()){
        auto now = pq.top();
        pq.pop();
        auto nowv=now.second;
        auto nowd=now.first;
        if(visited[nowv])continue;
        visited[nowv]=true;
        t2[from][nowv]=nowd;
        for(int i = 0 ; i < n ; i ++){
            if(t[nowv][i]>0&&(!visited[i])){
                pq.push({nowd+t[nowv][i],i});
            }
        }
    }
}
int main (){
    int T;
    scanf("%d",&T);
    for(int I = 1 ; I <= T ; I ++){
        scanf("%d%d",&n,&q);
        for(int i = 0 ; i < n ; i ++){
            scanf("%d%d",e+i,s+i);
        }
        for(int i = 0 ; i < n ; i ++){
            for(int j = 0 ; j < n ; j ++){
                scanf("%d",&(d[i][j]));
            }
        }
        for(int i = 0 ; i < q ; i ++){
            scanf("%d%d",u+i,k+i);
        }
        for(int i = 0 ; i < n ; i ++){
            mark(i);
        }
        for(int i = 0 ; i < n ; i ++){
            mark2(i);
        }
        printf("Case #%d:",I);
        for(int i = 0 ; i < q ; i ++){
            printf(" %.15f",t2[u[i]-1][k[i]-1]);
        }
        printf("\n");
    }

}
