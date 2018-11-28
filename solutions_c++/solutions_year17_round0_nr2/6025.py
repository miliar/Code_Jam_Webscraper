#include<bits/stdc++.h>
using namespace std;

int main()
{

   freopen("B-large.in","r",stdin);
   freopen("bl_out.in","w",stdout);
   int tst,ind,fl=0;
   string num,ans;
   cin >> tst;
   for(int tstno=1;tstno<=tst;tstno++)
   {
      cin >> num;
      fl=0,ind=0;
      for(int i=0;i<num.length()-1;i++)
      {
         if(fl)
         {
            num[i]='9';
         }
         else if(num[i]>num[i+1])
         {
            num[i]=num[i]-1;
            fl=1;
            ind=i;
         }
      }
      if(fl)
      {
         num[num.length()-1]='9';
      }
      for(int i=ind;i>=1;i--)
      {
        if(num[i-1]>num[i])
        {
           num[i]='9';
           num[i-1]=num[i-1]-1;
        }
      }
      if(num[0]=='0')
      {
         cout<<"Case #"<<tstno<<": "<<num.substr(1,num.length())<<"\n";
      }
      else
         cout<<"Case #"<<tstno<<": "<<num<<"\n";
   }
}
