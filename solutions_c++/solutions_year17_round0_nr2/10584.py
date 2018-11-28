#include <iostream>
#include<cstring>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int c=0;
    while(t--){
        c++;
        unsigned long long num;
        cin>>num;
        for(unsigned long long i=num;i>0;i--){
            //cout<<"sadad\n";
            if(i%10==0){
                continue;
            }
            unsigned long long k=i;
            int f=0;
            while(k/10!=0){
                //cout<<"hello\n";
                unsigned long long y=k%10;
                unsigned long long kk=k/10;
                //cout<<y<<endl;
                kk=kk%10;
                if(kk>y){
                    f=1;
                    break;
                }
                k=k/10;
            }
            if(!f){
                cout<<"Case #"<<c<<": "<<i<<endl;
                break;
            }
        }
    }
   return 0;
}

