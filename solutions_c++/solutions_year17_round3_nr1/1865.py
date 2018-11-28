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
const double pi=3.14159265359;
class obj
{
    public:
    i64 id;
i64 r;
int h;
i64 rh;
};
bool cmprh(obj o1,obj o2)
{
    return(o1.rh>o2.rh);
}
bool cmpr(obj o1,obj o2)
{
    return(o1.r>o2.r);
}

int main() {
    ios_base::sync_with_stdio(0);
    int n,k,t,count=1;
    long double ans,a1;
    obj rad[1000],radh[1000];
    cin>>t;
    while(count<=t)
    {
        count++;
        a1=ans=0.0;
        cin>>n>>k;
        rep(i,n)
        {
            cin>>rad[i].r>>rad[i].h;
            rad[i].rh=rad[i].r*rad[i].h;
            radh[i]=rad[i];
            rad[i].id=radh[i].id=i;
        }   
        sort(rad,rad+n,cmpr);
        sort(radh,radh+n,cmprh);
        // rep(i,n)
        // cout<<rad[i].id;
         rep(i,n-k+1)
        {
            a1=1.0*rad[i].r*(rad[i].r+2*rad[i].h);
            //cout<<"Ss"<<a1;
            int l=1;
            rep(j,n)
            {
                if(l==k)break;
                if(rad[i].id==radh[j].id)
                continue;
                else if(radh[j].r>rad[i].r)
                continue;
                else
                {
                    a1+=2*radh[j].rh;
                    l++;
                }
            }
            if(a1>ans)
            ans=a1;
        }
        //cout<<pi<<endl;
        cout<<"Case #"<<count-1<<": ";
        cout<<fixed<<setprecision(9)<<1.0*pi*ans;
        cout<<endl;
    }
    return 0;
}
