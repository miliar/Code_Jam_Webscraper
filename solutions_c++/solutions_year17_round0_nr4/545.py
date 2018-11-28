#include<bits/stdc++.h>

using namespace std;

vector<vector<char>> v;
vector<int> r, c, d1, d2;
vector<int> ans1, ans2;
vector<char> ansc;
unordered_map<int, char> mp;

ifstream fin("inputD.txt");
ofstream fout("outputD.txt");
#define cin fin
#define cout fout

void f(){
    int n;
    cin >> n;
    int ans = 0;
    vector<vector<char>> v(n, vector<char>(n, '.'));
    r.resize(n, 0);
    c.resize(n, 0);
    d1.resize(2*n, 0);
    d2.resize(2*n, 0);
    int m;
    cin >> m;
    for(int i = 0; i < m; ++i){
        char ch;
        int ri, ci;
        cin >> ch >> ri >> ci;
        --ri;
        --ci;
        mp[ri * 1000 + ci] = ch;
        v[ri][ci] = ch;
        #define i ri
        #define j ci
        if(ch == '+' || ch == 'o'){
            d1[i + j] = 1;
            d2[i - j + n] = 1;
            ++ans;
        }
        if(ch == 'x' || ch == 'o'){
            r[i] = 1;
            c[j] = 1;
            ++ans;
        }
        #undef i
        #undef j
    }
    for(int j = 0; j < n; ++j){
        if(v[0][j] == 'x'){
            v[0][j] = 'o';
            d1[0 + j] = 1;
            d2[0 - j + n] = 1;
            ++ans;
        }
        if(v[0][j] == '.'){
            v[0][j] = '+';
            d1[0 + j] = 1;
            d2[0 - j + n] = 1;
            ++ans;
        }
    }
    for(int j = 1; j < n-1; ++j){
        v[n-1][j] = '+';
        d1[n-1 + j] = 1;
        d2[n-1 - j + n] = 1;
        ++ans;
    }
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
//            if(r[i] == 0 && c[j] == 0 && d1[i + j] == 0 && d2[i - j + n] == 0){
//                v[i][j] = 'o';
//                r[i] = 1;
//                c[j] = 1;
//                ++ans;
//                d1[i + j] = 1;
//                d2[i - j + n] = 1;
//                ++ans;
//            }
            if(r[i] == 0 && c[j] == 0){
                if(v[i][j] == '+'){
                    v[i][j] = 'o';
                }
                else if(v[i][j] == '.'){
                    v[i][j] = 'x';
                }
                r[i] = 1;
                c[j] = 1;
                ++ans;
            }
//            else if(d1[i + j] == 0 && d2[i - j + n] == 0){
//                v[i][j] = '+';
//                d1[i + j] = 1;
//                d2[i - j + n] = 1;
//                ++ans;
//            }
        }
    }
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if(mp[i*1000 + j] != v[i][j] && v[i][j] != '.'){
                ans1.push_back(i);
                ans2.push_back(j);
                ansc.push_back(v[i][j]);
            }
        }
    }
    cout << ans << ' ' << ans1.size() << endl;
    for(int i = 0; i < ans1.size(); ++i){
        cout << ansc[i] << ' ' << ans1[i]+1 << ' ' << ans2[i]+1 << endl;
    }
//    cout << ans << endl;
//    for(int i = 0; i < v.size(); ++i){
//        for(int j = 0; j < v.size(); ++j){
//            cout << v[i][j];
//        }
//        cout << endl;
//    }
}

int32_t main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i){
        v.clear();
        r.clear();
        c.clear();
        d1.clear();
        d2.clear();
        ans1.clear();
        ans2.clear();
        ansc.clear();
        mp.clear();
        cout << "Case #" << i+1 << ": ";
        f();
    }
}
