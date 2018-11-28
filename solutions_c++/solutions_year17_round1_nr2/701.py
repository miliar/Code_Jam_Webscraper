#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
const int N = 2120;

struct Node
{
    int x;
    int y;
    int len;
    Node(int a=0, int b=0, int c=0)
    {
        x = a;
        y = b;
        len = c;
    }
    friend bool operator < (const Node& A, const Node& B)
    {
        if(A.len<B.len) return true;
        if(A.len == B.len && A.x > B.x) return true;
        return false;
    }
};

int f(int k, int key)
{
    int ret = k/key;
    if(ret*key*0.9 - 1e-6<=k && k<=ret*key*1.1 + 1e-6)
    {
        return ret;
    }
    ret += 1;
    if(ret*key*0.9 - 1e-6<=k && k<=ret*key*1.1 + 1e-6)
    {
        return ret;
    }
    return 0;
}

int n, p;
int need[N];


int main(int argc, const char* argv[])
{
    freopen("B-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        vector<int> need(n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &need[i]);
        }
        vector<vector<int> > own(n, vector<int>(m));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                scanf("%d", &own[i][j]);
            }
            sort(own[i].begin(), own[i].end());
        }
        int ans = 0;
        vector<int> h(n, 0);
        int ptr=0;
        while (true)
        {
            int flag = 1;
            for (int i = 0; i < n; i++)
            {
                while (h[i] < m && own[i][h[i]] * 10 < need[i] * ptr * 9) h[i]++;
                if (h[i] == m)
                {
                    flag = -1;
                    break;
                }
                if (own[i][h[i]] * 10 > need[i] * ptr * 11)
                {
                    flag = 0;
                    break;
                }
            }
            if (flag == -1)
            {
                break;
            }
            if (flag == 1)
            {
                ans++;
                for(int i=0; i<n; i++)
                {
                    h[i] += 1;
                }
                ptr--;
            }
            ptr += 1;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
