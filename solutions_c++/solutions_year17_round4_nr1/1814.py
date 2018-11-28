#include<bits/stdc++.h>
using namespace std;
inline void read(int &x){
    register char c=getchar();
    x=0;
    while(c<'0'||c>'9') c=getchar();
    for(;c>='0'&&c<='9';c=getchar())
        x=(x<<1)+(x<<3)+(c-'0');
}
int q[4];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,tt,n,p,i,z;
    read(t);
    for(tt=1;tt<=t;++tt){
        read(n);read(p);
        for(i=0;i<p;++i) q[i]=0;
        while(n--) read(i),++q[i%p];
        if(p==2) z=q[0]+(q[1]+1)/2;
        else if(p==3){
            if(q[1]>q[2]) swap(q[1],q[2]); q[2]-=q[1];
            z=q[0]+q[1]+(q[2]+2)/3;
        }
        else if(p==4){
            if(q[1]>q[3]) swap(q[1],q[3]); q[3]-=q[1];
            z=q[0]+q[1]+(q[2]+1)/2;
            if(q[2]%2==1&&q[3]>=2){
                q[3]-=2;
                ++z;
            }
            z+=(q[3]+3)/4;
        }
        printf("Case #%d: %d\n",tt,z);
    }
}
