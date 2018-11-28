#include<bits/stdc++.h>
std::map<long long,int>mp;
long long cnt[10001000];
long long tr[10001000];
int main(){
    int T,t=0;
    freopen("C-large.in","r",stdin);
    freopen("C-out.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        t++;
        long long x,y;
        scanf("%lld%lld",&x,&y);
        mp.clear();
        int now=0;
        mp[x]=now;
        tr[now]=x;
        cnt[now++]=1;
        y--;
        int ans=0;
        for(int k=0;;k++){
            if(y<cnt[k]) break;
            y-=cnt[k];
            long long p,q,c;
            c=tr[k];c--;
            p=(c+1)/2;q=c-p;
            if(mp[p]==0){
                mp[p]=now++;
                tr[mp[p]]=p;
            }
            if(mp[q]==0){
                mp[q]=now++;
                tr[mp[q]]=q;
            }
            cnt[mp[p]]+=cnt[k];
            cnt[mp[q]]+=cnt[k];
            cnt[k]=0;
        }
        printf("Case #%d: ",t);
        for(int k=0;;k++){
            if(cnt[k]!=0){
                long long p,q,c;
                c=tr[k];c--;
                p=(c+1)/2;q=c-p;
                printf("%lld %lld\n",p,q);
                break;
            }
        }
        for(int k=0;k<now;k++) cnt[k]=0;
    }
}
            
