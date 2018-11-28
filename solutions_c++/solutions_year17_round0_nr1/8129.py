/*   ayushkmr                 **
**   Ayush Kumar			  **
**   IIT (ISM) Dhanbad        */
#include<bits/stdc++.h>
#define gc getchar
#define pc putchar
#define pb(x) push_back(x)
#define eb(x) emplace_back(x)
#define mp(x,y) make_pair((x),(y))
#define sz size()
#define ff first
#define ss second
#define ins insert
#define all(x) (x).begin(),(x).end()
#define mset(m,v) memset(m,v,sizeof(m))
#define Abs(a,b) ((a) < (b) ? (b)-(a) : (a)-(b))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define remax(a,b) (a)=max((a),(b));
#define remin(a,b) (a)=min((a),(b));
#define nu 1005
#define pnu 1000100
#define MOD 1000000007
#define MAX 2000000000
#define MAXL 2000000000000000000LL
#define nmod(a,b) ((a%b)+b)%b
 
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef stack<int> sti;
typedef queue<int> qi;
typedef pair<int,int> ii;
typedef pair<ii,ii> iii;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef priority_queue<int> pq;
inline ll in()
{
    ll NR=0;
    register char c=gc();
    while( c < 48 || c > 57 ){c=gc();}
    while(c>47 && c< 58)
    {
		NR = (NR << 3) + (NR << 1) + (c - 48);
		c=gc();
    }
    return NR;
}
int main()
{
	//ios::sync_with_stdio(false);
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    ll t=in(),i,k,l,an,ii,j;
    string s;
    for(ii=1;ii<=t;ii++)
        {
        cin>>s>>k;
        l=s.length();
        an=0;
        for(i=0;i<=l-k;i++)
            {
            if(s[i]=='-')
                {
                for(j=i;j<i+k;j++)
                    {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                an++;
            }
        }
        for(i=0;i<l;i++)
            {
            if(s[i]=='-')
                {
                cout<<"Case #"<<ii<<": IMPOSSIBLE\n";
                break;
            }
        }
        if(i==l)
            {
            cout<<"Case #"<<ii<<": "<<an<<"\n";
        }
    }
	return 0;
}
