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

char str[SIZE];

int main(){

    freopen("A-large.in","r",stdin);
    freopen("outASmall.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        int k;
        scanf("%s %d",str,&k);

        int ans = 0;
        int n = strlen(str);
        queue<int> q;
        FO(i,0,n) {
            while ( !q.empty() && q.front() <= i - k ) {
                q.pop();
            }
            int val = (str[i]=='+')? 0 : 1;
            if ( q.size()%2 == 1 )val ^= 1;
            if ( val ){
                if ( i + k - 1 >= n ){
                    ans = -1;
                    break;
                }
                ans ++;
                q.push( i );
            }
        }
        if ( ans != -1 ){
            printf("Case #%d: %d\n",kk,ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n",kk);
        }
    }

    return 0;
}
