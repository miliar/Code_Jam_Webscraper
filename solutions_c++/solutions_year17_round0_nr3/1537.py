#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin>>t;
    int c=0;
  //  int c=0; 
    while(t--){
        c++;
   
        unsigned long long int n,k;
        //cin>>n;
        cin>>n>>k;
      // cout<<n<<"   "<<k<<"   \n";
         long long int min,max,nmin=1,nmax=1,ansmin=0,ansmax=0;
        unsigned long long int tk=1;
        unsigned long long int p=1;
        if(n%2==1) {
            min=n/2;
            max=n/2;
            
        }
        else {
            max=n/2;
            min=max-1;
        }
        if(k==1){
            cout<<"Case #"<<c<<": "<<max<<" "<<min<<endl;
           // cout<<endl;
            continue;
        }
        while(max>0){

            unsigned long long int inc=pow(2,p);
            unsigned long long int ntk=tk+inc;
     //  cout<<"min="<<min<<" max="<<max<<" nmin="<<nmin<<" nmax="<<nmax<<" tk="<<tk<<" ntk="<<ntk<<"------------------>"<<endl;

             if(k>tk && k<=ntk){
             if(k<=tk+nmax) {
                if(max%2==0) {
                    ansmax=max/2;
                    ansmin=ansmax-1;
                     
                }
                 else{
                     ansmax=max/2;
                     ansmin=max/2;
                 }
             }
                 else{
                    if(min%2==0) {
                    ansmax=min/2;
                    ansmin=ansmax-1;
                     
                }
                 else{
                     ansmax=min/2;
                     ansmin=min/2;
                 }
                 }
            break;
            } 
            
            if(max==min){
                nmin=nmin*2;
                nmax=nmax*2;
            }
            else{
                 if(min%2==1) {
                nmin=nmin*2 +nmax;
                         
                         }
            else{
                nmax=nmax*2+nmin;
                
                }
            }
            if(max==min){
                if(min%2==0) {
                    max=min/2;
                    min=max-1;
                }
                else{
                    min=max/2;
                    max=max/2;
                }
            }
            else{
            if(min%2==1) {
                 min=min/2;
                 max=min+1;
                         
                         }
            else{
                 min=min/2-1;
                 max=min+1;
            }
        }
       
            //   cout<<"min="<<min<<" max="<<max<<" nmin="<<nmin<<" nmax="<<nmax<<" tk="<<tk<<" ntk="<<ntk<<endl;
           
         
            tk=ntk;
            p++;
        
        
        }
        
        cout<<"Case #"<<c<<": "<<ansmax<<" "<<ansmin<<endl;
      //  cout<<endl;
       }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
