#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int T;
char c[20];

bool check(vector<int> v){
    for (int i = 1; i < v.size(); ++i){
        if (v[i - 1] > v[i]){
            return false;
        }
    }
    return true;
}

vector<int> iter(vector<int> v){
    for (int i = 1; i < v.size(); ++i){
        if (v[i - 1] > v[i]){
            v[i - 1] --;
            for (int j = i; j < v.size(); ++j){
                v[j] = 9;
            }
            return v;
        }
    }
    return v;
}

vector<int> solve(vector<int> v){
    while(!check(v)){
        v = iter(v);
    }
    vector<int> ans;
    for (int i = 0; i < v.size(); ++i){
        if (v[i] == 0 && ans.size() == 0)
            continue;
        ans.push_back(v[i]);
    }
    return ans;
}

int main(){
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t){
        vector<int> v;
        cin >> c;
        for (int i = 0; c[i] != '\0'; ++i){
            v.push_back(c[i] - '0');
        }
        cout << "Case #" << t << ": ";
        v = solve(v);
        for (int i = 0; i < v.size(); ++i){
            cout << v[i];
        }
        cout << endl;
    }
    return 0;
}
