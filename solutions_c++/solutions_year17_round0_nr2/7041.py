#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

long long t, T, n;
vector<int> v;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for (int t = 1; t <= T; ++t)
    {
        cin>>n;
        v.clear();
        while (n != 0)
        {
            v.push_back(n % 10);
            n /= 10;
        }
        for (int i = 0; i < (int)v.size() - 1; ++i)
        {
            if(v[i] < v[i + 1])
            {
                for(int j = 0; j <= i; ++j)
                    v[j] = 9;
                for(int j = i + 1; j < (int)v.size(); ++j)
                    if (--v[j] < 0) v[j] = 9;
                        else break;
                while(v.back() < 1)
                    v.pop_back();
            }
        }
        cout<<"Case #"<<t<<": ";
        for(int i = (int)v.size() - 1; i >= 0; --i)
            cout<<v[i];
        cout<<"\n";

    }
}
