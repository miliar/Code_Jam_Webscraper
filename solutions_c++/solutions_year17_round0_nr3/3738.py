#include<bits/stdc++.h>
using namespace std ;
#define LL long long

unordered_map<LL,LL> h ;
set<LL> s ;

void game(LL k , LL  ctr)
{

    set<LL>::reverse_iterator rit ;

    while(1)
    {
            if(!s.empty())
            rit=s.rbegin();
            else{
                cout<<"0 0"<<endl ;
                return ;
            }
            LL temp=(*rit) ;

            if(h[temp]==1){
                s.erase(temp) ;
                h.erase(temp) ;
            }
            else{
                h[temp]-- ;
            }
            LL l , r ;
            if(temp%2==0){
                l=temp/2 ;
                r=l-1 ;
            }
            else{
                l=temp/2 ;
                r=l ;
            }
            if(k==ctr){
                cout<<max(l,r)<<' '<<min(l,r)<<endl ;
                return ;
            }

            if(l!=0){
                s.insert(l) ;
                if(h.find(l)!=h.end()){
                    h[l]++ ;
                }
                else{
                    h[l]=1 ;
                }
            }
            if(r!=0){
                s.insert(r) ;
                if(h.find(r)!=h.end()){
                    h[r]++ ;
                }
                else{
                    h[r]=1 ;
                }
            }
            ctr++ ;
        }
}


int main()
{
    int t ;
    cin>>t ;
    int f=1 ;
    while(f<=t)
    {
       LL n,k ;
       cin>>n>>k  ;
       s.clear() ;
       h.clear() ;
       s.insert(n) ;
       h.insert(make_pair(n,1)) ;

       cout<<"Case #"<<f<<": " ;
       game(k , 1) ;
       f++ ;
    }
    return 0 ;
}
