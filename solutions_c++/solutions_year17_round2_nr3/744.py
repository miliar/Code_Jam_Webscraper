//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

double E[100009];
double S[100009];
double dis[109][109];
double dis_[109][109];
int N;
double EPS  = 1e-9;

struct data {
    int  city, from;
    double dist;
    bool operator < ( const data& p ) const {
        return dist > p.dist;
    }
};

priority_queue<data> q;

double dijkstra(long long  source)
{
    //cout<<"nnn "<<N<<endl;
    int i;
    while( !q.empty() ) q.pop();
    data u, v;
    u.city = source;
    u.from = source;
    u.dist = 0;
    q.push(u);
    dis[source][source] = 0;
    while( !q.empty() )
    {
        u = q.top();
        q.pop();
        double ucost = dis[ u.city ][u.from];
        for(i=1;i<=N;i++)
        {
            v.city = i;
            v.from = u.from;
            v.dist = dis_[v.from][v.city]*1.0/S[v.from] + ucost;

            if(dis_[v.from][v.city]<E[v.from] || fabs(dis_[v.from][v.city]-E[v.from])<=EPS)
            {
                if( dis[v.city][v.from] > v.dist )
                {
                    //cout<<v.city<<" "<<v.from<<" "<<dis[v.city][v.from]<<endl;
                    dis[v.city][v.from] = v.dist;
                    q.push( v );
                }

                v.from=v.city;
                if( dis[v.city][v.from] > v.dist )
                {
                    //cout<<v.city<<" "<<v.from<<" "<<dis[v.city][v.from]<<endl;
                    dis[v.city][v.from] = v.dist;
                    q.push( v );
                }
            }
        }
    }
}

int main()
{
    freopen("C-large.in","r",stdin);
    //freopen("out.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int i,j,k,l,n,cas,test,q,source,dest;
    double ans;

    cin>>test;
    //cout<<test<<endl;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>q;

        for(i=1;i<=n;i++)
        {
            cin>>E[i]>>S[i];
        }

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                cin>>dis_[i][j];
                if(fabs(dis_[i][j]+1)<=EPS) dis_[i][j]=1e12;
            }
        }

        for(i=1;i<=n;i++) for(j=1;j<=n;j++) for(k=1;k<=n;k++) dis_[j][k]=min(dis_[j][k],dis_[j][i]+dis_[i][k]);
//        for(i=1;i<=n;i++)
//        {
//            for(j=1;j<=n;j++)
//            {
//                cout<<dis_[i][j]<<" ";
//            }
//            cout<<endl;
//        }

        printf("Case #%d:",cas);
        while(q--)
        {
            N=n;
            for(i=1;i<=n;i++) for(j=1;j<=n;j++) dis[i][j]=1e20;
            cin>>source>>dest;
            dijkstra(source);
            ans=1e20;
            for(i=1;i<=n;i++) ans=min(ans,dis[dest][i]);
            cout<<fixed<<setprecision(10)<<" "<<ans;
        }
        cout<<endl;

    }



}
