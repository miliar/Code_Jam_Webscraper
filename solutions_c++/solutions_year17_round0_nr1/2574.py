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
int n,k;

     int main()
     {
     freopen("jaminpc.txt","r",stdin);
     freopen("jamoutc.txt","w",stdout);
     scanf("%d",&t);
     q=0;
     while(t--)
     {
      q++;
      string str;
      cin>>str>>k;
      l=str.size();
      int rekt=1;
string str1=str;
          cnt=0;
          for(i=0;i<=l-k;i++)
          {
              if(str[i]=='+')
                continue;
              cnt++;
              for(j=i;j<i+k;j++)
              {



                  if(str[j]=='-')
                  str[j]='+';
                  else str[j]='-';

              }
          }
          int cnt1=0;
          for(i=0;i<l;i++)
          {

              if(str[i]=='+')
                cnt1++;
          }
          if(cnt1!=l)
{
    str=str1;
 cnt=0;
          for(i=l-1;i>=k-1;i--)
          {
              if(str[i]=='+')
                continue;
              cnt++;
              for(j=i;j>i-k;j--)
              {



                  if(str[j]=='-')
                  str[j]='+';
                  else str[j]='-';

              }
          }
          cnt1=0;
          for(i=0;i<l;i++)
          {

              if(str[i]=='+')
                cnt1++;
          }
          if(cnt1!=l)
{
  printf("Case #%d: IMPOSSIBLE\n",q);
}
else
     printf("Case #%d: %d\n",q,cnt);
}
  else
{

    str=str1;
int  cnt3=0;
          for(i=l-1;i>=k-1;i--)
          {
              if(str[i]=='+')
                continue;
              cnt3++;
              for(j=i;j>i-k;j--)
              {



                  if(str[j]=='-')
                  str[j]='+';
                  else str[j]='-';

              }
          }
          cnt1=0;
          for(i=0;i<l;i++)
          {

              if(str[i]=='+')
                cnt1++;
          }

int  cnt2=1000000000;
if(cnt1==l)
    cnt2=cnt3;
   printf("Case #%d: %d\n",q,min(cnt,cnt2));
}

     }



    return 0;
     }
