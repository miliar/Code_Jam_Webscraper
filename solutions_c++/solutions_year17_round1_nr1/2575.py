

/*
    AUTHOR:hruday pabbisetty
    NIT ROURKElA
*/
#include <bits/stdc++.h>
using namespace std;
#define opt ios_base::sync_with_stdio(0)
#define lli long long int
#define ulli unsigned long long int
#define I int
#define S string
#define D double
#define rep(i,a,b) for(i=a;i<b;i++)
#define repr(i,a,b) for(i=a;i>b;i--)
#define in(n) scanf("%lld",&n)
#define in2(a,b) scanf("%lld %lld",&a,&b)
#define in3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define out(n) printf("%lld",n)
#define inu(a) scanf("%lld",&a)
#define outu(a) printf("%llu",a)
#define ins(s) scanf("%s",&s)
#define outs(s) printf("%s",s)
#define nl printf("\n")
#define mod 1000000007
#define inf 100000000000000
typedef long long       ll;
typedef pair<lli, lli>  plli;
typedef vector<lli>     vlli;
typedef vector<ulli>    vulli;
typedef vector<ll>      vll;
typedef vector<string>  vs;
typedef vector<plli>     vplli;
#define MM(a,x)  memset(a,x,sizeof(a));
#define ALL(x)   (x).begin(), (x).end()
#define P(x)       cerr<<"{"#x<<" = "<<(x)<<"}"<<endl;
#define P2(x,y)       cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<"}"<<endl;
#define P3(x,y,z)  cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<", "#z" = "<<(z)<<"}"<<endl;
#define P4(x,y,z,w)cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<", "#z" = "<<(z)<<", "#w" = "<<(w)<<"}"<<endl;
#define PP(x,i)     cerr<<"{"#x"["<<i<<"] = "<<x[i]<<"}"<<endl;
#define TM(a,b)     cerr<<"{"#a" -> "#b": "<<1000*(b-a)/CLOCKS_PER_SEC<<"ms}\n";
#define UN(v)    sort(ALL(v)), v.resize(unique(ALL(v))-v.begin())
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define sz() size()
lli power(lli a,lli b)
    {
    lli value;
    if(b==0)
        {
        return 1;
    }
    else if(b%2==0)
        {
        value=power(a,b/2)%mod;
        return(value*value)%mod;
    }
    else
        {
        value=power(a,b/2)%mod;
        return ((a*value)%mod*(value))%mod;
    }
}
int main()
{

    #ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        freopen("q1output3.txt","w",stdout);
        #endif
    opt;
    lli t,z;
    cin>>t;
    rep(z,1,1+t)
    {
        lli n,m,i,j;
        cin>>n>>m;
        char ch[n][m],ch1;
        vector<char>v,v1[n];
        lli a[105]={0},al[26]={0};
        rep(i,0,n)
        {
            rep(j,0,m)
            {
                cin>>ch[i][j];
                if(ch[i][j]!='?')
                {
                    a[i]++;
                    v1[i].pb(ch[i][j]);
                    al[ch[i][j]-'A']=1;
                }
            }
        }
        rep(i,0,26)
        {
            if(!al[i])
            {
                v.pb('A'+i);
            }
        }
        lli index,maxi=-inf;
        rep(i,0,n)
        {
            if(a[i]!=0)
            {
                index=i;
                break;
            }
        }
        lli cnt=0;
        rep(i,0,n)
        {
            if(a[i]==0)
            {
                continue;
            }
            else
            {
                lli temp=0;
                rep(j,0,m)
                {
                    if(ch[i][j]=='?')
                    {
                        ch[i][j]=v1[i][temp];
                    }
                    else
                    {
                        temp++;
                        lli temp2=v1[i].sz()-1;
                        temp=min(temp,temp2);
                    }
                }
            }
        }
        repr(i,index-1,-1)
        {
            if(a[i]==0)
            {
                rep(j,0,m)
                {
                    ch[i][j]=ch[i+1][j];
                }
            }
        }
        rep(i,index+1,n)
        {
            if(a[i]==0)
            {
                rep(j,0,m)
                {
                    ch[i][j]=ch[i-1][j];
                }
            }
        }
        cout<<"Case #"<<z<<":"<<endl;
        rep(i,0,n)
        {
            rep(j,0,m)
            {
                cout<<ch[i][j];
            }
            cout<<endl;
        }
    }
}
