#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

string m[30];
int r, c;

int get(string &s, int l, int r){
    for (int i = l; i < r; i++)
        if (s[i] != '?')
            return i;
    return -1;
}

set<int> visited;
string get(int i){
    if (visited.find(i) != visited.end())
        return "";
    visited.insert(i);
    if (i < 0 || i >= r)
        return "";
    if (m[i][0] != '?')
        return m[i];
    else{
        string top = get(i-1);
        if (top.size() != 0)
            return m[i] = top;
        return m[i] = get(i+1);
    }
}

int main(){ _
    int t;
    cin >> t;
    for (int q = 1; q <= t; q++){
        cin >> r >> c;
        for (int i = 0; i < r; i++)
            cin >> m[i];
        vector<int> aux;
        for (int i = 0; i < r; i++){
            int l = 0;
            while (l < c){
                int first = get(m[i], l, c);
                if (first == -1){
                    aux.push_back(i);
                    break;
                }
                while (l < c && (m[i][l] == m[i][first] || m[i][l] == '?'))
                    m[i][l++] = m[i][first];
            }
        }
        for (int i = 0; i < aux.size(); i++){
            visited.clear();
            m[aux[i]] = get(aux[i]);
        }
        cout << "Case #" << q << ": " << endl;
        for(int i = 0; i < r; i++){
            cout << m[i] << endl;
        }
    }
	return 0;
}
