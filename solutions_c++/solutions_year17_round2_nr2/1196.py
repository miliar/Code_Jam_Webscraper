#include <bits/stdc++.h>
using namespace std;

struct stall
{
    char col;
    int next;
    int pred;
};

stall otv[2000];
int k[2000], t, sz;

int main()
{
    //("B-small-attempt2.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        int n;
        cin >> n;
        //cout << n << ' ';
        cin >> k['R'] >> k['o'] >> k['Y'] >> k['g'] >> k['B'] >> k['v'] ;
        if(k['R'] > 0)
        {
            for(int i = 0; i < k['R']; ++i)
            {
                otv[i].col = 'R';
                otv[i].pred = (i+k['R']-1)%k['R'];
                otv[i].next = (i+1)%k['R'];
            }
            sz = k['R'] - 1;
            k['R'] = 0;
        }
        else
        {
            if(k['Y'] > 0)
            {
                for(int i = 0; i < k['Y']; ++i)
                {
                    otv[i].col = 'Y';
                    otv[i].pred = (i+k['Y']-1)%k['Y'];
                    otv[i].next = (i+1)%k['Y'];
                }
                sz = k['Y'] - 1;
                k['Y'] = 0;
            }
            else
            {
                if(k['B'] > 0)
                {
                    for(int i = 0; i < k['B']; ++i)
                    {
                        otv[i].col = 'B';
                        otv[i].pred = (i+k['B']-1)%k['B'];
                        otv[i].next = (i+1)%k['B'];
                    }
                    sz = k['B'] - 1;
                    k['B'] = 0;
                }
            }
        }
        bool ans = true;
        while(k['B'] > 0 || k['Y'] > 0)
        {
            bool flag = false;
            if(k['B'] > 0)
            {
                int v = 0;
                while(true)
                {
                    if(otv[v].col != 'B' && otv[otv[v].next].col != 'B' && otv[v].col == otv[otv[v].next].col)
                    {
                        sz++;
                        otv[sz].col = 'B';
                        otv[sz].next = otv[v].next;
                        otv[sz].pred = v;

                        otv[v].next = sz;
                        otv[otv[sz].next].pred = sz;
                        k['B']--;
                        //cout << "1b\n" << endl;
                        flag = true;
                        break;
                    }
                    v = otv[v].next;
                    if(v == 0) break;
                }
            }
            if(flag == true) continue;
            if(k['Y'] > 0)
            {
                int v = 0;
                while(true)
                {
                    if(otv[v].col != 'Y' && otv[otv[v].next].col != 'Y'  && otv[v].col == otv[otv[v].next].col)
                    {
                        sz++;
                        otv[sz].col = 'Y';
                        otv[sz].next = otv[v].next;
                        otv[sz].pred = v;

                        otv[v].next = sz;
                        otv[otv[sz].next].pred = sz;
                        k['Y']--;
                        flag = true;
                        //cout << "1y\n";
                        break;
                    }
                    v = otv[v].next;
                    if(v == 0) break;
                }
            }
            if(flag == true) continue;
            if(k['B'] > 0)
            {
                int v = 0;
                while(true)
                {
                    if(otv[v].col != 'B' && otv[otv[v].next].col != 'B')
                    {
                        sz++;
                        otv[sz].col = 'B';
                        otv[sz].next = otv[v].next;
                        otv[sz].pred = v;

                        otv[v].next = sz;
                        otv[otv[sz].next].pred = sz;
                        k['B']--;
                        //cout << "2b\n";
                        flag = true;
                        break;
                    }
                    v = otv[v].next;
                    if(v == 0) break;
                }
            }
            if(k['Y'] > 0)
            {
                int v = 0;
                while(true)
                {
                    if(otv[v].col != 'Y' && otv[otv[v].next].col != 'Y')
                    {
                        sz++;
                        otv[sz].col = 'Y';
                        otv[sz].next = otv[v].next;
                        otv[sz].pred = v;

                        otv[v].next = sz;
                        otv[otv[sz].next].pred = sz;
                        k['Y']--;
                        flag = true;
                        //cout << "2y\n";
                        break;
                    }
                    v = otv[v].next;
                    if(v == 0) break;
                }
            }
            if(!flag)
            {
                ans = false;
                break;
            }
        }
        cout << "Case #" << q+1 << ": ";
        if(ans == false)
            cout << "IMPOSSIBLE\n";
        else
        {
            vector<char > answer;
            int vv = 0;
            while(true)
            {
                answer.push_back(otv[vv].col);
                vv = otv[vv].next;
                if(otv[vv].col == answer[answer.size()-1]) ans = false;
                if(vv == 0) break;
            }
            if(ans == false)
                cout << "IMPOSSIBLE";
            else
            {
                for(int i = 0; i < answer.size(); ++i)
                    cout << answer[i];
            }
            cout << "\n";
            answer.clear();
        }
    }
}
