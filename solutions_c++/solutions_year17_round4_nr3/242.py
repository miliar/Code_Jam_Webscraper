#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>
#include <iomanip>
#include <vector>
#include <cstring>
#include <stack>
typedef std::pair<int, int> ii;

const int MAXX = 64;

char m[MAXX][MAXX];
char ans[MAXX][MAXX];
int r, c;

static const ii D[]={
    ii(0, 1), ii(-1, 0), ii(0, -1), ii(1, 0)
};

static ii operator+(ii a, ii b) {
    return ii(a.first + b.first, a.second + b.second);
}

static bool good(ii p) {
    return p.first >= 0 && p.first < r && p.second >=0 && p.second < c;
}


int hid[MAXX][MAXX];
int vid[MAXX][MAXX];
//int HMASK = (1 << 20);

bool canShoot(int y, int x, int dir) {
    ii cp(y, x);
    bool first = true;
    //std::cerr << "-----\n";
    while (true) {
     //  std::cerr << "cp " << cp.first << " " << cp.second << "\n";
        char tc = '.';
        if (!first)
        {
            if (!good(cp)) return true;
            tc = m[cp.first][cp.second];
            if (tc == '#') return true;
            if (tc == '-' || tc == '|') return false;
        }
        else
        {
            first = false;
        }
        
        if (tc == '/') {
            dir ^= 1;
        } else if (tc == '\\') {
            dir ^= 3;
        }
        cp = cp + D[dir];
    }
    return true;
}


bool mark(int y, int x, int dir, int marker) {
    ii cp(y, x);

    bool first = true;
    while (true) {
        char tc = '.';
        if (!first)
        {
            if (!good(cp)) return true;
            tc = m[cp.first][cp.second];
            if (tc == '#') return true;
            if (tc == '-' || tc == '|') return false;
            if (tc == '.') {
                if ((dir & 1) == 0) {
                    hid[cp.first][cp.second] = marker;
                } else {
                    vid[cp.first][cp.second] = marker;
                }
            }
        }
        else
        {
            first = false;
        }
        
        
        if (tc == '/') {
            dir ^= 1;
        } else if (tc == '\\') {
            dir ^= 3;
        }
        cp = cp + D[dir];
    }
}
/*
static int transformId(int v) {
    int mv = v & HMASK;
    v ^= mv;
    v <<= 1;
    if (mv) v|= 1;
    return v;
}
*/
static int getId(int i, int j) {
    
    return (i|(j<<6))<<1;
}

std::vector<int> truth;
std::vector<std::vector<int> > G;
std::vector<int> valid;

static const int MAXN = 1 << 13;
int nextIndex;
int vindex[MAXN];
int lowl[MAXN];
int inStack[MAXN];
int isFixed[MAXN];

std::stack<int> S;
static bool strongConnect(int v) {
    vindex[v] = nextIndex;
    lowl[v] = nextIndex;
    nextIndex++;
    
    S.push(v);
    inStack[v] = 1;
    for (int tg : G[v]) {
        if (vindex[tg] < 0) {
            bool r = strongConnect(tg);
            if (!r) return false;
            lowl[v] = std::min(lowl[v], lowl[tg]);
        } else if (inStack[tg]) {
            lowl[v] = std::min(lowl[v], vindex[tg]);
        }
    }
    if (lowl[v] == vindex[v]) {
        std::vector<int> component;
        int cid = -1;
        do {
            cid = S.top(); S.pop();
            inStack[cid] = 0;
            component.push_back(cid);
        } while (cid != v);

        std::sort(component.begin(), component.end());
        for (size_t j=1; j<component.size(); j++) {
            if (component[j] == (component[j-1]^1)) return false;
        }
        bool isTrue = false;
        bool isFalse = false;
        for (auto f : component) {
            if (truth[f]) isTrue = true;
            if (truth[f^1]) isFalse = true;
        }
        if (isTrue && isFalse) return false;
        if (isTrue) {
            for (auto f : component) {
                truth[f] = 1;
            }
        } else if (isFalse) {
            for (auto f : component) {
                truth[f^1] = 1;
            }
        } else {
            for (auto f : component) {
                truth[f] = 1;
            }
        }
    }
    return true;
}

bool solve()
{
    memset(ans, 0, sizeof(ans));
    std::vector<ii> bidir;
    valid.assign(MAXN, 0);
    
    memset(hid, 0xff, sizeof(hid));
    memset(vid, 0xff, sizeof(vid));
    memset(isFixed, 0, sizeof(isFixed));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            char cc = m[i][j];
            if (cc != '|' && cc != '-') continue;
            bool canh = canShoot(i, j, 0) && canShoot(i, j, 2);
            bool canv = canShoot(i, j, 1) && canShoot(i, j, 3);
         //   std::cerr << "p " << i << " " << j << " " << canh << canv << "\n";
            if (canv == false && canh == false) return false;
            if (canh && canv) {
                bidir.push_back(ii(i, j));
                int id1 = getId(i, j);
                valid[id1] = valid[id1^1] = 1;
            } else {
                isFixed[getId(i, j)] = isFixed[getId(i, j)^1] = 1;
             //          std::cerr << "p2 " << i << " " << j << " " << canh << canv << "\n";
                if (canh) {
                    ans[i][j] = '-';
                } else {
                    ans[i][j] = '|';
                }
            }
        }
    }
    
    for (auto pos : bidir) {
        int baseId = getId(pos.first, pos.second);
        for (int j=0; j<4; j++) 
            mark(pos.first, pos.second, j, baseId + (j & 1));
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            
            if (ans[i][j] == '-') {
                int id = getId(i, j);
                mark(i, j, 0, id);
                mark(i, j, 2, id);
            } else if (ans[i][j] == '|') {
                int id = getId(i, j)+1;
                mark(i, j, 1, id);
                mark(i, j, 3, id);
            }
        }
    }
    
    std::vector<ii> rules;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] != '.') continue;
            if ((hid[i][j] >= 0 && isFixed[hid[i][j]]) ||
                (vid[i][j] >= 0 && isFixed[vid[i][j]])) {
                continue;
            }
            if (hid[i][j] < 0 && vid[i][j] < 0) {
                return false;
            }
            if (hid[i][j] < 0) {
                rules.push_back(ii(vid[i][j], vid[i][j]));
            } else if (vid[i][j] < 0) {
                rules.push_back(ii(hid[i][j], hid[i][j]));
            } else {
                rules.push_back(ii(hid[i][j], vid[i][j]));
            }
        }
    }
    truth.assign(MAXN, 0);
    G.clear();
    G.resize(MAXN);
    for (auto rule : rules) {
        int a = rule.first, b = rule.second;
      //  std::cerr << "rl "  << a << " " << b << "\n";
        G[a^1].push_back(b);
        G[b^1].push_back(a);
    }
    nextIndex = 0;
    memset(vindex, 0xff, sizeof(vindex));
    memset(inStack, 0, sizeof(inStack));
    S = std::stack<int>();
    for (int i = 0; i<MAXN; i++) {
        if (valid[i]==1 && vindex[i] < 0) {
            if (!strongConnect(i)) return false;
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            char cc = m[i][j];
            if (cc != '|' && cc != '-') {
                ans[i][j] = m[i][j];
            } else {
                if (ans[i][j]) continue;
                int id1 = getId (i, j);
                if (truth[id1] && truth[id1^1]) {
                    std::cerr << "BAD!!!\n";
                }
                if (truth[id1] == 0 && truth[id1^1] == 0) {
                    std::cerr << "BAD!!!\n";
                }
                if (truth[id1]) {
                    ans[i][j] = '-';
                } else {
                    ans[i][j] = '|';
                }
            }
        }
    }
    
    return true;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::cin >> r >> c;
        for (int j = 0; j < r; j++) {
            std::cin >> m[j];
        }
        std::cout << "Case #" << i << ": ";
        if (solve()) {
            std::cout << "POSSIBLE\n";
            for (int j = 0; j < r; j++) {
                ans[j][c] = 0;
                std::cout << ans[j] << "\n";
            }
        } else {
            std::cout << "IMPOSSIBLE\n";
        }
    }
}
