 #include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <iomanip>
using namespace std;

template<typename T>
bool check(const vector<int>&d , const vector<int> &s, int D, T time){
    for(size_t i = 0, cntr = s.size(); i < cntr; ++i){
        auto v1 = static_cast<long long>(time) * static_cast<long long>(s[i]);
        auto v2 = D - d[i];
        if (v1 < v2) return false;
    }
    return true;
}
void solve(){
    int D, N;
    cin >> D >> N;
    vector<int> dist(N);
    vector<int> speed(N);
    vector<double> values(N);
    long long mxDist = 0, mxSpeed = 0;
    for (int i = 0; i < N; ++i){
        cin >> dist[i];
        cin >> speed[i];
        dist[i] = D - dist[i];
        if (dist[i] < 0) continue;
        if (dist[i] * mxSpeed >= mxDist * speed[i]){
            mxDist = dist[i];
            mxSpeed = speed[i];
        }
    }
    
    cout <<setprecision(7)<< D * mxSpeed / static_cast<float>(mxDist) << endl;
    // int highTime = 1e9 + 1, lowTime = 0;
    // int mid = -1;
    // while (highTime > lowTime){
    //     mid = lowTime + (highTime - lowTime)/2;
    //     auto chk = check(dist, speed, D, mid);
    //     if (!chk){
    //         lowTime = mid + 1; 
    //     }else if(check(dist, speed, D, mid + 1)){
    //        highTime = mid;
    //     }else{
    //         break;
    //     }
    // }
    // cerr << mid<<"#";
    // highTime = 1e8 + 1, lowTime = 0;
    // while(highTime > lowTime){
    //     auto middle = lowTime + (highTime - lowTime)/2;
    //     auto md = (static_cast<double>(lowTime + (highTime - lowTime)/2) / static_cast<double>(1e8));
    //     cerr << md << "==>";
    //     auto chk = check(dist, speed, D, mid + md);
    //     if (!chk){
    //         lowTime = middle + 1;
    //         cerr << mid + md << "->"<<endl; 
    //     }else if(check(dist, speed, D, mid + md + 1e-6)){
    //         highTime = middle;
    //         cerr << mid + md << "->"<<endl; 
    //     }else{
    //         cout << D / mid + md << endl;
    //         return;
    //     }
    // }
    // cout << D / mid << endl;
}

int main(){
    int t; 
    cin >> t;
    for (int i = 1; i <=t ; ++i){
        cout << "Case #" << i << ": ";
        solve();
    }
}