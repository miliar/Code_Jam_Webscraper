#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<long long int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;

#define mod 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define forn(i, n) for(ll i = 0; i < ll(n); ++i)
#define forv(i, n) for(int i = 0; i != int(n); ++i)
#define cases int t;  cin>>t;   while(t--)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int main()
{
    fast_io;
    freopen("B-large.txt","r",stdin);
    freopen("B-large output.txt","w",stdout);
    int t;
    cin>>t;
    forn(c,t)
    {
        string s;
        cin>>s;
        int a[20],n=s.length(),pos=0,f=0;
        forn(i,n)
            a[i]=s[i]-'0';
        forn(i,n-1)
            if(a[i]<a[i+1])
                pos=i+1,f=0;
            else if(a[i]==a[i+1])
            {
                f++;
                if(f==1)
                    pos=i;
            }
            else
            {
                a[pos]--;
                for(int i=pos+1;i<n;i++)
                    a[i]=9;
                break;
            }
        forn(i,n)
            if(a[i]!=0)
            {
                pos=i;
                break;
            }
        cout<<"Case #"<<c+1<<": ";
        for(int i=pos;i<n;i++)
            cout<<a[i];
        cout<<"\n";
    }
    return 0;
}
