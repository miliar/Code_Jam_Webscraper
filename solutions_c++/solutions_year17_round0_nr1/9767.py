#include<bits/stdc++.h>
#define f0(s,d) for(int (s) = 0; (s)<(d); (s)++)
#define f1(s,d) for(int (s) = 1; (s)<(d); (s)++)
#define int long long

using namespace std;

string flip(int ind, int k, string s)
{
    for(int i = ind; i<ind+k; i++)
        if(s[i] == '+') s[i] = '-';
        else s[i] = '+';
    return s;
}

#undef int
int main()
#define int long long
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    cin>>T;
    for(int z = 1; z<=T; z++)
    {
        string s;
        int k;
        map<string, int> d;
        cin>>s>>k;
        string all = s;
        fill(all.begin(), all.end(), '+');
        d[s] = 0;
        queue<string> q;
        q.push(s);
        while(!q.empty())
        {
            string t = q.front();
            if(t == all)
                break;
            q.pop();
            for(int i = 0; i<s.size() - k + 1; i++)
            {
                string tmp = flip(i,k,t);
                if(d.count(tmp) == 0)
                {
                    d[tmp] = d[t] + 1;
                    q.push(tmp);
                }
            }
        }
        if(d.count(all) == 0)
            cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<z<<": "<<d[all]<<endl;
    }
}
