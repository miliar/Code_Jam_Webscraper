#include<bits/stdc++.h>
using namespace std;
inline void read(int &x){
    register char c=getchar();
    x=0;
    while(c<'0'||c>'9') c=getchar();
    for(;c>='0'&&c<='9';c=getchar())
        x=(x<<1)+(x<<3)+(c-'0');
}
#define R first
#define H second
const double pi=3.14159265359;
pair<int,int> a[1005];
priority_queue<long long> q;
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cout<<fixed<<setprecision(9);
    int tt,t,i,k,n;
    long long x,y,z;
    read(t);
    for(tt=1;tt<=t;++tt){
        read(n);read(k);--k;
        for(i=0;i<n;++i) read(a[i].R),read(a[i].H);
        sort(a,a+n);
        while(!q.empty()) q.pop();
        y=z=0;
        if(k){
            for(i=0;i<n;++i){
                x=2LL*a[i].R*a[i].H;
                if(q.size()==k) z=max(z,x+y+1LL*a[i].R*a[i].R);
                if(q.size()==k&&q.top()>-x) y+=q.top(),q.pop();
                if(q.size()<k) y+=x,q.push(-x);
            }
        }
        else{
            for(i=0;i<n;++i) z=max(z,2LL*a[i].R*a[i].H+1LL*a[i].R*a[i].R);
        }
        cout<<"Case #"<<tt<<": "<<z*pi<<endl;
    }
}
