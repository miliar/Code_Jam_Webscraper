
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <sstream>

#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>

using namespace std;

string count(int N, int R, int O, int Y, int G, int B, int V) {
    if (O && O >= B) {
        if (N == 2*O) {
            string res;
            for (int i = 0; i < N/2; ++i) res.append("OB");
            return res;
        }
        else return "IMPOSSIBLE";
    }
    if (G && G >= R) {
        if (N == 2*G) {
            string res;
            for (int i = 0; i < N/2; ++i) res.append("GR");
            return res;
        }
        else return "IMPOSSIBLE";
    }
    if (V && V >= Y) {
        if (N == 2*Y) {
            string res;
            for (int i = 0; i < N/2; ++i) res.append("VY");
            return res;
        }
        else return "IMPOSSIBLE";
    }
    
    B -= O; R -= G; Y -= V;
    
    vector<pair<char, int>> vec = {{'B', B}, {'R', R}, {'Y', Y}};
    sort(vec.begin(), vec.end(), [](pair<char, int>& a, pair<char, int>& b){ return a.second < b.second; });
    
    if (vec[0].second + vec[1].second < vec[2].second) return "IMPOSSIBLE";
    int temp = vec[0].second + vec[1].second - vec[2].second;
    
    string res;
    for (int i = 0; i < vec[0].second - temp; ++i) {
        res.push_back(vec[0].first);
        res.push_back(vec[2].first);
    }
    for (int i = 0; i < temp; ++i) {
        res.push_back(vec[0].first);
        res.push_back(vec[1].first);
        res.push_back(vec[2].first);
    }
    for (int i = 0; i < vec[1].second - temp; ++i) {
        res.push_back(vec[1].first);
        res.push_back(vec[2].first);
    }
    
    for (int i = 0; i < res.size(); ++i) {
        string temp;
        if (res[i] == 'B') {
            for (int j = 0; j < O; ++j)
                temp.append("OB");
            res.insert(i+1, temp);
            break;
        }
    }
    for (int i = 0; i < res.size(); ++i) {
        string temp;
        if (res[i] == 'R') {
            for (int j = 0; j < G; ++j)
                temp.append("GR");
            res.insert(i+1, temp);
            break;
        } 
    }
    for (int i = 0; i < res.size(); ++i) {
        string temp;
        if (res[i] == 'Y') {
            for (int j = 0; j < V; ++j)
                temp.append("VY");
            res.insert(i+1, temp);
            break;
        }
    }
    
    return res;
}


int main(){
    int n; cin >> n;
    
    int N, R, O, Y, G, B, V;
    for (int i = 1; i <= n; ++i) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string res = count(N, R, O, Y, G, B, V);
        

        cout << "Case #" << i << ": " << res << endl;
    }
    
    return 0;
}