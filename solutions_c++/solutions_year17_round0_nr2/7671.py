#include<bits/stdc++.h>
#define int long long
using namespace std;


int f(vector<int> x)
{
   //try forming with i-1 places same,ith place -1 rest all 9s
   int prev =0,f=0;
   int ans=0,mn=1;
   for(int i=0;i<x.size();++i)
   {
       if(x[i]<prev){f=1;}
       prev=x[i];
       ans*=10;
       ans+=x[i];
       mn*=10;
   }
   mn/=10;
   if(f==0)
   {
       return ans;
   }

   //checked for same no

   --mn;
   ans=0;
   int fans=mn;
   vector<int> dd;

   for(int pos=x.size();pos>=0;--pos)
   {
       dd.clear();f=0;prev=0;ans=0;
       for(int i=0;i<x.size();++i)
       {
        if(i<pos)//same as ith place
        {
          dd.push_back(x[i]);
        }
        if(i==pos)
            dd.push_back(x[i]-1);
        if(i>pos)dd.push_back(9);
       }



   for(int i=0;i<dd.size();++i)
   {
       if(dd[i]<prev){f=1;}
       prev=dd[i];
       ans*=10;
       ans+=dd[i];
   }
   if(f==0)
   {
       fans=max(fans,ans);
   }


   }

   return fans;
}

main()
{
    freopen("B-large123.in","r",stdin);
   freopen("bfans.txt","w",stdout);
int t;
string s;
int k,ans;
vector<int> no;
//ans 1 = no of digits -1 all 9
//ans 2 = first digit -1 rest all 9
//ans 3=first digit same second digit-1


cin>>t;
for(int tc=1;tc<=t;++tc)
{
    no.clear();
    ans=0;
    cin>>k;
    while(k)
    {
        no.push_back(k%10);
        k/=10;
    }
    reverse(no.begin(),no.end());
    //cout<<no.size();
    cout<<"Case #"<<tc<<": ";
    cout<<f(no)<<endl;
    //cout<<ans<<endl;
}
return 0;
}
