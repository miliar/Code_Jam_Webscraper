#include<cstdio>
#include<iostream>
#include<cstring>
#include<map>
using namespace std;
typedef long long ll;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t;
    ll n, k;
    ll divide[2];
    map<ll, ll> mmap;
    map<ll, ll>::iterator it;
    cin >> t;
    for(int i=1; i<=t; i++)
    {
        cin >> n >> k;
        mmap.clear();
        mmap[n] = 1;
        while(!mmap.empty())
        {
            it = mmap.end();
            it--;
            ll key = it->first;
            ll value = it->second;
            //cout << key << endl;
            if(value >= k)
            {
                cout << "Case #" << i << ": " << key/2 << " " << (key-1)/2 << endl;
                break;
            }
            k -= value;
            divide[0] = (key)/2;
            divide[1] = (key-1)/2;
            for(int j=0; j<2; j++)
            {
                if(divide[j] > 0)
                {
                    if(mmap.find(divide[j]) != mmap.end())
                        mmap[divide[j]] += mmap[key];
                    else
                        mmap[divide[j]] = mmap[key];
                }
            }
            mmap.erase(it);
        }
    }
    return 0;
}
