#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        cout<<"Case #"<<t<<": ";
        int64_t i=0;
        int64_t N,K;
        cin>>N>>K;
        while((1LL<<(i+1))<=K) i++;
        int64_t short_len = (N-(1LL<<i)+1)/(1LL<<i);
        int64_t long_len = short_len+1;
        int64_t long_cnt=(N-(1LL<<i)+1)-short_len*(1LL<<i);
        int64_t short_cnt=(1LL<<i)-long_cnt;
        K-=(1LL<<i);
        int64_t len;
        if(long_cnt>K){
            len=long_len-1;
        }else{
            len=short_len-1;
        }
        int64_t y,z;
        if(len%2==0){
            y=z=len/2;
        }else{
            z=len/2;
            y=z+1;
        }
        cout<<y<<' '<<z<<endl;
    }
}