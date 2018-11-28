#include<iostream>
#include <cstdio>      
#include <cstdlib>     
#include <ctime>       
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>

using namespace std;

const int maxn = 1000000 + 100;

typedef pair<int, int> iPair;

int k;
string str;

bool isHappy(string st) {

    for(int i=0; i<st.length(); i++) {
        if (st[i] == '-') {
            return false;
        }
    }

    return true;
}

string flip(string st, int u) {
    
    string s = st;
    for(int i=0; i<k; i++) {
        if (s[u+i] == '-') {
            s[u+i] = '+';
        } else {
            s[u+i] = '-';
        }
    }

    return s;
}

int dfs() {

    map<string, int> q;
    q.clear();
    q[str] = 0;

    priority_queue<iPair, vector<iPair>, greater<iPair> > pq;
    pq.push(make_pair(0, 0));

    vector<string> s;
    s.push_back(str);

    int f[maxn];
    f[0] = 0;
    int n = 1;

    while (!pq.empty()) {

        int u = pq.top().second;
        pq.pop();

        string st = s[u];

        if (isHappy(st)) {
            return f[u];
        }

        for(int i=0; i+k-1<st.length(); i++) {
            string temp = flip(st, i);

            if(q.find(temp) == q.end()) {
                f[n] = f[u] + 1;
                q[temp] = n;
                s.push_back(temp);
                pq.push(make_pair(f[n], n));
                n++;
            } else {
                int v = q[temp];
                if (f[v] > f[u] + 1) {
                    f[v] = f[u] + 1;
                    pq.push(make_pair(f[v], v));
                }
            }
        }
    }

    return -1;
}


int main() {

    std::ios::sync_with_stdio(false);
	freopen("a-small-in.txt", "r", stdin);
	freopen("a-small-out.txt", "w", stdout);

    int test;
    cin >> test;

    for(int t=1; t<=test; t++) {
    	cin >> str >> k;

    	int res = dfs();

        if (res == -1) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << t << ": " << res << endl;
        }
    }

    // cout << "DONE" << endl;
    return 0;
}