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

struct node{
    int low,high;
    bool operator < (const node & p)const{
        if ( high-low != p.high - p.low ) {
            return high-low < p.high - p.low;
        } else {
            return low>p.low;
        }
    }
};


priority_queue<node> q;

int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("outC2.out","w",stdout);

    int kase;
    cin>>kase;

    for (int kk=1;kase--;++kk) {

        int n,k;
        cin>>n>>k;

        while (!q.empty())q.pop();

        q.push({0,n+1});

        FO(i,0,k-1) {
            node f = q.top();q.pop();

            int cut = (f.low + f.high) / 2;
            q.push({f.low,cut});
            q.push({cut,f.high});

        }
        node f = q.top();q.pop();

        //show(f.low,f.high);

        int cut = (f.low + f.high) / 2;

        printf("Case #%d: %d %d\n",kk,f.high-cut-1,cut-f.low-1);


    }


    return 0;
}
