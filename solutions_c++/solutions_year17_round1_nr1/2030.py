#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector< pair<int,int> > vpii;
typedef vector< pair<ll,ll> > vpll;
typedef vector< vector<int> > matrix;

#define SET(Ar,val) memset(Ar,val,sizeof(Ar))
#define rep(i,val,n)  for(int i=val;i<n;i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define LMAX LONG_LONG_MAX
#define LMIN LONG_LONG_MIN
#define IMAX INT_MAX
#define IMIN INT_MIN
#define M 1000000007

/*--------------------------------------------------------------------------------------------------------------------------------*/

template <class T> T modpower(T a,T b,T MOD)
{
    T ans=1;
    while(b!=0)
    {
        if(b%2==1)
        ans=(ans*a)%MOD;
        a=(a*a)%MOD;
        b/=2;
    }
    return ans;
}

void init()
{
    int t;
    cin >> t;
    rep(ca,1,t+1)
    {
        int r,c;
        cin >> r >> c ;
        string s[r+5];
        rep(i,0,r)
        cin >> s[i];
        rep(i,0,r)
        {
            int j=0,k=0;
            while(j<c)
            {
                if(s[i][j]=='?')
                j++;
                else
                {
                    if(k<=j)
                    {
                        while(k<j)
                        {
                            s[i][k]=s[i][j];
                            k++;
                        }
                        k++;
                        j++;
                        while(s[i][j]=='?')
                        {
                            s[i][j]=s[i][j-1];
                            k++;
                            j++;
                        }
                    }
                }
            }
        }
        rep(i,0,r)
        {
            if(s[i][0]=='?')
            {
                int j=i+1,fg=0;
                while(j<r)
                {
                    if(s[j][0]!='?')
                    {
                        fg=1;
                        break;
                    }
                    j++;
                }
                if(fg==1)
                for(int u=j-1;u>=i;u--)
                {
                    for(int v=0;v<c;v++)
                    {
                        s[u][v]=s[u+1][v];
                    }
                }
                if(fg==0)
                {
                    j=i-1;
                    while(j>=0)
                    {
                        if(s[j][0]!='?')
                        {
                            fg=1;
                            break;
                        }
                        j--;
                    }
                    for(int u=j+1;u<=i;u++)
                    {
                        for(int v=0;v<c;v++)
                        s[u][v]=s[u-1][v];
                    }
                }
            }
        }
    cout << "Case #" << ca << ":" << endl ;
    rep(i,0,r)
    {
        rep(j,0,c)
        cout << s[i][j];
        cout << endl ;
    }
    }
}

int main()
{
    clock_t time1 = clock();
	#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	#else
	//ONLINE_JUDGE
	#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    init();
    clock_t time2 = clock();
    cerr <<"Time: " <<(double)(time2-time1)/CLOCKS_PER_SEC <<" seconds" <<endl;
	return 0;
}
