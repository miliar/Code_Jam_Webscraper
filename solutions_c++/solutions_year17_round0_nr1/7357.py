#include<bits/stdc++.h>
using namespace std;
int data[10005];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test_case;
    scanf("%d",&test_case);
    for(int ca=1;ca<=test_case;ca++)
    {
      string inp;
      cin>>inp;
      int k;
      scanf("%d",&k);
      int len=inp.size();
      for(int i=0;i<len;i++)
      {
          if(inp[i]=='+')
            data[i]=1;
          else data[i]=0;

      }
      int cnt=0;
      int pos=-1;
      for(int i=0;i<len;i++)
      {

         if(data[i]==0 && (i+k-1)<len)
         {
              cnt++;
            for(int j=i;j<=(i+k-1);j++)
                data[j]^=1;
         }
      }
      for(int i=0;i<len;i++)
      {
         if(data[i]==0)cnt=-1;
          //cout<<data[i];
      }
      if(cnt==-1)printf("Case #%d: IMPOSSIBLE\n",ca);
      else printf("Case #%d: %d\n",ca,cnt);
    }
    return 0;
}
