#include<bits/stdc++.h>
#define F first
#define S second

using namespace std;

int main(){
freopen("C-small-2-attempt1.in","r",stdin);
freopen("outt_codejamC.txt","w",stdout);
int t;
cin>>t;
for(int tc=1;tc<=t;tc++){
    int n,k;
    cin>>n>>k;
    priority_queue< pair<int, pair<int,int> > ,vector< pair<int, pair<int,int> > >, less< pair<int, pair<int,int> > > > pq;
    pq.push(make_pair(n-1,make_pair(1,n)));
    for(int i=1;i<k;i++){
        if(pq.empty()) break;
        int l=pq.top().S.F,r=pq.top().S.S;
        int mid=(r+l)/2;
        pq.pop();
        int lval=mid-1-l,rval=r-mid-1;
        if(lval>0) pq.push(make_pair(lval,make_pair(l,mid-1)));
        if(rval>0) pq.push(make_pair(rval,make_pair(mid+1,r)));
    }
    int ls=0,rs=0;
    if(pq.size()) {
        int lt=pq.top().S.F,rt=pq.top().S.S;
        int mid=(rt+lt)/2;
        int x=mid-lt;
        int y=rt-mid;
        ls=max(x,y);
        rs=min(x,y);
    }
    cout<<"Case #"<<tc<<": ";
    cout<<ls<<" "<<rs<<endl;
}


return 0;
}

