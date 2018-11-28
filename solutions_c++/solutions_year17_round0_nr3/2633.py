#include <iostream>

using namespace std;

int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        int64_t n,k;
        cin>>n>>k;
        while (k!=1){
            if (n%2==0 && k%2!=0){
                k-=1;
                k/=2;
                n/=2;
                n-=1;
            } else  if (n%2==0 && k%2==0){
             if (k==2){
                 k=1;
                 n/=2;
             } else{

                 k/=2;
                 n/=2;

             }
            } else if (n%2==1 && k%2!=0){
                k-=1;
                k/=2;
                n/=2;
            }else  if (n%2==1 && k%2==0){
                if (k==2){
                    k=1;
                    n/=2;
                } else{
                    k-=2;
                    k/=2;
                    k+=1;
                    n/=2;
                }
            }
        }
        if (n%2==0)
            cout<<"Case #"<<(test+1)<<": "<<(n/2)<<" "<<(n/2-1)<<endl;
        else
            cout<<"Case #"<<(test+1)<<": "<<(n/2)<<" "<<(n/2)<<endl;
    }




}
