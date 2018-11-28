#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <tuple>
typedef long long ll;
using namespace std;
int t,n,k;
double u, a, b;

void solve(int Case){
    vector<double> probs;
    cin >> n >> k;
    cin >> u;
    double sum = 0;
    for(int i=0; i<n; i++){
        cin >> a;
        probs.push_back(a);
        sum += a;
    }
    if(sum + u >= n-0.0000001){
        cout << "Case #" << Case << ": " << 1.0 << "\n";
        return;
    }
    sort(probs.begin(), probs.end());
    probs.push_back(1.0);
    probs.push_back(2.0);
    int num = 1;
    while(u >= (probs[num] - probs[num-1])*num ){
        u -= (probs[num] - probs[num-1])*num;
        for(int i=0; i<num; i++){
            probs[i] = probs[num];
        }
        num++;
    }
    for(int i=0; i<num; i++){
        probs[i] += u/num;
    }
    double prob = 1;
    for(int i=0; i<n; i++){
        prob *= probs[i];
    }
    cout << "Case #" << Case << ": " << prob << "\n";
}



int main()
{
    ios::sync_with_stdio(false);
    cout.precision(10);
    cout << fixed;
    cin >> t;
    for(int i=0; i<t; i++){
        solve(i+1);
    }
    return 0;
}