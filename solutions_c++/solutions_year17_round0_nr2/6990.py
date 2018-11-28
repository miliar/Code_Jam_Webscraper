#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;
#define lol long long
bool check(lol int n)
{
    vector<lol int>vec;
    lol int i;
    while(n!=0)
    {
        lol int a=n%10;
        vec.push_back(a);
        n/=10;
    }
    reverse(vec.begin(),vec.end());
    int flag=0;
    for(i=1;i<vec.size();i++)
    {
        if(vec[i]<vec[i-1])
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    {
        vec.clear();
        return false;
    }
    else
    {
        vec.clear();
        return true;
    }
}
lol int sum(lol int n)
{
    lol int f;
    vector<lol int>vec;
     while(n!=0)
    {
        lol int a=n%10;
        vec.push_back(a);
        n/=10;
    }
    f=vec.size();
    vec.clear();
    return f;
}
int main()
{
   lol int i,j,k,n,t,tcase=0,val,h,x;
   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   cin>>t;
   while(t--)
   {
       tcase++;
       scanf("%lld",&n);
       lol int f=10;
       k=sum(n);
       if(true==check(n))
       {
           printf("Case #%lld: %lld\n",tcase,n);
       }
       else
       {
           int flag=0;
           for(i=1;i<=k-1;i++)
           {
               h=n/f;
               val=(h*f)-1;
               if(true==check(val))
               {
                   flag=1;
                   break;
               }
               f*=10;
           }
           if(flag==1)printf("Case #%lld: %lld\n",tcase,val);
       }
   }
    return 0;

}
