#include<bits/stdc++.h>
using namespace std;
 int main()
{
  freopen("B-small-attempt2.in","r",stdin);
freopen("B-small823.out","w",stdout);
    int t,c=0;
    cin>>t;
    while(t--){ c++;
            unsigned long int n;
            cin>>n;

        for(unsigned long int i=n;i>0;i--){

            unsigned long  int nm=i;
            unsigned long  int rem=nm%10;
             while(nm)
             {
               if((nm%10)<=rem){
                   rem=nm%10;
                   nm/=10;
               }
               else break;
             }
             if(nm==0)
             {cout<<"Case #"<<c<<":"<<" "<<i<<endl;break;}
            // n--;

         }//c++;
}
}
