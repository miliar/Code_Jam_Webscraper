#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#include "queue"
#include <functional>
#include <climits>
#include <cstring>
#include <ctime>
#include <list>
#include <iomanip>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <limits>
#include <complex>

#define int64 unsigned long long

#include <iostream>

using namespace std;


string Fill(char c1, char c2, int count) {
    string str(2 * count, '!');
    for (int i = 0; i < str.size(); i += 2) {
        str[i] = c2;
    }
    for (int i = 1; i < str.size(); i += 2) {
        str[i] = c1;
    }
    return str;
    
}


string Get2(int n, int R, int Y, int B) {
    vector<pair<int, char>> data;
    data.push_back({R, 'R'});
    data.push_back({Y, 'Y'});
    data.push_back({B, 'B'});
    sort(data.rbegin(), data.rend());
    string res(n, '!');
    int p = 0;
    while (data[0].first != 0) {
        if (p >= res.size() - 1) break;
        res[p] = data[0].second;
        p += 2;
        --data[0].first;
    }
    if (data[0].first != 0) {
        return "IMPOSSIBLE";
    }
    
    while (data[1].first != 0) {
        if (p >= res.size()) break;
        res[p] = data[1].second;
        p += 2;
        --data[1].first;
    }
    p = 1;
    while (data[1].first != 0) {
        if (p >= res.size()) break;
        res[p] = data[1].second;
        p += 2;
        --data[1].first;
    }
    while (data[2].first != 0) {
        if (p >= res.size()) break;
        res[p] = data[2].second;
        p += 2;
        --data[2].first;
    }
    assert(data[0].first == 0);
    assert(data[1].first == 0);
    assert(data[2].first == 0);
    for (int i = 0; i < n - 1; ++i) {
        if (res[i] == res[i + 1]) return "IMPOSSIBLE";
    }
    if (res[0] == res[n - 1]) {
        return "IMPOSSIBLE";
    }
    return res;
    
}

string replace(string str, char c, string r) {
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == c) {
            return str.substr(0, i + 1) + r + str.substr(i + 1);
        }
    }
    assert(false);
}

string Get1(int n, int R, int O, int Y, int G , int B, int V) {
    if (O > B) {
        return "IMPOSSIBLE";
    }
    if (G > R) {
        return "IMPOSSIBLE";
    }
    if (V > Y) {
        return "IMPOSSIBLE";
    }
    
    string str1 = Fill('B', 'O', O);
    string str2 = Fill('R', 'G', G);
    string str3 = Fill('Y', 'V', V);
    
    if (O == B && O != 0) {
        if (n > O + B) return "IMPOSSIBLE";
        return str1;
    }
    if (G == R && G != 0) {
        if (n > G + R) return "IMPOSSIBLE";
        return str2;
    }
    if (V == Y && V != 0) {
        if (n > V + Y) return "IMPOSSIBLE";
        return str3;
    }
    int newN = n - 2 * O - 2 * G - 2 * V;
    int newB = B - O;
    int newR = R - G;
    int newY = Y - V;
    assert(newN == newB + newR + newY);
    if (newN == 0) {
        
    }
    string res = Get2(newN, newR, newY, newB);
    if (res == "IMPOSSIBLE") {
        return "IMPOSSIBLE";
    }
    if (newB > 0) {
        if (O == 0) {
            assert(str1.size() == 0);
        }
        res = replace(res, 'B', str1);
    }
    if (newR > 0) {
        if (G == 0) {
            assert(str2.size() == 0);
        }
        res = replace(res, 'R', str2);
    }
    if (newY > 0) {
        if (V == 0) {
            assert(str3.size() == 0);
        }
        res = replace(res, 'Y', str3);
    }
    return res;
}

int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);
    
    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        
        int n;
        cin >> n;
        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V;
        string res = Get1(n, R, O, Y, G, B, V);
        
        
        cout << "Case #" << t + 1 << ": " << res << endl;
    }
    return 0;
}
