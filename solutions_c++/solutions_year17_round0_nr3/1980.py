#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    cin >> t;
    for(int I = 1; I <= t; I++){
        long long n,k;
        cin >> n >> k;
        /*cin >> n >> k;
        long long x,y;
        long long z = n/k-1;
        x = (z+1)/2;
        y = z/2;

        printf("Case #%d: ", I);
        cout << x << " " << y << "\n";
        */
        map<pair<long long, long long>, long long>mp;
        map<pair<long long, long long>, long long>:: reverse_iterator it;
        mp[{n,n}] = 1;
        k++;
        bool f = false;
        while(k > 0){
            it = mp.rbegin();
            long long x = it->second;
            pair<long long, long long>p = it->first;
            mp.erase(--it.base());
            k -= x;
            if(k <= 0 || p.first == 0) {
                printf("Case #%d: ", I);
                cout << p.first << " " << p.second << "\n";
                break;
            }
            if(!f) {
                f = true;
                if((p.first&1) == 0){
                    mp[{p.first>>1, (p.first>>1)-1}] = 1;
                } else{
                    mp[{p.first>>1, (p.first>>1)}] = 1;
                }
            } else{
                if(p.first == p.second){
                    long long a = p.first>>1;
                    long long b = p.first-a-1;
                    mp[{a, b}] += x+x;
                } else{
                    if(p.first&1){
                        mp[{p.first>>1, p.first>>1}] += x;
                        mp[{p.first>>1, (p.first>>1)-1}] += x;
                    } else{
                        mp[{p.first>>1, p.second>>1}] += x;
                        mp[{(p.first>>1)-1, p.second>>1}] += x;
                    }
                }
            }
        }
        mp.clear();
    }
    return 0;
}

