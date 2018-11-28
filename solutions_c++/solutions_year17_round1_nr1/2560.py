# include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

// Input macros
#define s(n)                        scanf("%d",&n)
#define p(n)                        printf("%d\n",n)
#define pl(n)                       printf("%lld\n",n);
#define INF                         (int)1e9
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define mod 1000000007LL

// Useful container manipulation / traversal macros
#define all(n)                      for(int i=0;i<n;i++)
#define alls(m)                     for(int j=0;j<m;j++)
#define rep(a,n)                    for(int i=a;i<n;i++)
#define each(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all1(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define init(Arr) memset((Arr), 0, sizeof (Arr))


int main()
{
    int cases;
    s(cases);

    for(int t=1;t<=cases;t++)
    {
        printf("Case #%d:\n",t);

        int r,c;
        s(r);
        s(c);

        char m[26][26];

        for(int i=0;i<r;i++)
        {
            scanf("%s",m[i]);
        }

        for(int j=0;j<c;j++)
        {
            for(int i=0;i<r;i++)
            {
                if(m[i][j] != '?')
                {
                    for(int k=i+1;k<r && m[k][j] == '?';k++)
                    {
                        m[k][j] = m[i][j];
                    }

                    for(int k=i-1;k>=0 && m[k][j] == '?';k--)
                    {
                        m[k][j] = m[i][j];
                    }
                }
            }
        }

        for(int i=0;i<r;i++) 
        {
            for(int j=0;j<c;j++)
            {
                if(m[i][j] != '?')
                {
                    for(int k=j+1;k<c && m[i][k] == '?';k++)
                    {
                        m[i][k] = m[i][j];
                    }

                    for(int k=j-1;k>=0 && m[i][k] == '?';k--)
                    {
                        m[i][k] = m[i][j];
                    }
                }   
            }
        }

        for(int i=0;i<r;i++)
            cout<<m[i]<<endl;
    }
}
