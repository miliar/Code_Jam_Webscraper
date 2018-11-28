#include<bits/stdc++.h>
using namespace std;

string a;
int n, i, j, t, k, cnt, flg, tc=0;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

  scanf("%d", &t);
  while(t--)
  {
     cin>>a>>k; cnt=0; flg=0;
     string b, c;
     b=a; c=a;

     for(i=0; i<b.size()-k+1; i++)
     {
            if(b[i]=='-')
            {
               for(j=i; j<i+k; j++)
               {
                     if(b[j]=='-') b[j] = '+';
                     else b[j]= '-';

               }
               ++cnt;
            }
     }

     for(int i=0; i<b.size(); i++)
     {
         if(b[i]=='-') flg++;
     }
  int cnt1=0, flg1=0;
  reverse(c.begin(),c.end());


   for(i=0; i<c.size()-k+1; i++)
   {
            if(c[i]=='-')
            {
               for(j=i; j<i+k; j++)
               {
                     if(c[j]=='-') c[j] = '+';
                     else c[j]= '-';
               }
               ++cnt1;
            }
   }

    for(int i=0; i<c.size(); i++) { if(c[i]=='-') flg1++; }

     printf("Case #%d: ",++tc);
    if(flg!=0 && flg!=0) cout<<"IMPOSSIBLE"<<endl;
    else
    {
        int ans;
        if(flg1!=0) ans = cnt;
        else if(flg!=0) ans = cnt1;
        else ans = min(cnt,cnt1);

        cout<<ans<<endl;
    }
  }

return 0;
}
