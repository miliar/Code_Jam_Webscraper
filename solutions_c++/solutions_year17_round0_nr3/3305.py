#define lli unsigned long long int
#include <bits/stdc++.h>

using namespace std;

int main() {
    lli t;
    cin>>t;
    lli testcase=1;
  //  int c=0; 
    while(t--){
        lli n,k;
        cin>>n>>k;

        lli min,max,newmin=1,newmax=1,ansmin=0,ansmax=0;
        lli tempk=1;
        lli p=1;

        max=n/2; 
        if(n%2) {
            min=max;
        }
        else {
            min=max-1;
        }
        if(k==1){
            cout<<"Case #"<<testcase++<<": "<<max<<" "<<min<<endl;
            continue;
        }
        while(max>0){

            lli increment=pow(2,p);
            lli newtempk=tempk+increment;

            if(k>tempk && k<=newtempk){
                if(k<=tempk+newmax) {
                    ansmax=max/2;

                    if(max%2) {
                        ansmin=ansmax;                     
                    }
                     else{
                         ansmin=ansmax-1;
                     }
                }
                else{
                        ansmax=min/2;
                    if(min%2) {
                        ansmin=ansmax;                     
                    }
                     else{
                         ansmin=ansmax-1;
                     }
                }
                break;
            } 
            
            if(max==min){
                newmin*=2;
                newmax*=2;
            }
            else{
                if(min%2==1) {
                    newmin=newmin*2 +newmax;
                }
                else{
                    newmax=newmax*2+newmin;
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
            tempk=newtempk;
            p++;
    
        }
        
        cout<<"Case #"<<testcase++<<": "<<ansmax<<" "<<ansmin<<endl;
       }
    return 0;
}