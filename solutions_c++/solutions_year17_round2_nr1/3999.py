#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    long long int t,n,T=1;
    long double d;
    cin>>t;
    while(T<=t){
        cin>>d>>n;
        long long int k[n],s[n];
        for(long long int i=0;i<n;i++){
            cin>>k[i]>>s[i];
        }
        long double time=(d-k[0])/s[0];
        for(long long int i=0;i<n;i++){
            long double temp=(d-k[i])/s[i];
            if(time<temp)
                    time=temp;
        }
        std::cout << std::fixed;
        std::cout << std::setprecision(6);
        cout<<"Case #"<<T<<": "<<d/time<<endl;
        T++;
    }
    return 0;
}
