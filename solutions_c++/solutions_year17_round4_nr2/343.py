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

int n,c,m;
pint ticket[SIZE];
vector<int> per[SIZE];
vector<int> row[SIZE];

int rowcnt[SIZE];
int shift;

bool pos(int ride){

    int car = 0;
    shift = 0;
    FO(i,1,n+1){
        if ( rowcnt[i] <= ride ){
            car += ride - rowcnt[i];
        }else{
            car -= rowcnt[i] - ride;
            shift += rowcnt[i] - ride;
            if ( car<0 )return false;
        }
    }
    return true;
}


pint calc(){

    int low = 0;
    FO(i,0,SIZE){
        low = max( low,int(per[i].size()) );
        //low = max( low,int(row[i].size()) );
    }
    //show(low);
    int high = SIZE;
    pint ans;
    while (low<=high){
        int mid= (low+high)/2;
        if ( pos(mid) ){
            high = mid-1;
            ans = MP(mid,shift);
        }else{
            low = mid+1;
        }
    }
    return ans;
}


int main(){

    freopen("B-large.in","r",stdin);
    freopen("outB.out","w",stdout);

    int kase;
    cin>>kase;

    for (int kk=1;kase--;++kk){

        FO(i,0,SIZE){
            per[i].clear();
            row[i].clear();
        }
        CLR(rowcnt);

        cin>>n>>c>>m;

        FO(i,0,m){
            cin>>ticket[i].X>>ticket[i].Y;
            row[ ticket[i].X ].PB( ticket[i].Y );
            per[ ticket[i].Y ].PB( ticket[i].X );
            rowcnt[ticket[i].X]++;
        }


        pint ride = calc();

        printf("Case #%d: %d %d\n",kk,ride.X,ride.Y);
    }


    return 0;
}
