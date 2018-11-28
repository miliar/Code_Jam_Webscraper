#include <iostream>
#include <queue>
#include <iomanip>
using namespace std;

struct horse{
    long long e;
    long long s;
};

struct node{
    long long ind;
    double t;
    node (long long a=0, double b=-1){
        ind=a; t=b;
    }
    bool operator < (const node a)const{
        return t > a.t;
    }
};

long long n, q;
long long d[128][128];
long long d2[128][128];
double times[128];
horse h[128];

void calcd2(){
    for (long long i=0; i<n; ++i){
        for (long long j=0; j<n; ++j){
            d2[i][j]=d[i][j];
            if (i==j){d2[i][j]=0;}
        }
    }

    for (long long k=0; k<n; ++k){
        for (long long i=0; i<n; ++i){
            for (long long j=0; j<n; ++j){
                if (d2[i][k]!=-1 && d2[k][j]!=-1 && (d2[i][j]>d2[i][k]+d2[k][j] || d2[i][j]==-1)){
                    d2[i][j] = d2[i][k]+d2[k][j];
                }
            }
        }
    }
}

priority_queue<node> qu;
void closest(long long from){
    for (long long i=0; i<n; ++i){times[i]=-1;}
    times[from]=0;
    qu.push(node(from, 0));
    while (!qu.empty()){
        node top = qu.top();
        qu.pop();
        if (top.t > times[top.ind]){continue;}
        for (long long i=0; i<n; ++i){
            if (d2[top.ind][i] > h[top.ind].e || d2[top.ind][i]==-1){continue;}
            double time = (double)(d2[top.ind][i])/h[top.ind].s;
            if (top.t + time < times[i] || times[i]==-1){
                times[i] = top.t + time;
                qu.push(node(i, times[i]));
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    long long t;
    cin>>t;
    for (long long l=0; l<t; ++l){
        cin>>n>>q;
        for (long long i=0; i<n; ++i){
            cin>>h[i].e>>h[i].s;
        }
        for (long long i=0; i<n; ++i){
            for (long long j=0; j<n; ++j){
                cin>>d[i][j];
            }
        }
        calcd2();
        cout<<"Case #"<<l+1<<": ";
        for (long long i=0; i<q; ++i){
            long long u, v;
            cin>>u>>v;
            --u;--v;
            closest(u);
            cout<<fixed<<setprecision(6)<<times[v]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
