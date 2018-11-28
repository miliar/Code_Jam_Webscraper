using namespace std;
#include<bits/stdc++.h>

#define db          double
#define ll          long long
#define ull         unsigned long long

#define vi          vector<int>
#define vl          vector<long>
#define vll         vector<ll>

#define mii         map<int,int>
#define mll         map<ll,ll>

#define pi          pair<int,int>
#define pl          pair<long,long>
#define pll         pair<ll,ll>

#define pb          push_back
#define mp          make_pair
#define fs          first
#define sc          second

#define pf          printf
#define sf          scanf
#define II          ({int a; _in(a); a;})
#define IL          ({long a; _in(a); a;})
#define ILL         ({ll a; _in(a); a;})
#define ID          ({db a; sf("%lf",&a); a;})
#define IF          ({float a; sf("%f",&a); a;})
#define IC          ({char a; sf("%c",&a); a;})
#define IS          ({string a; _in_cin_string(a); a;})

#define repI(i,b,c)  for(int i=b;   i<=c; i++)
#define repL(i,b,c)  for(long i=b;  i<=c; i++)
#define repLL(i,b,c) for(ll i=b;    i<=c; i++)

#define all(V)      V.begin(),V.end()
#define clr(A,B)    memset(A,B,sizeof A)

#define _F_in       freopen("A-large.in","r",stdin)
#define _F_out      freopen("A-large.out","w",stdout)

#define PI          2*acos(0.0)
#define mod         1000000007
#define INF         LLONG_MAX
#define sqr(n)      (n*n)

#define endl	    '\n'

template <typename T>inline T BigMod (T b,T p,T m){if (p == 0) return 1;if (p%2 == 0){T s = BigMod(b,p/2,m);return ((s%m)*(s%m))%m;}return ((b%m)*(BigMod(b,p-1,m)%m))%m;}
template <typename T>inline T ModInv (T b,T m){return BigMod(b,m-2,m);}
template <typename T>inline T Bigmod(T b,T p,T m){ if(p==0) return 1; else if (!(p&1)) return sqr(Bigmod(b,p/2,m)) % m;else return ((b % m) * Bigmod(b,p-1,m)) % m;}
template <typename T>inline T gcd(T a,T b){ if(b==0)return a; return gcd(b,a%b);}
template <typename T>inline T lcm(T a,T b) {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template <typename T>inline T euclide(T a,T b,T &x,T &y) {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template <typename T>inline T Dis(T x1,T y1,T x2, T y2){return sqrt( (sqr((x1-x2)) + sqr((y1-y2))) );}
template <typename T>inline T Angle(T x1,T y1,T x2, T y2){ return atan(double(y1-y2) / double(x1-x2));}
template <typename T>inline T DIFF(T a,T b) { T d = a-b;if(d<(T)0)return -d;else return d;}
template <typename T>inline T ABS(T a) {if(a<0)return -a;else return a;}
template <typename T>inline ll isLeft(T a,T b,T c) { return (a.x-b.x)*(b.y-c.y)-(b.x-c.x)*(a.y-b.y); }

template <typename T>inline void _in(T &x){register int c = getchar();x = 0;bool neg = 0;for(;((c<48 | c>57) && c != '-');c = getchar()); if(c=='-') {neg=1;c=getchar();}for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}if(neg) x=-x;}

template <typename T>inline bool isLeapYear(T N){ if (N%4) return 0; else if (N%100) return 1; else if (N%400) return 0; else return 1; }
template <typename T>inline T Set(T N,T pos){ T A = 1; return N=N | (A<<pos);}
template <typename T>inline T Reset(T N,T pos){ T A = 1; return N= N & ~(A<<pos);}
template <typename T>inline bool Check(T N,T pos){T A=1; return (bool)(N & (A<<pos));}
template <class T, class X>inline T togglebit(T a, X i) { T t=1;return (a^(t<<i)); }

template <class T, class X>inline T toInt(T &sm, X s) {stringstream ss(s); ss>>sm; return sm;}
template <typename T>inline int cdigittoint(T ch){return ch-'0';}
template <typename T>inline bool isVowel(T ch){ ch=toupper(ch); if(ch=='A'||ch=='U'||ch=='I'||ch=='O'||ch=='E') return true; return false;}
template <typename T>inline bool isConst(T ch){if (isalpha(ch) && !isVowel(ch)) return true; return false;}


inline double DEG(double x) { return (180.0*x)/(PI);}
inline double RAD(double x) { return (x*(double)PI)/(180.0);}

//Knight Move
//ll dx[]= {-1, -2, -2, -1, +1, +2, +2, +1};
//ll dy[]= {-2, -1, +1, +2, +2, +1, -1, -2};

//8 Direction
//ll dx[]={-1, -1, -1, 0, +1, +1, +1, 0};
//ll dy[]={-1, 0, +1, +1, +1, 0, -1, -1};

//4 Direction
//ll dx[]={0, +1, 0, -1};
//ll dy[]={+1, 0, -1, 0};

///------------------------------------------------------///

int main()
{
    _F_in;
    _F_out;
    ll t=ILL;
    repLL(cs, 1, t)
    {
        string A,B;
        ll k;
        cin>>A>>k;
        B=A;
        ll Ans1=0, Ans2=0;
        for(ll i=0; i<A.length(); i++)
        {
            if(A[i]=='+')
                continue;
            else
            {
                Ans1++;
                if(A.length()-i>=k)
                {
                    for(ll j=i; j<i+k; j++)
                    {
                        if(A[j]=='-')
                            A[j]='+';
                        else
                            A[j]='-';
                    }
                }
            }
        }
        bool flag=1;
        for(ll i=0; i<A.length(); i++)
        {
            if(A[i]=='+')
                continue;
            else
            {
                flag=0;
                Ans1=(ll)mod;
                break;
            }
        }
//        cout<<Ans1<<endl;
        for(ll i=B.length()-1; i>=0; i--)
        {
            if(B[i]=='+')
                continue;
            else
            {
                Ans2++;
                if(i+1>=k)
                {
                    for(ll j=i; j>i-k; j--)
                    {
                        if(B[j]=='-')
                            B[j]='+';
                        else
                            B[j]='-';
                    }
                }
            }
        }
//        cout<<Ans2<<endl;
        flag=1;
        for(ll i=0; i<B.length(); i++)
        {
            if(B[i]=='+')
                continue;
            else
            {
                flag=0;
                Ans2=(ll)mod;
                break;
            }
        }
        ll Ans = min(Ans1, Ans2);
        pf("Case #%lld: ",cs);
        if(Ans!=(ll)mod)
            pf("%lld\n",Ans);
        else
            pf("IMPOSSIBLE\n");
    }
    return 0;
}
