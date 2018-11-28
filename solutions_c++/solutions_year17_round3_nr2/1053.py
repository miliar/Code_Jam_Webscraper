#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>

using namespace std;
constexpr double pi = 3.141592653589793;

int getAns2(vector<pair<int,int>>& T){
    sort(begin(T), end(T));
    if(T[1].second-T[0].first<=720 || T[1].first-T[0].second>=720 || (T[0].first==0&&T[1].second==1440)){
        return 2;
    }else{
        return 4;
    }
}

int main() {
    int T;
    cin >> T;

//    cout << fixed << setprecision(10);
    for (int I = 0; I < T; ++I) {
        int N,K;
        cin>>N>>K;

        vector<pair<int,int>> Tc(N);
        vector<pair<int,int>> Tj(K);
        for(auto& val:Tc){
            cin>>val.first>>val.second;
        }
        for(auto& val:Tj){
            cin>>val.first>>val.second;
        }

        int ans=0;
        if(N+K == 1){
            ans = 2;
        }else if(N+K==2) {
            if(N==1){
                ans = 2;
            }else if(N==2){
                ans=getAns2(Tc);
            }else if(K==2){
                ans=getAns2(Tj);
            }
        }


        cout << "Case #" << I + 1 << ": "<<ans<<'\n';
    }
    return 0;
}