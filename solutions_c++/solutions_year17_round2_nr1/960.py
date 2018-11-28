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

#define SIZE 1010

int n;
double tar;

pair<double,double> horse[SIZE];

double req[SIZE];

int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("outA.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        scanf("%lf %d",&tar,&n);

        FO(i,0,n) {
            scanf("%lf %lf",&horse[i].X,&horse[i].Y);
        }

        sort( horse,horse + n );

        req[n-1] = ( tar - horse[n-1].X )/ horse[n-1].Y;
        for (int i=n-2;i>=0;--i) {
            double tmp = ( tar - horse[i].X )/ horse[i].Y;
            if ( tmp >= req[i+1] ){
                req[i] = tmp;
                continue;
            }
            double catching_time = ( horse[i+1].X - horse[i].X ) / ( horse[i].Y - horse[i+1].Y );
            double t2 = ( (tar - horse[i].X) - horse[i].Y * catching_time ) / horse[i+1].Y;
            req[i] = catching_time + t2;
        }

        //FO(i,0,n)show(req[i]);

        printf("Case #%d: %.8f\n",kk,tar/req[0]);
    }


    return 0;
}
