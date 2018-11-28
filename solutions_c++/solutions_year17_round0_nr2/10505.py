#include <iostream>

using namespace std;

long long result = 0;

long long pow(long long x, int y){
    long long r =1;
    for(y = y; y>0; y--){
        r*=x;
    }
    return r;
}

int numDigits(long long number)
{
    int digits = 0;
    if (number < 0) digits = 1;
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}

void smth(long long k){
    int n[numDigits(k)];
    long long x = 0;
    long long y = k;
    long long z;
    int last;
    for(int i = numDigits(k);i>0;i--){
        z = pow(10,i-1);
        x = k%z;
        n[i]=(y-x)/z;
        y-=n[i]*pow(10,i-1);
        if(i!= numDigits(k)){
            if(n[i+1] <= n[i]){
                if(i == 1){
                    result = k;
                }
            }else{
                break;
            }
        }
    }
    if(numDigits(k)==1){
        result = k;
    }
}

void lecimy(long long k,int l){
    for(long long i = k; i>0;i--){
        smth(i);
        if(result!=0)
            break;
    }
    cout<<"Case #"<<l+1<<": "<<result;
    result = 0;
}

int main()
{
    int t;
    cin>>t;
    long long N[t];
    for(int i =0;i<t;i++){
        cin>>N[i];
        lecimy(N[i],i);
        if(i!=t-1)
            cout<<endl;
    }
    return 0;
}
