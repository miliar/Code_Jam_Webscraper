#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int R[50];

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';
        int ans = 0;
        int n, p, q;
        cin>>n>>p;
        for(int i = 0; i < n; ++i)
            cin>>R[i];
        queue<pii> all[50];
        for(int i = 0; i < n; ++i)
        {
            vector<int> cur;
            for(int j = 0; j < p; ++j)
            {
                cin>>q;
                cur.push_back(q);
            }
            sort(cur.begin(), cur.end());
            for(int q: cur)
            {
                auto temp = pii(q*10/(R[i]*11)+(q*10%(R[i]*11)>0), q*10/(R[i]*9));
                if(temp.first <= temp.second)all[i].push(temp);
            }
        }
        bool done = false;
        while(true)
        {
            int mi = 1e9;
            int ma = 0;
            for(int i = 0; i < n; ++i)
            {
                if(all[i].empty())
                {
                    done = true;
                    break;
                }
                mi = min(all[i].front().second, mi);
                ma = max(all[i].front().first, ma);
            }
            if(done)
                break;
            if(mi >= ma)
            {
                ++ans;
                for(int i = 0; i < n; ++i)
                    all[i].pop();
            }
            else
            {
                for(int i = 0; i < n; ++i)
                    if(all[i].front().second == mi)
                        all[i].pop();
            }
        }
        assert(ans >= 0 && ans <= p);
        cout<<"Case #"<<t<<": "<<ans<<'\n';
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
