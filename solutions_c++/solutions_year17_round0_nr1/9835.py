#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
using namespace std;
const int N = 15;
const int M = 10000100;
const long long MOD = 495;
const double PI = acos(-1.0);
const double eps = 1e-10;
const int MAX_VAL = 800*1000;
string s, v;
unordered_set<string> st;
pair<string,int> q[M];
int k, fnt, rear;

bool isfliped(string s){
    for (int i = 0; i < s.size(); ++ i) {
        if (s[i] == '-') {
            return false;
        }
    }
    return true;
}

int main(){
    freopen("/Users/ybc/Project/CCPP/ACM/A-small-attempt0.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/output.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        fnt = rear = 0;
        st.clear();
        cin>>s>>k;
        q[rear ++] = make_pair(s, 0);
        st.insert(s);
        int ans = -1;
        
        while (fnt < rear) {
            pair<string, int> u = q[fnt ++];
            v = u.first;
            if (isfliped(v)) {
                ans = u.second;
                break;
            }
            int j = 0;
            for (int i = -1; j < v.size(); ++ j) {
                if (v[j] == '-') {
                    v[j] = '+';
                } else {
                    v[j] = '-';
                }
                if(j == k - 1){
                    if (st.find(v) == st.end()) {
                        st.insert(v);
                        q[rear ++] = make_pair(v, u.second + 1);
                    }
                }
                if (j >= k)  {
                    ++ i;
                    if (v[i] == '-') {
                        v[i] = '+';
                    } else {
                        v[i] = '-';
                    }
                    if (st.find(v) == st.end()) {
                        st.insert(v);
                        q[rear ++] = make_pair(v, u.second + 1);
                    }
                }
            }
        }
        
        printf("Case #%d: ",cas);
        if (ans == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n",ans);
        }
    }
    return 0;
}

/*
struct flower{
    int l, r, cnt;
};
map<int,flower> fvec;
int dp[N][2];
int n, arr[N];

void init(){
    
}

int main(){
    scanf("%d",&n);
    for (int i = 0; i < n; ++ i)
        scanf("%d",&arr[i]);
    init();
    return 0;
}
*/