#include<iostream>
#include<string>
#include<sstream>
#include<map>
#include<hash_map>
#include<queue>
#include<algorithm>
#define max_step 1e3
using namespace std;

int work(string &s,int k);
bool check(string &s);
int main()
{
    int T;
    cin >> T;
    for(int t = 1;t <= T;++t)
    {
        string s;
        int k,ans = 0;
        cin >> s >> k;
        ans = work(s,k);
        cout << "Case #" << t << ": ";
        if(ans >= 0)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}

int work(string &s,int k)
{
    queue< pair<string,int> > q;
    map<string,bool> h;
    int ans = -1,len = s.size();
    q.push(make_pair(s,0));
    h[s] = true;
    while(!q.empty())
    {
        string t = q.front().first;
        int st = q.front().second;
        q.pop();
        //cout << t << "," << st << endl;
        //cin.get();
        if(check(t))
        {
            ans = st;
            break;
        }
        if(st > max_step)
        {
            return -1;
        }
        for(int i = 0;i < len;++i)
        {
            if(t[i] == '-')
            {
                //cout << i << " ";
                string tt = t;
                if(i + k < len)
                {
                    for(int j = 0;j < k;++j)
                    {
                        tt[i + j] = (tt[i + j] == '+') ? '-' : '+';
                    }
                    if(h.find(tt) == h.end())
                    {
                        q.push(make_pair(tt,st + 1));
                        h[tt] = true;
                    }
                }
                if(i >= k - 1)
                {
                    tt = t;
                    for(int j = 0;j < k;++j)
                    {
                        tt[i - j] = (tt[i - j] == '+') ? '-' : '+';
                    }
                    if(h.find(tt) == h.end())
                    {
                        q.push(make_pair(tt,st + 1));
                        h[tt] = true;
                    }
                }
            }
        }
        //cout << endl;
    }
    return ans;
}

bool check(string &s)
{
    for(unsigned int i = 0;i < s.size();++i)
    {
        if(s[i] == '-')
            return false;
    }
    return true;
}
