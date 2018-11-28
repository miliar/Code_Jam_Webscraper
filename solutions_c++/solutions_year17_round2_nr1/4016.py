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
        int n ;
        double d ;
        cin>>d>>n ;
        double time[n+1] ;
        vector<pair<double , double> > v(n) ;
        double k , s ;
        for(int i=0 ; i<n ; i++)
        {
           cin>>v[i].first>>v[i].second ;
        }
        sort(v.begin() , v.end()) ;
        double m=-1 ;
        for(int i=0 ; i<n ; i++){
            time[i]=(d-v[i].first)/v[i].second ;
            m=max(m , time[i]) ;
        }
        double ans=d/m ;

        std::cout << std::fixed;
       //std::cout << std::setprecision(5) << f << '\n';
        cout<< std::setprecision(6)<<"Case #"<<f<<": "<<ans<<endl ;
        //cout<<ans<<endl ;


        f++ ;
    }
}
