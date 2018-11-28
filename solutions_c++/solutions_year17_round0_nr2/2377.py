#include <bits/stdc++.h>
using namespace std;

typedef long long llong;

vector<int> llongToVector(llong n){
    vector<int> dig;
    while (n){
        dig.push_back(n%10);
        n /= 10;
    }
    return vector<int>(dig.rbegin(), dig.rend());
}

llong vectorToLlong(vector<int> &n){
    llong ans = 0;
    for (int i = 0; i < n.size(); i++){
        ans *= 10;
        ans += n[i];
    }
    return ans;
}

void tyde(vector<int> &n){
    for (int i = 1; i < n.size(); i++){
        if (n[i] < n[i-1]){
            n[i-1]--;
            for (int j = i; j < n.size(); j++)
                n[j] = 9;
            i = max(i-2, 0);
        }
    }
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        llong n;
        cin >> n;
        vector<int> dg = llongToVector(n);
        tyde(dg);
        cout << "Case #" << cases++ << ": " << vectorToLlong(dg) << endl;

    }
    return 0;
}
