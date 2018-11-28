#define problem "B-large"
#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen(problem".in", "r", stdin);
    freopen(problem".out", "w", stdout);
    int test;
    cin >> test;
    for(int test_case = 1; test_case <= test; test_case++){
        long long N;
        cin >> N;
        vector<int> v;
        while(N){
            v.push_back(N % 10);
            N /= 10;
        }
        reverse(v.begin(), v.end());
        long long ans = 0;
        for(int i = 0; i < (int)v.size() - 1; i++) ans = ans * 10 + 9;
        for(int i = 1; i < (int)v.size(); i++) if(v[i] < v[i - 1]){
            int j = i - 1;
            while(j > 0 && v[j] == v[j - 1]) j--;
            v[j]--;
            for(int k = j + 1; k < (int)v.size(); k++) v[k] = 9;
            break;
        }
        long long tmp = 0;
        for(int i = 0; i < (int)v.size(); i++) tmp = tmp * 10 + v[i];
        printf("Case #%d: %I64d\n", test_case, max(ans, tmp));
    }
}
