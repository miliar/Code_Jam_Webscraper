#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 5;

const char s[3][5] = {"R", "B", "Y"};

string makePattern(vector<int> v1, vector<int> v2) {
    string p;
    int last = -1;
    while(v1[0] || v1[1] || v1[2]) {
        int cur = last;
        int mx = 0;
        for(int i=0;i<3;i++) {
            if (v2[i] != last) {
                if (v1[v2[i]] > mx) {
                    cur = v2[i];
                    mx = v1[v2[i]];
                }
            }
        }
        if (cur == last) return string("");
        v1[cur]--;
        p.append(string(s[cur]));
        last = cur;
    }
    return p;
}

string generate(int b, const char *st) {
    if (b == 0) return string("");
    char s[10002];
    int i = 0;
    while(b) {
        s[i++] = st[0];
        s[i++] = st[1];
        b--;
    }
    s[i++] = st[0];
    s[i] = '\0';
    return string(s);
}

int main() {
    int t;
    scanf("%d", &t);
    int te = 1;
    while(te <= t) {
        int n, r, o, y, g, b, v;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: ", te++);
        if (r == 0 && y == 0 && g == 0 && v == 0) {
            if (b == o) {
                for(int i=0;i<n;i+=2) {
                    printf("BO");
                }
                printf("\n");
            }
            else {
                printf("IMPOSSIBLE\n");
            }
            continue;
        }
        if (o == 0 && y == 0 && b == 0 && v == 0) {
            if (r == g) {
                for(int i=0;i<n;i+=2) {
                    printf("RG");
                }
                printf("\n");
            }
            else {
                printf("IMPOSSIBLE\n");
            }
            continue;
        }
        if (r == 0 && o == 0 && g == 0 && b == 0) {
            if (y == v) {
                for(int i=0;i<n;i+=2) {
                    printf("YV");
                }
                printf("\n");
            }
            else {
                printf("IMPOSSIBLE\n");
            }
            continue;
        }
        if (g) {
            r -= g+1;
            if (r < 0) {
                printf("IMPOSSIBLE\n");
                continue;
            }
        }
        if (o) {
            b -= o+1;
            if (b < 0) {
                printf("IMPOSSIBLE\n");
                continue;
            }
        }
        if (v) {
            y -= v+1;
            if (y < 0) {
                printf("IMPOSSIBLE\n");
                continue;
            }
        }
        vector<int> v1, v2, v3;
        map<char, int> m;
        m['R'] = 0;
        m['B'] = 1;
        m['Y'] = 2;
        v3.push_back(g);
        v3.push_back(o);
        v3.push_back(v);
        v1.push_back(r);
        v1.push_back(b);
        v1.push_back(y);
        v2.push_back(0);
        v2.push_back(1);
        v2.push_back(2);
        bool found = false;
        string resp;
        for(int i=0;i<6;i++) {
            string s = makePattern(v1, v2);
            if (s.size()) {
                if (s[0] == s[s.size()-1]) {
                    if (s[0] == 'R' && g && o && v) {
                        resp = generate(o, "BO");
                        resp.append(generate(g, "RG"));
                        resp.append(generate(v, "YV"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                    if (s[0] == 'R' && !g && (o || v)) {
                        resp = generate(o, "BO");
                        resp.append(generate(g, "RG"));
                        resp.append(generate(v, "YV"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                    if (s[0] == 'B' && g && o && v) {
                        resp = generate(g, "RG");
                        resp.append(generate(o, "BO"));
                        resp.append(generate(v, "YV"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                    if (s[0] == 'B' && !o && (g || v)) {
                        resp = generate(g, "RG");
                        resp.append(generate(o, "BO"));
                        resp.append(generate(v, "YV"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                    if (s[0] == 'Y' && g && o && v) {
                        resp = generate(o, "BO");
                        resp.append(generate(v, "YV"));
                        resp.append(generate(g, "RG"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                    if (s[0] == 'Y' && !v && (o || g)) {
                        resp = generate(o, "BO");
                        resp.append(generate(v, "YV"));
                        resp.append(generate(g, "RG"));
                        resp.append(s);
                        found = true;
                        break;
                    }
                }
                else {
                    if (v == 0 && g == 0 && o == 0) {
                        resp = s;
                        found = true;
                        break;
                    }
                    if (s[0] == 'R') {
                        if (s[s.size()-1] == 'B' && (v || o && g)) {
                            resp = generate(r, "RG");
                            resp.append(generate(v, "YV"));
                            resp.append(generate(o, "BO"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                        if (s[s.size()-1] == 'Y' && (o || v && g)) {
                            resp = generate(r, "RG");
                            resp.append(generate(o, "BO"));
                            resp.append(generate(v, "YV"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                    }
                    if (s[0] == 'B') {
                        if (s[s.size()-1] == 'R' && (v || o && g)) {
                            resp = generate(o, "BO");
                            resp.append(generate(v, "YV"));
                            resp.append(generate(r, "RG"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                        if (s[s.size()-1] == 'Y' && (g || v && o)) {
                            resp = generate(o, "BO");
                            resp.append(generate(r, "RG"));
                            resp.append(generate(v, "YV"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                    }
                    if (s[0] == 'Y') {
                        if (s[s.size()-1] == 'B' && (g || o && v)) {
                            resp = generate(v, "YV");
                            resp.append(generate(g, "RG"));
                            resp.append(generate(o, "BO"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                        if (s[s.size()-1] == 'R' && (o || v && g)) {
                            resp = generate(v, "YV");
                            resp.append(generate(o, "BO"));
                            resp.append(generate(g, "RG"));
                            resp.append(s);
                            found = true;
                            break;
                        }
                    }
                }
            }
            swap(v2[i%2], v2[i%2+1]);
        }       
        if (found) {
            printf("%s\n", resp.c_str());
            continue;
        }
        printf("IMPOSSIBLE\n");
    } 
    return 0;
}

