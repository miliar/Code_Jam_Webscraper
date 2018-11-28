#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
typedef long long LL;
const double PI = acos(-1);

int n, m, T;
struct Node
{
    int s, t, id;
} p[1002];

bool cmp(Node a, Node b)
{
    return a.s < b.s;
}
bool mycmp(int a, int b)
{
    return a>b;
}

vector<int> v_a, v_b;
int main()
{
    
    freopen("/Users/RUSH_D_CAT/Desktop/in.txt", "r", stdin);
    freopen("/Users/RUSH_D_CAT/Desktop/out.txt", "w", stdout);
    
    cin >> T;
    int cas = 0;
    while(T--)
    {
        v_a.clear();
        v_b.clear();

        scanf("%d %d", &n, &m);
        for(int i=1;i<=n;i++)
        {
            scanf("%d %d", &p[i].s, &p[i].t);
            p[i].id = 1;
        }

        for(int i=n+1;i<=n+m;i++)
        {
            scanf("%d %d", &p[i].s, &p[i].t);
            p[i].id = 2;
        }
        sort(p+1, p+m+n+1, cmp);
        int sum = 0, ans = 0;
        int time_a = 0, time_b = 0;
        int add_a = 0, add_b = 0;

        p[m+n+1].t = p[1].t + 1440;
        p[m+n+1].s = p[1].s + 1440;
        p[m+n+1].id = p[1].id;
        for(int i=1;i<=m+n;i++)
        {
            if(p[i].id == 1) time_b += p[i].t - p[i].s;
            if(p[i].id == 2) time_a += p[i].t - p[i].s;
        }

        for(int i=2;i<=m+n+1;i++)
        {
            if(p[i].id != p[i-1].id)
            {
                sum += p[i].s - p[i-1].t;
                ans ++; 
            } else {
                if(p[i].id == 1)
                {
                    add_b += p[i].s - p[i-1].t;
                    v_b.push_back(p[i].s - p[i-1].t);
                } else {
                    add_a += p[i].s - p[i-1].t;
                    v_a.push_back(p[i].s - p[i-1].t);
                }
            }
        }
  
        sort(v_a.begin(), v_a.end(), mycmp); int cnt_a = 0;
        sort(v_b.begin(), v_b.end(), mycmp); int cnt_b = 0;


        while(add_a + time_a > 720)
        {
            add_a -= v_a[cnt_a];
            ans += 2;
        }

        while(add_b + time_b > 720)
        {
            add_b -= v_b[cnt_b];
            ans += 2;
        }

        printf("Case #%d: %d\n", ++cas, ans);

    }
}











