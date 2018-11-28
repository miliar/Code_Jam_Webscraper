#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);

using namespace std;

const double pi = M_PI;
const double E = M_E;
const int N = 1e3+5;
const int M = 1e3;
const int inf = 1e9;
const int md = 1e9+7;

int t,n,k,i;
vector<pair<int,int> > v1;
vector<pair<int,int> > v2;

int main()
{
    fc

    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int it = 0;
    cin>>t;
    while (t--)
    {
        cin>>n>>k;

        ++it;
        cout<<"Case #"<<it<<": ";

        v1.clear();
        v1.pb(mk(n, 1));

        while (true)
        {
            bool can = false;
            for (i = v1.size()-1; i>=0; --i)
            {
                if (k<=v1[i].second)
                {
                    cout<<v1[i].first / 2<<" "<<(v1[i].first - 1) / 2<<"\n";
                    can = true;
                    break;
                }
                else k -= v1[i].second;
            }
            if (can) break;

            v2.clear();
            for (i=0; i<v1.size(); ++i)
            {
                v2.pb(mk(v1[i].first / 2, v1[i].second));
                v2.pb(mk((v1[i].first - 1) / 2, v1[i].second));
            }
            sort(v2.begin(), v2.end());

            v1.clear();
            for (i=0; i<v2.size(); ++i)
            {
                if (v2[i].first != 0)
                {
                    if (v1.size() == 0 || v1[v1.size()-1].first != v2[i].first)
                    {
                        v1.pb(mk(v2[i].first, v2[i].second));
                    } else
                    {
                        v1[v1.size()-1].second += v2[i].second;
                    }
                }
            }
        }
    }
}
