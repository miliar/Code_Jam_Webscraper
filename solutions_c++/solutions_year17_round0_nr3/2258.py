#include<cstdio>

long long sol(long long N, long long x){
    if(x==1) return N;

    long long xx=x;
    long long one=1;
    int cnt=0;
    while(xx>3){
        xx/=2; cnt++;
    }
    if(xx==2) return sol(N,x-(one<<cnt))/2;
    else return (sol(N,x-(one<<(cnt+1)))-1)/2;
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int T;
    long long K,N;
    long long ans;

    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        printf("Case #%d: ",t);
        scanf("%lld %lld",&N,&K);
        ans=sol(N,K);
        printf("%lld %lld\n",ans/2,(ans-1)/2);
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
