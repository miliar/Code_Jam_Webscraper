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
//int n,k;
ll n;

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
      cin>>str;
      l=str.size();
for(a=1;a<=19;a++)
{
l=str.size();
f=0;
      for(i=0;i<l-1;i++)
      {
          if(str[i]>str[i+1])
          {

              str[i]=(char)((int)str[i]-1);
              f=1;
              break;
          }

      }
      if(f==1)
      for(j=i+1;j<l;j++)
        str[j]='9';
        string str1="";
     i=0;

         while(i+1<l && str[i]==str[i+1] && str[i]=='0')
            i++;
            if(str[i]!='0')
                i--;
        for(j=i+1;j<l;j++)
            str1+=str[j];
            str=str1;
            //cout<<str<<endl;
}


   printf("Case #%d: ",q);
   cout<<str<<endl;
}





    return 0;
     }
