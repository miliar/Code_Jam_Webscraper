#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<set>
#include<string.h>
#include<algorithm>
#include<math.h>
#define F first
#define S second
#define sd(n) scanf("%d",&n)
#define sdd(m,n) scanf("%d %d",&m,&n)
#define sl(n) scanf("%lld",&n)
#define sll(m,n) scanf("%lld %lld",&m,&n)
#define sc(n) scanf("%c",&n)
#define ss(n) scanf("%s",n)
#define pd(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define pc(n) printf("%c ",n)
#define ps(n) printf("%s ",n)
#define NL printf("\n")
#define pb(n) push_back(n)
#define sz size()
#define clr(v,a,b) for(int i=a;i<=b;i++)v[i].clear()
#define all(v) v.begin(),v.end()
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
/*#include<fstream>
ifstream fin("in.txt");
ofstream fout("out.txt");*/
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const int MXN=100005;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int dxx[8]={0,1,1,1,0,-1,-1,-1};
int dyy[8]={1,1,0,-1,-1,-1,0,1};
char s[30][30];
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out1l.txt","w",stdout);
    int t;
    sd(t);
    for(int tc=1;tc<=t;tc++)
    {
        vector< pii > v;
        int r,c;
        sdd(r,c);
        for(int i=0;i<r;i++)
        {
            ss(s[i]);
            for(int j=0;j<c;j++)
            {
                if(s[i][j]!='?')
                v.pb(pp(i,j));
            }
        }
        for(int i=0;i<v.sz;i++)
        {
            int p=v[i].F;
            int q=v[i].S;
            int mu=-1,md=1000;
            char c=s[p][q];
            int ml=q,mr=q;
            for(int rr=q;rr<c;rr++)
            {
                if(s[p][rr]==c||s[p][rr]=='?')
                {
                    int k=p-1;
                    while(k>=0&&s[k][rr]=='?'&&k>=mu)
                        k--;
                    k++;
                    mu=k;
                    k=p+1;
                    while(k<r&&s[k][rr]=='?'&&k<=md)
                        k++;
                    k--;
                    md=k;
                    mr=rr;
                }
                else
                    break;
            }
            for(int rr=q;rr>=0;rr--)
            {
                if(s[p][rr]==c||s[p][rr]=='?')
                {
                    int k=p-1;
                    while(k>=0&&s[k][rr]=='?'&&k>=mu)
                        k--;
                    k++;
                    mu=k;
                    k=p+1;
                    while(k<r&&s[k][rr]=='?'&&k<=md)
                        k++;
                    k--;
                    md=k;
                    ml=rr;
                }
                else
                    break;
            }
            //cout<<p<<" "<<q<<" "<<c<<" ml="<<ml<<" mr="<<mr<<" mu="<<mu<<" md="<<md<<endl;
            for(int j=mu;j<=md;j++)
            {
                for(int k=ml;k<=mr;k++)
                    s[j][k]=c;
            }
        }
        printf("Case #%d:\n",tc);
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
                printf("%c",s[i][j]);
            NL;
        }
    }
    return 0;
}


