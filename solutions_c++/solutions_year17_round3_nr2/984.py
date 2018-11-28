#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

void solve(int t) {

    int ct, j;
    cin>>ct>>j;

    cout<<"Case #"<<t<<": ";

    

    vector<pair<int, int > >c; 
    for(int i=0; i<ct+j; i++) {
        int u, v;
        cin>>u>>v;
        c.push_back(make_pair(u, v));
        //cout<<u<<" "<<v<<endl;
    }

    if(ct>0 && j>0) {
        cout<<2<<endl;return;
    }
    sort(c.begin(), c.end());

    //cout<<c[1].second - c[0].first<<" "<< 1440-c[1].first + c[0].second<<endl;
    if(c.size()<2 || c[1].second - c[0].first <= 720 || (1440-c[1].first + c[0].second) <= 720) {
        cout<<2<<endl;
    } else {
        cout<<4<<endl;
    }

}


int main() {

    freopen("B-small-attempt1 (2).in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}