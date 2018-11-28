#include<bits/stdc++.h>
using namespace std;
vector<pair<int,int> > v;
void op(int n){
    if(n == 0) return;
    v.push_back(make_pair(max(n/2,n-1-n/2),min(n/2,n-1-n/2)));
    op(n/2);
    op(n-1-n/2);
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("C-small-2-attempt0.in.txt","r",stdin);
    freopen("outsmall.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        int k, n;
        cin >> n >> k;
        op(n);
        sort(v.begin(),v.end(),greater<pair<int,int> >());
        cout << max(v[k-1].first,0) << " " << max(0,v[k-1].second) << "\n";
        v.clear();
    }
    return 0;
}
