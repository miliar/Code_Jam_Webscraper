#include<bits/stdc++.h>
using namespace std;
typedef long long i64;

int main()
{


    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
      int test;
        i64 n;
        scanf("%d",&test);
     vector<int>lst;

    for(int ca=1;ca<=test;ca++)
    {
       scanf("%lld",&n);
       lst.clear();

       printf("Case #%d: ",ca);
       if(n<=9)
       {
           printf("%lld",n);
       }
       else
       {
          while(n>0)
          {
              lst.push_back(n%10LL);
              n/=10LL;
          }
          reverse(lst.begin(),lst.end());
          int len=lst.size();
            while(1)
            {
                int yes=1;
                for(int i=0;i+1<len;i++)
                {
                  if(lst[i]>lst[i+1])
                  {
                      yes=0;
                      lst[i]--;
                      for(int j=i+1;j<len;j++)
                        lst[j]=9;
                  }
                }
                if(yes==1)break;

            }
          for(int i=0;i<len;i++)
          {
              if(i==0 && lst[0]<=0)continue;
              printf("%d",lst[i]);
          }
       }
       puts("");

    }
    return 0;
}
