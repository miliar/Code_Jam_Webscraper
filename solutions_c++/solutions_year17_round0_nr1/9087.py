#include <bits/stdc++.h>
using namespace std;
string cad;
int b,ans=0;
static void misa(int  u){
    if(cad.size()-b>=u){
       for(int i=u;i<u+b;++i){
          if(cad[i]=='-')cad[i]='+';
          else cad[i]='-';
       }
       ans++;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("misael.txt","w",stdout);
    int a,c;
    cin>> a ;
    for(int i=0;i<a;++i){
      cin>> cad >> b;
      for(int s=0;s<cad.size();++s){
         if(cad[s]=='-'){
           misa(s);
         }
      }
      cout<<"Case #"<<i+1<<": ";
      int cont=0;
      for(int s=0;s<cad.size();++s){
         if(cad[s]=='+')cont++;
      }
      if(cont==cad.size())cout<<ans<<endl;
      else cout<<"IMPOSSIBLE"<<endl;
      cont=0; ans=0;

    }

}
