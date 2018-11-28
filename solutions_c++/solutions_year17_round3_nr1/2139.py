//Author: AKSHAY VASANDANI FROM JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY



    //#include <ext/pb_ds/assoc_container.hpp>
    //#include <ext/pb_ds/tree_policy.hpp>
    #define ll long long
    #define gcd __gcd
    #include<bits/stdc++.h>
    #define fi first
    #define se second
    #define mod 1000000007
    #define pb push_back
    #define N 100001
    #define eb emplace_back
    #define gc getchar_unlocked
    #define LN 20
    //#include <boost/multiprecision/cpp_int.hpp>
    //#define bigint boost::multiprecision::cpp_int

    using namespace std;
    /*using namespace __gnu_pbds;
    typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
    ordered_set;
     */

     ll p(ll a,ll b)
    {
        ll temp;
        if(b==0)
        return 1;
        temp=p(a,b/2)%mod;
        if(b&1)
        return (((a*temp)%mod)*temp)%mod;
        else
        return (temp*temp)%mod;
    }

  ll p1(ll a,ll b)
    {
        ll temp;
        if(b==0)
        return 1;
        temp=p1(a,b/2);
        if(b&1)
        return (((a*temp))*temp);
        else
        return (temp*temp);
    }
     int m,q,u,h,t,a,b,c,d;
     int s,de,f,e,g,cnt,l,x,y,r,mi,ma;
     int i,j,num,ans1,ans,sq;

int ar[1000001];
int n,k;
int radius[100001],height[100001];
     int main()
     {
     freopen("rc.txt","r",stdin);
     freopen("rco.txt","w",stdout);
     scanf("%d",&t);
     q=0;
     h=0;
     while(t--)
     {
      q++;
     scanf("%d %d",&n,&k);
   for(i=0;i<n;i++)
   {

       scanf("%d %d",&radius[i],&height[i]);
   }

x=p(2,n);
x--;
ll ans=0;
for(i=1;i<=x;i++)
{
    h=0;
    for(j=0;j<n;j++)
    {

        if(i&(1<<j))
        {

            ar[h++]=j;
        }
    }
if(h!=k)
    continue;
    pair<int,int> ar1[20];
    for(j=0;j<h;j++)
    {
        ar1[j].fi=radius[ar[j]];
        ar1[j].se=height[ar[j]];
    }
    sort(ar1,ar1+h);
    reverse(ar1,ar1+h);
    ll res=(2*(ll)ar1[0].fi*(ll)ar1[0].se);
    //cout<<res<<endl;



    for(j=0;j<h-1;j++)
    {
   // ll a1=ar1[j+1].fi-ar1[j].fi;
     res+=(((ll)ar1[j].fi*(ll)ar1[j].fi)-((ll)ar1[j+1].fi*(ll)ar1[j+1].fi));
     res+=(2*(ll)ar1[j+1].fi*(ll)ar1[j+1].se);
//    }
    }
    res+=((ll)ar1[h-1].fi*(ll)ar1[h-1].fi);

    if(res>ans)
        ans=res;
}
//cout<<ans<<endl;
double d1 = 3.14159265358979*(double)ans;
int precision = std::numeric_limits<double>::max_digits10;
std::cout <<"Case #"<<q<<": "<<std::setprecision(precision) << d1 << std::endl;
//printf("%lf\n",3.14159*(double)ans);

     }

    return 0;
     }
