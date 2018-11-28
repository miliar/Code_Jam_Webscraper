/*
    @Author: wchhlbt
    @Date:   2017/4/7
*/
#include <bits/stdc++.h>

#define Fori(x) for(int i=0;i<x;i++)
#define Forj(x) for(int j=0;j<x;j++)
#define maxn 11005
#define inf 0x3f3f3f3f
#define ONES(x) __builtin_popcount(x)
using namespace std;

typedef long long ll ;
const double eps =1e-8;
const int mod = 1000000007;
typedef pair<int, int> P;
const double PI = acos(-1.0);
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

ll n;

bool judge(ll num)
{
    int a[20] = {0};
    int cnt = 0;
    while(num){
        a[cnt++] = num%10;
        num /= 10;
    }
    
    for(int i = 0; i<cnt; i++){
        if(a[i]<a[i+1])
            return false;
    }
    return true;
}

int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int kase = 1; kase<=t; kase++)
    {
    	cin>>n;
    	for(ll i = n; i>=1; i--){
            if(judge(i)){
                printf("Case #%d: %d\n",kase,i);
                break;
            }
        }
    }
    //cout << ans << endl;
    return 0;
}

/*

unsigned   int   0～4294967295
int   2147483648～2147483647
unsigned long 0～4294967295
long   2147483648～2147483647
long long的最大值：9223372036854775807
long long的最小值：-9223372036854775808
unsigned long long的最大值：18446744073709551615

__int64的最大值：9223372036854775807
__int64的最小值：-9223372036854775808
unsigned __int64的最大值：18446744073709551615

*/

