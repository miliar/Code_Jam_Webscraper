#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

char ans[100007];

vector<pair<int, int> > vv;
vector<char> now;
map<int, char> m;

int main ()
{
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("out.txt", "w", stdout);
    int n, r, o, y, g, b, v;
    m[1]='R';
    m[2]='Y';
    m[3]='B';
    int t, cs=0;
    int i, j, k;
    cin >> t;
    while (t--)
    {
        memset(ans, 0, sizeof(ans));
        cs++;
        cin >> n >> r >> o >> y >> g >> b >> v;
        vv.push_back(make_pair(r, 1));
        vv.push_back(make_pair(y, 2));
        vv.push_back(make_pair(b, 3));
        sort(vv.begin(), vv.end());
        if (vv[2].first>vv[0].first+vv[1].first)
        {
            printf("Case #%d: IMPOSSIBLE\n", cs);
            vv.clear();
            now.clear();
            continue;
        }
        else
        {
            for (i=0; i<vv[2].first*3; i+=3)
            {
                ans[i]=m[vv[2].second];
            }
            for (i=0; i<vv[1].first; i++)
            {
                now.push_back(m[vv[1].second]);
            }
            for (i=0; i<vv[0].first; i++)
            {
                now.push_back(m[vv[0].second]);
            }
            int cnt=0;
            for (i=1; i<vv[2].first*3; i+=3)
            {
                if (cnt<now.size())
                {
                     ans[i]=now[cnt];
                     cnt++;
                }
            }
            for (i=2; i<vv[2].first*3; i+=3)
            {
                if (cnt<now.size())
                {
                     ans[i]=now[cnt];
                     cnt++;
                }
            }
            string temp="";
            for (i=0; i<10000; i++)
            {
                if (ans[i]!=0)
                {
                    temp+=ans[i];
                }
            }
            printf("Case #%d: ", cs);
            cout << temp << endl;
            vv.clear();
            now.clear();
        }
    }

    return 0;
}
