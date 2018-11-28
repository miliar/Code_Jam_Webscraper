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
#define sz              40000+7
#define Mod             1000000007
#define EPS             1e-7
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
int dx[]= {0,0,1,-1};/*4 side move*/
int dy[]= {-1,1,0,0};/*4 side move*/
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

char str[50][50] ;
int r , c ;

struct data
{
    int mnx , mxx , mny , mxy ;

    data() {}

    void ini()
    {
        mnx = -1 ;
        mxx = -1 ;
        mny = -1 ;
        mxy = -1 ;
    }
};

data arr[30] ;
bool visit[26][26] ;

bool isvalid(int x,int y)
{
    if(x>=0 && x<r && y>=0 && y<c)
        return 1 ;

    return 0 ;
}

void dfs(int x,int y,int ch)
{
    if(isalpha(str[x][y]) && (int)(str[x][y]-'A') == ch)
    {
        if(arr[ch].mnx == -1)
        {
            arr[ch].mnx = x ;
            arr[ch].mxx = x ;
            arr[ch].mny = y ;
            arr[ch].mxy = y ;
        }

        else
        {
            arr[ch].mnx = min(arr[ch].mnx,x);
            arr[ch].mxx = max(arr[ch].mxx,x);
            arr[ch].mny = min(y,arr[ch].mny);
            arr[ch].mxy = max(y,arr[ch].mxy);
        }
    }

    visit[x][y] = 1 ;

    int tx , ty ;

    for(int i=0 ; i<4 ; i++)
    {
        tx = x + dx[i] ;
        ty = y + dy[i] ;

        if(isvalid(tx,ty) && visit[tx][ty] == 0)
            dfs(tx,ty,ch);
    }
}

void fill_up(int id)
{
    for(int i=arr[id].mnx  ; i<=arr[id].mxx ; i++)
    {
        for(int j=arr[id].mny ; j<=arr[id].mxy ; j++)
            str[i][j] = (id+'A') ;
    }
}

VI all ;

bool cal_y(int id,int v)
{
    int y ;

    if(v == -1)
        y = arr[id].mny - 1 ;

    else
        y = arr[id].mxy + 1 ;

    if(y<0 || y>=c)
        return 0 ;

    for(int i=arr[id].mnx ; i<=arr[id].mxx ; i++)
    {
        if(str[i][y] != '?')
            return 0 ;
    }

    for(int i=arr[id].mnx  ; i<=arr[id].mxx ; i++)
        str[i][y] = (id + 'A');

    if(v == -1)
        arr[id].mny-- ;

    else
        arr[id].mxy++ ;

    return 1 ;
}

bool cal_x(int id,int v)
{
    int tx ;

    if(v == -1)
        tx = arr[id].mnx - 1 ;

    else
        tx = arr[id].mxx + 1 ;


    if(tx<0 || tx>=r)
        return 0 ;

    for(int i=arr[id].mny ; i<=arr[id].mxy ; i++)
    {
        if(str[tx][i] != '?')
            return 0 ;
    }

    for(int i=arr[id].mny ; i<=arr[id].mxy ; i++)
    {
        str[tx][i] = (id + 'A');
    }

    if(v == -1)
        arr[id].mnx--;

    else
        arr[id].mxx++;

    return 1 ;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tcase ;

    sf1(tcase);

    for(int cas=1 ; cas<=tcase ; cas++)
    {
        for(int i=0 ; i<30 ; i++)
            arr[i].ini();

        sf2(r,c);

        for(int i=0 ; i<r ; i++)
            sf("%s",str[i]);

        for(int i=0 ; i<25 ; i++)
        {
            clr(visit,0);

            dfs(0,0,i);

            if(arr[i].mnx != -1)
            {
                all.pb(i);
                fill_up(i);
            }
        }

        for(int i=0 ; i<all.size() ; i++)
        {
            while(cal_x(all[i],1));

            while(cal_x(all[i],-1));

            while(cal_y(all[i],1));

            while(cal_y(all[i],-1));
        }

        pf("Case #%d:\n",cas);

        for(int i=0 ; i<r ; i++)
        {
            for(int j=0 ; j<c ; j++)
                pf("%c",str[i][j]);

            pf("\n");
        }
    }

    return 0 ;
}
