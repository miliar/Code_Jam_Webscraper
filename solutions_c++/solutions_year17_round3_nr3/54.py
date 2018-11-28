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


#define SIZE 55


double pro[SIZE];

int main(){

    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("outC.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {

        int n,k;
        scanf("%d %d",&n,&k);

        double have;
        scanf("%lf",&have);

        FO(i,0,n) {
            scanf("%lf",&pro[i]);
        }


        double low = 0,high = 1;
        for (int i=0;i<100;++i){

            double mid = (low+high)/2;

            double req = 0;
            FO(j,0,n){
                req += max(0.0, mid - pro[j]);
            }

            if ( req>have ){
                high= mid;
            }else{
                low = mid;
            }
        }

        double ans = 1;
        FO(i,0,n) {
            ans = ans * max(pro[i],low);
        }

        printf("Case #%d: %.8f\n",kk,ans);
    }


    return 0;
}
