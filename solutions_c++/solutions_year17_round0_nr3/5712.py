#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef pair<lint,lint> pii;
pii p;
lint n,k;

lint pw2(lint x) {
if(x==1) return 0;
return 1+pw2(x/2);
}

void place(lint cnt,lint lvl,lint l,lint r) {
if(cnt>k) return;
if(cnt==k) { lint m=(l+r)/2;  p.first=max(m-l-1,r-m-1);p.second =min(m-l-1,r-m-1);

return;}
lint m = (l+r)/2;
lint pwl = pow(2,lvl);
place(cnt+2*pwl,lvl+1,l,m);
place(cnt+pwl,lvl+1,m,r);

}

int main() {
lint t,test=0;cin>>t;
    while(t--)
    {
    cin>>n>>k;

    place(1,0,-1,n);
    cout<<"Case #"<<(++test)<<": "<<p.first<<" "<<p.second<<endl;
    }

return 0;
}
