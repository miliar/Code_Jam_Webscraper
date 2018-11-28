#include <bits/stdc++.h>
using namespace std;


bool isTidy(long long x){
    long long next, actual;
    while(x!=0){
        actual = x%10;
        next = (x/10)%10;
        if(actual<next) return false;
        x /= 10;
    }
    return true;
}

int main(){
    long long t, n;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        while(!isTidy(n)) --n;
        cout<<"Case #"<<i<<": "<<n<<"\n";
    }
    return 0;
}
