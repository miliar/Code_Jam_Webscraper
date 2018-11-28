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
#define PI  2*acos(0);

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
    ll v,d;
};

bool fun(ma m1,ma m2)
{
    return m1.d<m2.d;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,bk;
    cin>>t;
    for(bk=1;bk<=t;bk++)
    {
        cout<<"Case #"<<bk<<": ";
        vector<ma> ve;
        ma temp2;
        ll da,n,i,temp,la;
        double dis,temp1;

        cin>>da>>n;
        //cout<<" da:"<<da<<" N:"<<n<<endl;
        temp1=(double)da;
        for(i=0;i<n;i++)
        {
            cin>>temp;
            temp2.d=temp;
            cin>>temp;
            temp2.v=temp;
            ve.push_back(temp2);
        }
        sort(ve.begin(),ve.end(),fun);
        la=0;
        for(i=1;i<n;i++)
        {
            //cout<<"I:"<<i<<" D:"<<ve[i].d<<" V:"<<ve[i].v<<endl;
            //cout<<"Il:"<<la<<" Dl:"<<ve[la].d<<" Vl:"<<ve[la].v<<endl;
            if(ve[i].v<ve[la].v)
            {
                dis=(double)(ve[i].v*(ve[i].d-ve[la].d))/(ve[la].v-ve[i].v);
                dis=dis+ve[i].d;
                //cout<<" DIS:"<<dis<<endl;
                //cout<<" temp1:"<<temp1<<endl;
                if(dis<=temp1)
                {
                    la=i;
                }
            }
        }
        //cout<<"N:"<<n<<" LA:"<<la+1<<endl;
        temp1=da*ve[la].v;
        temp1=(double)(temp1/(da-ve[la].d));
        cout<<setprecision(6)<<fixed<<temp1<<endl;
    }
    return 0;
}
