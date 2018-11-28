#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#define ll long long
using namespace std;
int main(){
    freopen("B-small-attempt1.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,tc=1;
    cin>>t;
    while(t--){
        int n, arr[6];
        string s;
        cin>>n;
        for(int i=0; i<6; i++) cin>>arr[i];
        int r=arr[0], y=arr[2], b=arr[4];
        if(r>n/2||y>n/2||b>n/2){
            cout<<"Case #"<<tc++<<": IMPOSSIBLE"<<endl;
            continue;
        }
        for(int i=0; i<n; i++) s+="?";
        vector<pair<int,char> > vec;
        vec.push_back({r,'R'});
        vec.push_back({y,'Y'});
        vec.push_back({b,'B'});
        sort(vec.rbegin(), vec.rend());
        for(int i=0; i<n && vec[0].first; i+=2){
            s[i]=vec[0].second;
            vec[0].first--;
        }
        for(int i=n-1; i>=1 && vec[1].first; i-=2){
            if(s[i]!='?'){
                i--;
            }
            s[i]=vec[1].second;
            vec[1].first--;
        }
        for(int i=0; i<n; i++){
            if(s[i]=='?') s[i]=vec[2].second;
        }
        map<char,int> mop;
        for(int i=0; i<n; i++) {
            if(s[i]==s[(i+1)%n]) cout<<"====================================================";
            mop[s[i]]++;
        }
        if(mop['R']>r) cout<<"R====================================================";
        if(mop['B']>b) cout<<"B====================================================";
        if(mop['Y']>y) cout<<"Y====================================================";
        cout<<"Case #"<<tc++<<": "<<s<<endl;
    }
}
