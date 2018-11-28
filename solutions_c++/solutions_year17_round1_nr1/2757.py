#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <set>

using namespace std;

bool up(vector<string> &m, int r, int c) {
    char ch=m[r-1][c];
    m[r][c] = ch;
    for(int i=c-1;i>=0 && m[r-1][i]==ch;i--) {
        if(m[r][i] != '?') return false;
        m[r][i] = ch;
    }
    for(int i=c+1;i<m[0].size() && m[r-1][i]==ch;i++) {
        if(m[r][i] != '?') return false;
        m[r][i] = ch;
    }

    return true;
}
bool down(vector<string> &m, int r, int c) {
    char ch=m[r+1][c];
    m[r][c] = ch;
    for(int i=c-1;i>=0 && m[r+1][i]==ch;i--) {
        if(m[r][i] != '?') return false;
        m[r][i] = ch;
    }
    for(int i=c+1;i<m[0].size() && m[r+1][i]==ch;i++) {
        if(m[r][i] != '?') return false;
        m[r][i] = ch;
    }

    return true;
}
bool left(vector<string> &m, int r, int c) {
    char ch=m[r][c-1];
    m[r][c] = ch;
    for(int i=r-1;i>=0 && m[i][c-1]==ch;i--) {
        if(m[i][c] != '?') return false;
        m[i][c] = ch;
    }
    for(int i=r+1;i<m.size() && m[i][c-1]==ch;i--) {
        if(m[i][c] != '?') return false;
        m[i][c] = ch;
    }
    return true;
}
bool right(vector<string> &m, int r, int c) {
    char ch=m[r][c+1];
    m[r][c] = ch;
    for(int i=r-1;i>=0 && m[i][c+1]==ch;i--) {
        if(m[i][c] != '?') return false;
        m[i][c] = ch;
    }
    for(int i=r+1;i<m.size() && m[i][c+1]==ch;i--) {
        if(m[i][c] != '?') return false;
        m[i][c] = ch;
    }
    return true;
}

int main() {
    int T;

    cin >> T;
    for(int cs=1; cs<=T; cs++) {
        int R,C;
        cin >> R >> C;
        vector<string> m(R);
        for(int i=0;i<R;i++) cin >> m[i];

        deque<vector<string> > q;
        set<vector<string> > ss;
        vector<string> t,tt;

        q.push_back(m);
        ss.insert(m);
        while(!q.empty()) {
            t = q.front(); q.pop_front();
            tt = t;
            bool found = false;

            for(int i=0;i<R;i++) {
                for(int j=0;j<C;j++) {
                    if(t[i][j] == '?') {
                        found = true;

                        if(i-1>=0 && t[i-1][j]!='?') {
                            if(up(t, i, j)) {
                                if(ss.find(t) == ss.end()) {
                                    q.push_back(t);
                                    ss.insert(t);
                                }
                            }
                            t = tt;
                        }

                        if(i+1<R && t[i+1][j]!='?') {
                            if(down(t, i,j)) {
                                if(ss.find(t) == ss.end()) {
                                    q.push_back(t);
                                    ss.insert(t);
                                }
                            }
                            t = tt;
                        }

                        if(j-1>=0 && t[i][j-1]!='?') {
                            if(left(t, i,j)) {
                                if(ss.find(t) == ss.end()) {
                                    q.push_back(t);
                                    ss.insert(t);
                                }
                            }
                            t = tt;
                        }

                        if(j+1<C && t[i][j+1]!='?') {
                            if(right(t, i,j)) {
                                if(ss.find(t) == ss.end()) {
                                    q.push_back(t);
                                    ss.insert(t);
                                }
                            }
                            t = tt;
                        }
                    }
                }
            }

            if(found == false) break;
        }

        printf("Case #%d:\n", cs);
        for(int i=0;i<R;i++) cout << t[i] << endl;
    }

    return 0;
}
