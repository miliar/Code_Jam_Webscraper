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


int dp[SIZE][SIZE][SIZE][6];
int p;

int calc(int val){
    if (val%p == 0)return 1;
    else return 0;
}

int func(int a,int b,int c,int car){
    car %= p;
    if ( a== 0 && b== 0 && c==0 ){
        if(car>0)return 1;
        else return 0;
    }
    int &ret = dp[a][b][c][car];
    if (ret != -1)return ret;

    ret = 0;
    if (a>0){
        ret = max(ret, calc(car+1) + func(a-1,b,c,car+1));
    }
    if (b>0){
        ret = max(ret, calc(car+2) + func(a,b-1,c,car+2));
    }
    if (c>0){
        ret = max(ret, calc(car+3) + func(a,b,c-1,car+3));
    }

    return ret;
}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("outA.out","w",stdout);

    int kase;
    cin>>kase;

    for (int kk=1;kase--;++kk){

        int n;
        cin>>n>>p;

        int tmp,ans = 0;
        int cnt[10]={0};
        FO(i,0,n){
            cin>>tmp;
            if (tmp%p==0){
                ans++;
            }else{
                cnt[tmp%p]++;
            }
        }

        NEG(dp);

        printf("Case #%d: %d\n",kk,ans + func(cnt[1],cnt[2],cnt[3],0));




    }


    return 0;
}
