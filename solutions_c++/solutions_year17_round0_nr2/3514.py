#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cerr << #x " = " << (x) << '\n'
#define DBG         cerr << "Hi" << '\n'
#define pb          push_back
#define PI          acos(-1.00)
#define xx          first
#define yy          second
#define eps         1e-9

typedef unsigned long long int ULL;
typedef long long int LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;


inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

LL n;
int decimalN[100];
bool dp[70][2];
int vis[70][2], cs;
vector<int>sltn;
bool call(int pos, bool smaller, int last)
{
    if(pos == -1)
        return true;
    bool &ret = dp[pos][smaller];
    if(vis[pos][smaller] == cs)
        return ret;
    ret = false;
    vis[pos][smaller] = cs;
    if(smaller)
    {
        call(pos-1, smaller, 9);
        return ret = true;
    }
    for(int i = decimalN[pos]; i>=last; i--)
    {
        if(call(pos-1, smaller | (decimalN[pos] > i), i))
            return ret = true;
    }
    return ret;
}

void printPath(int pos, bool smaller, int last)
{
    if(pos == -1)
        return;
    if(smaller)
    {
        sltn.pb(9);
        printPath(pos-1, smaller, 9);
        return;
    }
    for(int i = decimalN[pos]; i>=last; i--)
    {
        if(call(pos-1, smaller | (decimalN[pos] > i), i))
        {
            sltn.pb(i);
            printPath(pos-1,smaller | (decimalN[pos] > i), i);
            return;
        }
    }
}

void make(LL n)
{
    int pos = 0;
    while(n)
    {
        decimalN[pos] = n%10;
        pos++;
        n/=10;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, t;
    sf(t);
    FRE(cs,1,t)
    {
        mem(decimalN,0);
        sltn.clear();
        sl(n);
        printf("Case #%d: ",cs);
        make(n);
//        for(int i = 20; i>=0; i--)
//            cout << decimalN[i];
//        cout << endl;
        call(20, 0, 0);
        printPath(20,0,0);
        bool found = false;
        for(int i = 0; i<sltn.size(); i++)
        {
            if(sltn[i])
                found = true;
            if(found)
                printf("%d",sltn[i]);
        }
        if(!found)
            printf("0");
        puts("");
    }
    return 0;
}


