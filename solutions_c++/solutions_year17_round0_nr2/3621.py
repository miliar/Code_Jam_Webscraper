#include<bits/stdc++.h>
using namespace std ;
#define LL long long

int main()
{
    int t ;
    cin>>t ;
    int f=1 ;
    while(f<=t)
    {
        LL n ;
        cin>>n  ;

        LL temp1=n , ans=0 ;
        int r=temp1%10 ;
        temp1=temp1/10 ;
        int l=temp1%10 ;
        temp1=temp1/10 ;
        LL mult=100 ;

        if(l<=r){
            ans=l*10+r ;
        }
        else{
            l-- ;
            ans=l*10+9 ;
        }
        int x;
        LL tempmul ;
        while(temp1>0)
        {
            x=temp1%10 ;
            temp1=temp1/10 ;
            if(x<=l)
            {
                ans=ans+(mult*x) ;
                mult=mult*10 ;
                l=x ;
            }
            else
            {
                x-- ;
                tempmul=mult-1 ;
                ans=tempmul+(mult*x) ;
                mult=mult*10 ;
                l=x ;
            }
        }
        cout<<"Case #"<<f<<": "<<ans<<endl ;
        f++ ;
    }
    return 0 ;
}
