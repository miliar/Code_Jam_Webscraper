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

//int ar[1000001];
ll n,k;

     int main()
     {
     freopen("jaminpc.txt","r",stdin);
     freopen("jamoutc.txt","w",stdout);
     scanf("%d",&t);
     q=0;
     while(t--)
     {
         map<ll,ll>mapp;

         ll ans1=0,ans2=0;
         q++;
     	scanf("%lld %lld",&n,&k);
     	 mapp[n]=1;
set<pair<ll,ll> > qu;
          qu.insert(make_pair(n,1));
          while(qu.size()>=1)
          {
              auto it=qu.end();
              it--;
              pair<ll,ll>pa=*it;
              ll quan=pa.se;
              ll si=pa.fi;
              qu.erase(qu.find(make_pair(si,quan)));

              if(k-quan<=0)
              {
                  if(si%2==0)
                  {


                    ans1=si/2;
                    ans2=ans1-1;
                  }
                  else
                  {

                      ans1=si/2;
                    ans2=ans1;
                  }

                  break;
              }
              else
              {

                  mapp[si]-=quan;
              k-=quan;
//cout<<si<<" "<<quan<<" "<<k<<endl;
              if(si&1)
              {
                  if(qu.find(make_pair(si/2,mapp[si/2]))!=qu.end())
            qu.erase(qu.find(make_pair(si/2,mapp[si/2])));
              mapp[si/2]+=(2*quan);
                  qu.insert(make_pair((si/2),mapp[si/2]));
              }
                else
                {
                    if(qu.find(make_pair(si/2,mapp[si/2]))!=qu.end())
 qu.erase(qu.find(make_pair(si/2,mapp[si/2])));
 if(qu.find(make_pair((si/2)-1,mapp[(si/2)-1]))!=qu.end())
  qu.erase(qu.find(make_pair((si/2)-1,mapp[(si/2)-1])));
                mapp[si/2]+=quan;
                mapp[(si/2)-1]+=quan;
              qu.insert(make_pair(si/2,mapp[si/2]));
              qu.insert(make_pair((si/2)-1,mapp[(si/2)-1]));
                }
              }

          }
  printf("Case #%d: %lld %lld\n",q,ans1,ans2);

     }



    return 0;
     }
