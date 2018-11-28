using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
#define MOD 1000000007
#define foreach(it, l) for (auto it = l.begin(); it != l.end(); it++)
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define mx 0
int main() {
    ios_base::sync_with_stdio(0);
    int i,j,k,t,s,count;
    st a;
    cin>>t;
    count=1;
    while(count<=t)
    {
        count++;
        cin>>a;
        s=a.size();
        i=0;
        while(i<s-1&&a[i]<=a[i+1])
        {
            i++;
        }
        if(i!=s-1)
        {
            for(j=i;j>0;j--)
            if(a[j]!=a[j-1])
            break;
            a[j]--;
            for(k=j+1;k<s;k++)
            a[k]='9';
        }
        cout<<"Case #"<<count-1<<": ";
        if(a[0]=='0')
        a.erase(a.begin());
        cout<<a;
        cout<<endl;
    }
    return 0;
}
