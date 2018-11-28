#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>


using namespace std;

long long findn(long long n,long long x,unordered_map<long long, long long> &a){
    if (n<=x){
        a[n]=0;
        return a[n];
    }
    if (a.find(n)!=a.end()){
        return a[n];
    }
    else {
        a[n]=findn((n-1)/2, x, a)+findn(n/2,x,a)+1;
        return a[n];
    }
}

long long numlargerthan(long long n, long long x){
    unordered_map<long long, long long> a;
    a.clear();
    return findn(n,x,a);
}

int main() {
    freopen("C-large.in.txt", "r", stdin);
    freopen("C-large.out.txt", "w", stdout);
    long t,tt;
    scanf("%ld",&t);
    for (tt=1;tt<=t;tt++){
        long long n,k;
        scanf("%lld%lld",&n,&k);
        long long l=1,r=n,mid;
        while (l<r){
            mid=(l+r)/2;
            if (numlargerthan(n, mid)<k)
                r=mid;
            else
                l=mid+1;
        }
        printf("Case #%ld: %lld %lld\n",tt,l/2,(l-1)/2);
    }
    return 0;
}
