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

#define SIZE 1100

int n;
int cnt[5];
int ans[SIZE];

bool violate(){
    FO(i,0,n) {
        if ( ans[i] == ans[(i+1)%n] ){
            return true;
        }
    }
    return false;
}

int main(){

    freopen("B-small-attempt2.in","r",stdin);
    freopen("outB.out","w",stdout);

    char dir[5];
    dir[0] = 'R';
    dir[1] = 'Y';
    dir[2] = 'B';

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        scanf("%d",&n);
        FO(i,0,3) {
            scanf("%d %*d",&cnt[i]);
            //show(i,cnt[i]);
        }

        int st = 0;
        FO(i,0,3) {
            if ( cnt[i] > 0 ){
                st = i;
                break;
            }
        }
        ans[0] = st;
        cnt[st]--;
        bool pos= true;
        FO(i,1,n) {
            int now = 0;
            if ( cnt[(st+1)%3] > cnt[(st+2)%3]  ){
                now = (st+1)%3;
            } else {
                now = (st+2)%3;
            }
            if ( cnt[now] == 0 ) {
                pos=false;
                break;
            }
            ans[i] = now;
            cnt[now]--;
            st = now;
        }

        printf("Case #%d: ",kk);

        if ( !pos ){
            printf("IMPOSSIBLE\n");
            continue;
        }

        if ( ans [0] == ans[n-1] ) {
            int tmp = n-1;
            swap( ans[tmp],ans[tmp-1] );
            tmp -= 1;
            while ( tmp-1>= 0 ){
                if ( ans[tmp] != ans[tmp-1] ){
                    break;
                }
                swap( ans[tmp],ans[tmp-1] );
                tmp -= 1;
            }
        }

        if ( violate() ){
            printf("IMPOSSIBLE\n");
            continue;
        }

        for (int i=0;i<n;++i) {
            printf("%c",dir[ ans[i] ]);
        }
        printf("\n");

    }

    return 0;
}
