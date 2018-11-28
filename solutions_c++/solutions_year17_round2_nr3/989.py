#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace std;
using namespace __gnu_pbds;

typedef long long LL;

typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
ordered_set;
//find_by_order
//order_of_key

#define FO(i,a,b) for (int i = (a); i < (b); i++)

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );
#define ALL(v) v.begin(),v.end()

#define X first
#define Y second
#define MP make_pair

typedef pair<int,int> pint;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }


#define SIZE 105

struct node{
    int city;
    double cost;
    LL cap,speed;
    bool operator < (const node & p)const{return cost>p.cost;}
};


int n;

LL cap[SIZE];
LL speed[SIZE];

LL d[SIZE][SIZE];
priority_queue<node> q;

set< pair<LL,LL> > vis[SIZE];

bool initiated[SIZE];

bool is_current_superior(node& f) {
    return cap[f.city] >= f.cap && speed[f.city] >= f.speed;
}

bool is_vis(node &f) {
    for (auto&p:vis[f.city]) {
        if ( p.X>= f.cap && p.Y>= f.speed ) {
            return true;
        }
    }
    return false;
}

void add_to_q(node &tar) {
    if ( !is_vis(tar) ) {
        q.push(tar);
    }
}

double calc(int u,int v) {
    while ( !q.empty() ) q.pop();
    FO(i,0,n) vis[i].clear();
    FO(i,0,n) initiated[i]=false;

    q.push( {u,0,cap[u],speed[u]} );

    while ( !q.empty() ) {
        node f = q.top();q.pop();
        if ( f.city == v )return f.cost;

        if ( is_current_superior(f) ) {
            if (initiated[f.city]) {
                continue;
            }
            f.cap = cap[f.city];
            f.speed = speed[f.city];
            initiated[f.city] = true;
        }
        if ( is_vis(f) )continue;


        vis[f.city].insert( {f.cap,f.speed} );

        FO(i,0,n) {
            if ( d[f.city][i] == -1 )continue;
            if (f.cap < d[f.city][i]) continue;
            node tar = {i,f.cost + double(d[f.city][i])/f.speed, f.cap - d[f.city][i] , f.speed };
            add_to_q(tar);
        }
        if (initiated[f.city])continue;

        f.cap = cap[f.city];
        f.speed = speed[f.city];
        vis[f.city].insert( {f.cap,f.speed} );
        initiated[f.city] = true;
        FO(i,0,n) {
            if ( d[f.city][i] == -1 )continue;
            if (f.cap < d[f.city][i]) continue;
            node tar = {i,f.cost + double(d[f.city][i])/f.speed, f.cap - d[f.city][i] , f.speed };
            add_to_q(tar);
        }

    }

}

int main(){

    freopen("C-large.in","r",stdin);
    freopen("outC.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        int qq;
        scanf("%d %d",&n,&qq);

        FO(i,0,n) {
            scanf("%lld %lld",&cap[i],&speed[i]);
        }

        FO(i,0,n)FO(j,0,n) {
            scanf("%lld",&d[i][j]);
        }

        printf("Case #%d:",kk);
        while ( qq-- ) {
            int u,v;
            scanf("%d %d",&u,&v);
            u--,v--;

            printf(" %.8f",calc(u,v));
        }
        printf("\n");
        cerr<<kk<<endl;
    }

    return 0;
}
