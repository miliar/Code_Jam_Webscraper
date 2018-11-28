#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{   freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout); 
    ll t,z=1;
       cin>>t;
     while(t--)
     {
      ll ans=0,flag=0,i=1,y,k,x,n;
      cin>>n;
   
    while(flag!=1)
      {
          k=n;
          ans=45;
        while(k!=0)
          {
         y=k%10;
         k=k/10;
            if(y>ans)
             {
              flag=0;
               break;
             }
             else
            flag=1;
            ans=y; 
        }
        
        if(flag==1)
        break;
        
        x=pow(10,i);
        n=n-((n%x)+1);
     
        i++;
        
     }
     cout<<"Case #"<<z<<": "<<n<<"\n";
     z++;
    }
    return 0;
}
