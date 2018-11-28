
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
//#include "optimization.h"

using namespace std;

int c[256];

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t;
    long long n;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cin >> n;
        vector<int> v;
        while (n){
            v.push_back(n % 10);
            n /= 10;
        }
        bool bb= false;
        reverse(v.begin(), v.end());
        bool good[20];
        good[0] = true;
        for (int i = 1; i < v.size(); i++)
            good[i] = (good[i-1] & (v[i] >= v[i-1]));
        if (!good[v.size() - 1]){
            for (int i = v.size() - 1; i >= 0; i--){
                if (good[i] && (i == 0 || v[i] != v[i - 1])){
                    v[i]--;
                    for (int j = i + 1; j < v.size(); j++)
                        v[j] = 9;
                    break;
                }
            }
        }
        int pos = 0;
        while (v[pos] == 0 && pos != v.size())
            pos++;
        cout << "Case #" << tt << ": ";
        for (int i = pos; i < v.size(); i++)
            cout << v[i];
        cout << "\n";
    }
    return 0;
}
