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

bool A[1010];
int k;
void flip(int idx)
{
    for(int i = idx, cnt = 1; cnt<=k; i++,cnt++)
        A[i] = A[i]^1;
}
int n;
void print()
{
    for(int i = 0; i<n ; i++)
        cout << (int) A[i] ;
    cout << endl;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, cs, t;
    string s;
    sf(t);
    FRE(cs,1,t)
    {
        cin >> s;
        FRL(i,0,s.size())
        {
            if(s[i] == '-')
                A[i] = 0;
            else
                A[i] = 1;
        }
        n = s.size();
//        print();
        sf(k);
        int ans = 0;
        for(i = 0; i<=(int)s.size()-k; i++)
        {
            if(A[i] == 0)
                ans++,flip(i);
        }
        bool ok = true;
        for(i = 0; i<(int)s.size(); i++)
        {
            if(A[i] == 0)
                ok = false;
        }
        printf("Case #%d: ",cs);
        if(!ok)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);

    }
    return 0;
}


