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
#define sz              100+7
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
#define inf             1000000000000000LL

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
//
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

struct data
{
    int u ;
    double tme ;

    data() {}
    data(int u,double tme)
    {
        this->u = u ;
        this->tme = tme ;
    }

    bool operator < (const data& p)const
    {
        return tme>p.tme ;
    }
};

ll mat[sz][sz] ;
jora_ll horse[sz] ;
double tme[sz][sz] , needT[sz] ;
int n;

void dijkastra(int s)
{
    priority_queue<data>q ;
    data tp ;

    for(int i=0 ; i<sz ; i++)
        needT[i] = inf ;

    q.push(data(s,0));
    needT[s] = 0.0 ;

    double temp ;

    while(!q.empty())
    {
        tp = q.top();
        q.pop();

        for(int i=1 ; i<=n ; i++)
        {
            if(i == tp.u || tme[tp.u][i] == -1.0)
                continue;

            temp = needT[tp.u] + tme[tp.u][i] ;

            if(temp<needT[i])
            {
                needT[i] = temp ;
                q.push(data(i,needT[i]));
            }
        }
    }
}

int main()
{
    int tcase , q ;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    sf1(tcase);

    for(int cas=1 ; cas<=tcase ; cas++)
    {
        sf2(n,q);

        for(int i=1 ; i<=n ; i++)
            sf2ll(horse[i].fs,horse[i].sc);


        for(int i=1 ; i<=n ; i++)
        {
            for(int j=1 ; j<=n ; j++)
            {
                sf1ll(mat[i][j]);

                if(mat[i][j] == -1)
                    mat[i][j] = inf ;

                tme[i][j] = -1.0 ;
            }
        }

        for(int k=1 ; k<=n ; k++)
        {
            for(int i=1 ; i<=n ; i++)
            {
                for(int j=1 ; j<=n ; j++)
                {
                    mat[i][j] = min(mat[i][j],mat[i][k] + mat[k][j]);
                }
            }
        }

        for(int i=1 ; i<=n ; i++)
        {
            for(int j=1 ; j<=n ; j++)
            {
                if(i == j)
                    tme[i][j] = 0.0 ;

                else if(mat[i][j] != inf && horse[i].fs>=mat[i][j])
                    tme[i][j] = (double)mat[i][j]/(double)horse[i].sc ;
            }
        }

        int u , v ;

        pf("Case #%d:",cas);

        for(int i=0 ; i<q ; i++)
        {
            sf2(u,v);
            dijkastra(u);

            pf(" %.8f",needT[v]);
        }

        pf("\n");
    }

    return 0 ;
}
