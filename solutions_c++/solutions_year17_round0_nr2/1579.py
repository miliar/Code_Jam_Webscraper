#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
ll p[20]={1};
int c[20], len;
bool tidy(ll n){
    int b=10;
    while(n){
        if(n%10>b) return false;
        b=n%10;
        n/=10;
    }
    return true;
}
void modify(int pos){
    if(pos>=len) return;
    if(c[pos]<=c[pos+1]) goto con;
    --c[pos];
    c[pos+1]=10;
    con:
    modify(pos+1);
}
int main(){
    freopen("B-large.in","rt",stdin);
    freopen("B-large-out.out","wt",stdout);
    int T;
    ll N, ans;
    cin>>T;
    for(int f=1;f<=T;f++){
        cin>>N;
        len=0;
        if(tidy(N)){
            printf("Case #%d: %lld\n",f,N);
            continue;
        }
        while(N){
            c[len++]=N%10;
            N/=10;
        }
        reverse(c,c+len);
        for(int j=len-1;j>=0;j--) modify(j);
        for(int j=0;j<len;j++) if(c[j]==10) --c[j];
        cout<<"Case #"<<f<<": ";
        int idx=0; for(;!c[idx];++idx);
        for(int i=idx;i<len;i++) cout<<c[i];
        cout<<endl;
    }
}
