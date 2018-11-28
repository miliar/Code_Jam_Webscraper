#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pll pair<LL, LL>
#define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define fs first
#define sc second

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define EPS 1e-6
#define MOD (1000000007)
//#define PI  2*acos(0);

#define fore(iter,v) for(iter=v.begin(); iter!=v.end(); iter++)
#define forup(i,a,n) for(i=a; i<n; i++)
#define rep(i,n) for(i=0; i<n; i++)
#define SET(a, v) memset(a, v, sizeof a)
#define all(a) a.begin(),a.end()
#define ALLOC0(N)   (int*)calloc(N, sizeof(int));

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)


#define ps(x) printf("%s",x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pn printf("\n")
#define spc printf(" ")
#define gc getchar

struct ma
{
    ll r,h,rh,i;
};

struct ma1
{
    ll val,i,rh;
};

bool fun(ma m1,ma m2)
{
    return m1.rh>m2.rh;
}

bool fun1(ma1 m1,ma1 m2)
{
    return m1.val>m2.val;
}


int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,bk;
    cin>>t;
    const double PI  =3.141592653589793238463;
    //cout<<"PI:"<<PI<<endl;
    for(bk=1;bk<=t;bk++)
    {
        cout<<"Case #"<<bk<<": ";

        ll n,k,temp,m=INF_MIN,i,j,su,p;
        double ans;
        ma temp1;
        ma1 temp2;
        vector<ma> v;
        vector<ma1> c;
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            cin>>temp;
            temp1.r=temp;
            temp1.i=i;
            temp2.i=i;
            temp2.val=temp;


            cin>>temp;
            temp1.h=temp;
            temp1.rh=temp1.r*temp1.h;
            temp2.rh=temp1.rh;

            c.push_back(temp2);
            v.push_back(temp1);
        }
        sort(v.begin(),v.end(),fun);
        sort(c.begin(),c.end(),fun1);
        /*for(i=0;i<n;i++)
        {
            cout<<"I:"<<i<<" val:"<<v[i].rh<<endl;
            cout<<" val2:"<<c[i].val<<endl;
        }
        cout<<endl;*/
        for(i=0;i<=n-k;i++)
        {
            //cout<<" I:"<<i<<" val2:"<<c[i].val<<" "<<c[i].i<<endl;
            su=c[i].val*c[i].val+2*c[i].rh;
            j=1;
            p=0;
            while(p<n && j!=k)
            {
                //cout<<"P:"<<p<<" J:"<<j<<" R:"<<v[p].r<<" "<<v[p].i<<endl;
                if(v[p].r<=c[i].val && v[p].i!=c[i].i)
                {
                    su+=2*v[p].rh;
                    j++;
                }
                p++;
            }
            if(j==k)
            {
                m=max(m,su);
            }
        }
        ans=(double)PI*m;
        cout<<setprecision(9)<<fixed<<ans<<endl;
        //cout<<m<<endl<<endl<<endl;
    }
    return 0;
}
