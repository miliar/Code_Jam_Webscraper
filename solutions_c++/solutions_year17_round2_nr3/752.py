#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

int e[100];
int s[100];
int d[100][100];
int u[100];
int v[100];
using namespace std;

typedef pair<double, int> iPair;

int main(){
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n,q;
        scanf("%d%d",&n,&q);
        for(int i=0;i<n;i++){
            scanf("%d%d",&e[i],&s[i]);
        }
        for(int i=0;i<n;i++)for(int j=0;j<n;j++)scanf("%d",&d[i][j]);
        for(int i=0;i<q;i++){scanf("%d%d",&u[i],&v[i]);}
//small




//n*Dijkstra:precompute where we can go

        map<int,double> directd[100];
        for(int i=0;i<n;i++){
            priority_queue<iPair, vector <iPair> , greater<iPair> > pq;
            vector<double> dist(n, 1e50);
            pq.push(make_pair(0, i));
            dist[i]=0;
            while (!pq.empty()){
            int u = pq.top().second;
            if(pq.top().first>e[i])break;
            pq.pop();
            for(auto j=0;j<n;j++){if(d[u][j]!=-1 && dist[j]>dist[u]+d[u][j] && dist[u]+d[u][j] <= e[i] ){
                dist[j]=dist[u]+d[u][j];pq.push(make_pair(dist[j],j));}}
            }
            for(int j=0;j<n;j++){if(dist[j]<=e[i] && dist[j]>0){
                //printf("woo cango %d %d\n",i,j);
                (directd[i])[j]=dist[j];}}
        }







//

printf("Case #%d: ",cas);
for(int tc =0;tc<q;tc++){

set<int> reachable;
vector<double> time(100,1e50);
time[u[tc]-1]=0;
reachable.insert(u[tc]-1);

for(int nbhorse=0;nbhorse<n-1;nbhorse++){
    map<int,double> n_r;
    for(int x:reachable){//where can I go, changing at x
        for(auto i:directd[x]){
                //we can reach i from x!
                //printf("we can reach %d from %d\n",i.first,x);
                if(n_r.find(i.first)==n_r.end() || n_r[i.first]>time[x]+(double)(i.second)/(double)s[x] )
                    n_r[i.first] = time[x]+(double)(i.second)/(double)s[x];
            }
        }

    reachable.clear();
    for(auto it=n_r.begin();it!=n_r.end();++it){
        reachable.insert(it->first);
        time[it->first]=min(time[it->first],n_r[it->first]);
    
    }


}
    printf("%lf%c",time[v[tc]-1],q-1==tc?'\n':' ');
    }


       /* 
        for(int k=0;k<n;k++)
        for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            //is it better to do i-k-j or keep previous i-j ?


        }*/



    }
}

