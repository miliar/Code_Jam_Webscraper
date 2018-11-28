#include <bits/stdc++.h>

using namespace std;

const int maxN = 1e3+10;
int test, N;
int A[6], stt[6];
char chr[6] = {'R','O','Y','G','B','V'};
string ans;

bool cmp(int a, int b) { return A[a] > A[b]; }
bool dif(char x)
{
    return x != 'O' && x != 'G' && x != 'V';
}

void solve(int x)
{
    if (ans.empty())
    {
        for (int i=0; i < A[x]; i++) ans.push_back(chr[x]);
        return;
    }
    int w = A[x];
    for (int i=0; i < ans.size() && w; i++)
        if (ans[i] == ans[(i+1)%int(ans.size())]) ans.insert(i+1,1,chr[x]), w--;
    for (int i=0; i < ans.size() && w; i++)
        if (dif(ans[i]) && dif(ans[(i+1)%int(ans.size())]))
        {
            if (ans[i] != ans[(i+1)%int(ans.size())] && ans[i] != chr[x] && ans[(i+1)%int(ans.size())] != chr[x])
                ans.insert(i+1,1,chr[x]), w--;
        }
    for (int i=0; i < ans.size() && w; i++)
        if (ans[i] == chr[x] && dif(ans[(i+1)%int(ans.size())])) ans.insert(i+1,1,chr[x]), w--;
}

bool check()
{
    for (int i=0; i < ans.size(); i++)
        if (ans[i] == ans[(i+1)%int(ans.size())]) return 0;
    return 1;
}

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        printf("Case #%d: ",t);
        cin >> N; ans.clear();
        int cnt = 0;
        for (int i=0; i < 6; i++) cin >> A[i], stt[i] = i, cnt += (A[i] == 0);
        if (cnt == 4)
        {
            bool flag = 0;
            for (int k=0; k < 3; k++)
                if (A[k] && A[k+3])
                {
                    flag = 1;
                    if (A[k] != A[k+3]) puts("IMPOSSIBLE");
                    else
                    {
                        for (int i=0; i < A[k]; i++) cout << chr[k] << chr[k+3];
                        cout << endl;
                    }
                }
            if (flag) continue;
        }
        if ((A[3] && A[0] < A[3]+1) || (A[1] && A[4] < A[1]+1) || (A[5] && A[2] < A[5]+1))
        {
            puts("IMPOSSIBLE");
            continue;
        }
        if (A[3])
        {
            while (A[3])
            {
                ans.push_back(chr[0]);
                ans.push_back(chr[3]);
                A[0]--; A[3]--;
            }
            ans.push_back(chr[0]); A[0]--;
        }
        if (A[1])
        {
            while (A[1])
            {
                ans.push_back(chr[4]);
                ans.push_back(chr[1]);
                A[4]--; A[1]--;
            }
            ans.push_back(chr[4]); A[4]--;
        }
        if (A[5])
        {
            while (A[5])
            {
                ans.push_back(chr[2]);
                ans.push_back(chr[5]);
                A[2]--; A[5]--;
            }
            ans.push_back(chr[2]); A[2]--;
        }
        sort(stt,stt+6,cmp);
        for (int k=0; k < 3; k++) solve(stt[k]);
        if (check()) cout << ans << endl;
        else puts("IMPOSSIBLE");
    }
}
