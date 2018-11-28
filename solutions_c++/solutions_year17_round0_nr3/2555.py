#include<bits/stdc++.h>
using namespace std;
int t;
void solve(long long n,long long k){
    long long first,second;
    if(n%2){
        first = n/2;
        second = n/2;
    }
    else{
        first = n/2;
        second = n/2 - 1;
    }
    if(k == 1)
        printf("Case #%d: %lld %lld\n",t+1,first,second);
    else{
        if(k%2 == 0)
            solve(first,k/2);
        else
            solve(second,k/2);
    }
}
int main(){
    int test;
    cin >> test;
    for(t=0;t<test;t++){
        long long n,k;
        cin >> n >> k;
        solve(n,k);
    }
    return 0;
}

