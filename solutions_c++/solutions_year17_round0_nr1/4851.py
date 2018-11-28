#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL

int main()
{
  gearchange();
   int t;
   cin>>t;
   int y=0;
   while(t--){
       y++;
       string s;
       cin>>s;
       int k;
       cin>>k;
       int ans=0;
       for (int i = 0; i<s.length()-k+1; ++i)
       {
         if(s[i]=='-'){

             ans++;
             for (int j = i; j<k+i; j++)
             {
               if(s[j]=='-'){
                 s[j]='+';
               }
               else{
                 s[j]='-';
               }
             }
         }
       }
       bool yes= true;
       for (int i = 0; i <s.length(); ++i)
       {
         if(s[i]=='-'){ yes=false; break;}
       }
       cout<<"Case #"<<y<<": ";
       if(!yes){
          cout<<"IMPOSSIBLE"<<endl;
       }
       else{
          cout<<ans<<endl;
       }
   }
  return 0;
}