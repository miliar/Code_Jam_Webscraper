#include<bits/stdc++.h>
using namespace std;

int main(){
    int test;
    cin>>test;
    long long int n,k;
    int c=1;
    while (test--){
        cin>>n>>k;
        int I=0;
        int i=1;
        for (i=1; i<70; i++){
            if (pow(2,i)-1>=k){
                break;
            }
        }
        /* Tumhari maa ki chut */
        /* Bhag bhosdike */
        /* Chaapa hai bhenchod */
        /* Pakad ke dikha */
        I=i;
        long long int p=pow(2,I);
       long long int var=(n-p+1);
        long long int r=var%p;
        long long int b=var/p;
        long long int a=0;
        if (p/2<r){
            long long int temp=pow(2,I-1);
            r=2*r-pow(2,I);
            if(2*(k-temp+1)<=r){
               
                a=b+1;
                b=b+1;
                        cout<<"Case #"<<c<<": "<<a<<" "<<b<<endl;

            }
            else{
                a=b+1;
                        cout<<"Case #"<<c<<": "<<a<<" "<<b<<endl;

            }
        }
        else{
            long long int temp=pow(2,I-1);
            if((k-temp+1)<=r){
                a=b+1;
                        cout<<"Case #"<<c<<": "<<a<<" "<<b<<endl;

            }         
            else{
                a=b;
                        cout<<"Case #"<<c<<": "<<a<<" "<<b<<endl;

            }
        }
        c++;
    
    }
    
}