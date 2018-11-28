//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void arreglar2(string &st) {
    for(int times=0;times<50;times++) {
        for(int i=0;i<st.size()-1;i++) {
            if(st[i] == '?' && st[i+1] != '?') {
                st[i] = st[i+1];
            }
            if(st[i+1] == '?' && st[i] != '?') {
                st[i+1] = st[i];
            }
        }
    }
    return;
}

void arreglar(vector<string> &vec) {
    for(int i=0;i<vec.size();i++) {
        if(count(vec[i].begin(),vec[i].end(),'?') != vec[i].size()) {
            arreglar2(vec[i]);
        }
    }
    for(int times=0;times<50;times++) {
        for(int i=0;i<vec.size()-1;i++) {
            if(vec[i][0] == '?' && vec[i+1][0] != '?') {
                vec[i] = vec[i+1];
            }
            if(vec[i+1][0] == '?' && vec[i][0] != '?') {
                vec[i+1] = vec[i];
            }
        }
    }
}

int main() {
    int casos;
    cin >> casos;
    for(int casito = 1; casito <= casos; casito++) {
        int r,c;
        cin >> r >> c;
        vector<string> vec(r);
        for(int i=0;i<r;i++) {
            cin >> vec[i];
        }
        arreglar(vec);
        cout << "Case #" << casito <<": " << endl;
        for(int i=0;i<r;i++) {
            cout << vec[i] << endl;
        }
    }
}