#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define pp pair<int,int>
using namespace std;
int n,k,y,z;
int a[1001];
set<pair<int,pp> > S;


int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output-C-small.txt","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++){

        cin>>n>>k;
        S.clear();
        S.insert(mp(n,mp(0,n+1)));

        for(int j=1;j<=k;j++){
            int len= -(*S.begin()).F;
            int l=(*S.begin()).S.F;
            int r=(*S.begin()).S.S;
            S.erase(S.begin());
            int x=(l+r)/2;
            //cout<<l<<' '<<r<<endl;
            int ll=x-l-1,rr=r-x-1;

            //cout<<x<<endl;

            z=min(ll,rr);
            y=max(ll,rr);
            if(l+1<=x-1)
                S.insert(mp(-(x-l-1),mp(l,x)));
            if(x+1<=r-1)
                S.insert(mp(-(r-x-1),mp(x,r)));
        }

        cout<<"Case #"<<t<<": "<<y<<' '<<z<<endl;
    }

    return 0;
}
