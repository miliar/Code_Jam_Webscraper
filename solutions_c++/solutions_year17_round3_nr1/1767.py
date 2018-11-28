#include<bits/stdc++.h>
using namespace std ;
#define LL long long

const double pi=3.14159265359 ;
bool mycomp(pair<double , double> x , pair<double , double > y){
    if(x.first>y.first){
        return true ;
    }
    else if(x.first==y.first){
        if(x.second>=y.second){
            return true ;
        }
        return false ;
    }
    return false ;
}

int main()
{

 int t ;
 cin>>t ;
 int f=1 ;
 while(f<=t){

double n , k ;
cin>>n>>k ;

    vector<pair<double , double> > rh(n) ;
    ///           area     radius
    vector<pair<double , double > > csa(n) ;

    for(int i=0 ; i<n ; i++){
        cin>>rh[i].first>>rh[i].second ;
    //    csa[i]=2*rh[i].first*rh[i].second ;
    }

    sort(rh.begin() , rh.end()) ;

    double currR , currTA ,maxA=-1 , ctr=0 ;
    vector<pair<double , double> > temp(n) ;
    for(int i=k-1 ; i<n ; i++){
        currTA=2*rh[i].first*rh[i].second + rh[i].first*rh[i].first ;
        currR=rh[i].first ;
        ctr=1 ;
         vector<pair<double , double> > temp(i) ;
        for(int j=0 ; j<i ; j++){
            temp[j].first=2*rh[j].first*rh[j].second ;
            temp[j].second=rh[j].first ;
        }
        sort(temp.begin() , temp.end()) ;
        for(int j=i-1 ; j>=0 ; j--){
            if(ctr==k){
                break ;
            }
            if(temp[j].second<=currR){
                currTA+=temp[j].first ;
                ctr++ ;
            }
        }

        if(ctr==k){
            maxA=max(maxA , currTA) ;
        }
    }




    /*
    sort(csa.begin() , csa.end()) ;


    double ctr=0 ;
    double ta=0  ,  currR ;
    for(int i=0 ; i<n ; i++)
    {
        ta=2*rh[i].first*rh[i].second ;
        currR=rh[i].first ;
        ctr=0 ;
        for(int j=n-1 ; j>=0 ; j--)
        {
            if(csa[j].second<=curr)
        }

    }

    //sort(rh.begin() , rh.end() , mycomp) ;
    */
    std::cout << std::fixed;

    cout<<"Case #"<<f<<": "<<std::setprecision(9)<<maxA*pi <<endl ;
    f++ ;
 }
 return 0 ;
}
