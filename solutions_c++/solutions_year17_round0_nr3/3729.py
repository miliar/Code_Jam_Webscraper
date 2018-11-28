#include <cstdio>
#include <utility>

typedef std::pair<long long,long long> ii;

ii mymerge(long long n,long long a){
    long long left,right;
    while(a>0){
        if(n%2==0){
            left = n/2-1;
            right = n/2;
        }
        else{
            left = n/2;
            right = n/2;
        }
        if(a%2==0){
            n=right;
            a/=2;
        }
        else{
            n=left;
            a/=2;
        }
    }
    return ii(right,left);
}

int main(){
    int t;
    long long k,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        long long a,b;
        ii answer;
        scanf("%lld %lld",&a,&b);
        answer = mymerge(a,b);
        printf("Case #%d: %lld %lld\n",i+1,answer.first,answer.second);
    }
}