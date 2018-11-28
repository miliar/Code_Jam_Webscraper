#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

int a[6];
const std::string sym[] = {"R", "O", "Y", "G", "B", "V"};

bool read() {
    int n;
    assert(scanf("%d", &n) == 1);
    for (int i = 0; i < 6; i++) {
        assert(scanf("%d", &a[i]) == 1);
    }
    return true;
}

std::vector<std::string> s[6];

bool prepare(int mixedId, int id) {
    while (s[mixedId].size() > 0) {
        if (s[id].size() >= 2) {
            std::string res = s[id].back();
            s[id].pop_back();
            res += s[mixedId].back();
            s[mixedId].pop_back();
            res += s[id].back();
            s[id].pop_back();
            s[id].push_back(res);
        } else {
            return false;
        }
    }
    return true;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    for (int i = 0; i < 6; i++) {
        s[i].clear();
    }
    
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < a[i]; j++) {
            s[i].push_back(sym[i]);
        }
    }
    
    bool good = prepare(1, 4) && prepare(3, 0) && prepare(5, 2);
    
    if (!good) {
        if (s[1].size() + s[3].size() + s[5].size() == 1) {
            int mixedId = s[1].size() > 0 ? 1 : s[3].size() > 0 ? 3 : 5;
            int supId = mixedId == 1 ? 4 : mixedId == 3 ? 0 : 2;
            
            if (s[supId].size() == 0) {
                int rem = 0;
                for (int i = 0; i < 6; i++) {
                    rem += s[i].size();
                }
                
                if (rem == 1) {
                    cout << s[mixedId].back() << endl;
                    return;
                }
            } else if (s[supId].size() == 1) {
                int rem = 0;
                for (int i = 0; i < 6; i++) {
                    rem += s[i].size();
                }
                
                if (rem == 2) {
                    cout << s[mixedId].back() << s[supId].back() << endl;
                    return;
                }
            } else {
                throw;
            }
        }
        puts("IMPOSSIBLE");
        return;
    }
    
    vector<int> order;
    for (int i = 0; i < 6; i++) {
        order.push_back(i);
    }
    
    sort(order.begin(), order.end(), [](int i, int j) -> bool {
        return s[i].size() > s[j].size();
    });
    
    for (int i = 3; i < 6; i++) {
        if (s[order[i]].size() != 0) {
            throw;
        }
    }
    
    const int x = order[0];
    const int y = order[1];
    const int z = order[2];
    
    if (s[x].size() > s[y].size() + s[z].size()) {
        puts("IMPOSSIBLE");
        return;
    }
    
    vector<string> ans;
    while (!s[x].empty()) {
        ans.push_back(s[x].back());
        s[x].pop_back();
        
        if (s[y].size() > 0) {
            ans.push_back(s[y].back());
            s[y].pop_back();
        } else if (s[z].size() > 0) {
            ans.push_back(s[z].back());
            s[z].pop_back();
        } else {
            throw;
        }
    }
    
    if (s[y].size() > 0) {
        throw;
    }
    
    string result;
    for (int i = 0; i < ans.size(); i++) {
        result += ans[i];
        if (s[z].size() > 0) {
            result += s[z].back();
            s[z].pop_back();
        }
    }
    if (result[0] == result.back()) {
        puts("IMPOSSIBLE");
        return;
    }
    
    cout << result << endl;
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
