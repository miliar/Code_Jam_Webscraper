// ==========================================================================
//
//                   "With Every Difficulty, There is Relief."
//
// ==========================================================================

// Pre_code

#include <bits/stdc++.h>

// header file

#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <fstream>
#include <numeric>
#include <cstring>
//#include <unordered_map>
//#include <unordered_set>

using namespace std ;

//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
//
//using namespace __gnu_pbds;

//define function

#pragma                 comment(linker, "/STACK:667772160")
#define forln(i,a,n)    for(int i=a ; i<n ; i++)
#define foren(i,a,n)    for(int i=a ; i<=n ; i++)
#define forg0(i,a,n)    for(int i=a ; i>n ; i--)
#define fore0(i,a,n)    for(int i=a ; i>=n ; i--)
#define pb              push_back
#define pp              pop_back
#define clr(a,b)        memset(a,b,sizeof(a))
#define sf1(a)          scanf("%d",&a)
#define sf2(a,b)        scanf("%d %d",&a,&b)
#define sf1ll(a)        scanf("%lld",&a)
#define sf2ll(a,b)      scanf("%lld %lld",&a,&b)
#define pii             acos(-1.0)
#define jora_int        pair<int,int>
#define jora_ll         pair<long long,long long>
#define max3(a,b,c)     max(a,max(b,c))
#define min3(a,b,c)     min(a,min(b,c))
#define Max             2000000000+9
#define sz              10000+7
#define Mod             100000007
#define EPS             1e-9
#define ll              long long
#define ull             unsigned long long
#define fs              first
#define sc              second
#define wait            system("pause")
#define sf              scanf
#define pf              printf
#define mp              make_pair
#define ps              pf("PASS\n")
#define Read            freopen("00.txt","r",stdin)
#define Write           freopen("C:\\Users\\RONIN-47\\Desktop\\input_output\\output.txt","w",stdout)
#define num_of_bit(a)   __builtin_popcount(a) // for long long use ll as suffix
#define lsb(a)          __builtin_ffs(a) // for long long use ll as suffix
#define msb(a)          32-__builtin_clz(a) // for long long use ll as suffix
#define inf             10000000000000000LL

// typedef

typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<jora_int> VJ ;
typedef vector<jora_ll> VJL ;

//debug

struct debugger
{
    template<typename T> debugger& operator, (const T& v)
    {
        cerr<< v <<" ";
        return *this;
    }
} dbg;
#define deb(args...) {dbg,args; cerr<<endl;}


// moves

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

//int set_bit(int n,int pos)
//{
//    return (int)(n|(1<<pos));
//}
//
//int off_bit(int n,int pos)
//{
//    return (int)(n&(~(1<<pos))) ;
//}
//
//bool is_on(int n,int pos)
//{
//    return (bool)(n&(1<<pos));
//}
//
//int flip_bit(int n,int pos)
//{
//    return (int)(n^(1<<pos));
//}

//close

int arr[1000+7] ;

int main()
{
    int tcase ;
    char str[1000+7] ;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    sf1(tcase);

    int k ;

    for(int cas=1 ; cas<=tcase ; cas++)
    {
        sf("%s",str);
        sf1(k);

        int ln = strlen(str);
        clr(arr,0);

        int cont = 0 , b , togg = 0 ;
        bool ok = 1 ;

        for(int i=0 ; i<ln ; i++)
        {
            togg+=arr[i] ;

            if((togg%2 == 0 && str[i] == '-') || (togg%2 == 1 && str[i] == '+'))
            {
                cont++;

                if(i+k>ln)
                {
                    ok = 0 ;
                    break;
                }

                arr[i+k]--;
                togg++;
            }
        }

        pf("Case #%d: ",cas);

        if(ok)
            pf("%d\n",cont);

        else
            pf("IMPOSSIBLE\n");
    }

    return 0 ;
}
