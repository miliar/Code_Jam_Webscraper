#include <bits/stdc++.h>

using namespace std;


int main()
{

    freopen("C.in", "r", stdin);
    freopen("C3.out", "w", stdout);

    int t;
    cin>>t;

    long long int N;
    long long int k;

    map<long long int, long long int> mp;
    map<long long int, long long int>::reverse_iterator it;
    long long int current, sol;
    long long int nr;
    for(int i=1; i<=t; i++){
        cin>>N>>k;
        mp.clear();
        mp[N] = 1;
        long long int j = 0;
        while(j <= k){
            it = mp.rbegin();
            current = it->first;
            nr = it->second;
            if(j + nr >= k){
                sol = current;
                break;
            }

            mp.erase(current);
            if(current % 2 == 1){
                current /= 2;
                mp[current]+= 2 * nr;
            } else{
                current /= 2;
                mp[current] += nr;
                mp[current - 1] += nr;
            }

            j+=nr;
        }

        current = sol;

        cout<<"Case #"<<i<<": ";
        if(current % 2 == 1){
            current /= 2;
            cout<<current<<" "<<current;
        } else {
            current /= 2;
            cout<<current<<" "<<current - 1;
        }
        cout<<'\n';

    }

    return 0;
}
