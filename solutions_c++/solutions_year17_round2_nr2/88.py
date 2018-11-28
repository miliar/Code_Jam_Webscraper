#include <cstdio>
#include <algorithm>

using namespace std;

int A[10];
string ans;

bool Work(pair<int, char> a, pair<int, char> b, pair<int, char> c)
{
    string res; ans.clear();
    if(b.first > a.first) swap(a, b);
    if(c.first > a.first) swap(a, c);
    int i, j = b.first, k = a.first - c.first;
    for(i = 1; i <= a.first; ++i){
        res += a.second;
        if(i <= j) res += b.second;
        if(i > k) res += c.second;
    }
    j = res.size();
    for(i = 1; i < j; ++i){
        if(res[i] == res[i - 1])
            return false;
    }
    if(j > 1 && res[j - 1] == res[0]) return false;
    for(i = 0; i < j; ++i){
        for(;res[i] == 'R' && A[4]; --A[4]){
            ans += 'R';
            ans += 'G';
        }
        for(;res[i] == 'Y' && A[6]; --A[6]){
            ans += 'Y';
            ans += 'V';
        }
        for(;res[i] == 'B' && A[2]; --A[2]){
            ans += 'B';
            ans += 'O';
        }
        ans += res[i];
    }
    for(;A[4]; --A[4]){
        if(A[0] > 1) ans += 'R';
        ans += 'G';
    }
    for(;A[6]; --A[6]){
        if(A[0] > 1) ans += 'Y';
        ans += 'V';
    }
    for(;A[2]; --A[2]){
        if(A[0] > 1) ans += 'B';
        ans += 'O';
    }
    j = ans.size();
    for(i = 1; i < j; ++i){
        if(ans[i] == ans[i - 1])
            return false;
    }
    if(j > 1 && ans[j - 1] == ans[0]) return false;
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, i, j;
    bool flag;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        flag = true;
        for(i = 0; i <= 6; ++i)
            scanf("%d", A + i);
        if(A[5] < A[2]){
            if(A[2] != 1 || A[2] != A[0]) flag = false;
        }
        else if(A[5] == A[2]){
            if(A[5] + A[2] != A[0] && (A[2] || A[5])) flag = false;
            else A[5] -= A[2];
        }
        else A[5] -= A[2];
        if(A[1] < A[4]){
            if(A[4] != 1 || A[4] != A[0]) flag = false;
        }
        else if(A[1] == A[4]){
            if(A[1] + A[4] != A[0] && (A[1] || A[4])) flag = false;
            else A[1] -= A[4];
        }
        else A[1] -= A[4];
        if(A[3] < A[6]){
            if(A[6] != 1 || A[6] != A[0]) flag = false;
        }
        else if(A[3] == A[6]){
            if(A[3] + A[6] != A[0] && (A[3] || A[6])) flag = false;
            else A[3] -= A[6];
        }
        else A[3] -= A[6];

        if(flag)
            flag &= Work({A[1], 'R'}, {A[3], 'Y'}, {A[5], 'B'});
        if(flag) printf("Case #%d: %s\n", j, ans.c_str());
        else printf("Case #%d: IMPOSSIBLE\n", j);
    }
    return 0;
}
