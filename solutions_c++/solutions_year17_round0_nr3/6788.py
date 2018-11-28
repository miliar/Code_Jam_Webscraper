#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t,T;
    fin >> t;
    T = t;
    while(t--) {
        ll n,k;
        fin>>n>>k;
        map<ll,ll> heap;
        heap[n] = 1;
        ll occ=0;
        ll rez=0;
        while(!heap.empty()) {
            auto it=heap.rbegin();
            //cout<<it->first<<" "<<it->second<<"\n";
            occ = it->second;
            rez = it->first;
            k -= occ;
            if(k<=0)
                break;
            heap[(rez-1)/2 + ((rez-1)&1)] += occ;
            heap[(rez-1)/2] += occ;
            auto d_it=heap.end();
            d_it--;
            heap.erase(d_it);
        }
        fout<<"Case #"<<T-t<<": "<<(rez-1)/2 + ((rez-1)&1)<<" "<<(rez-1)/2<<"\n";
        cout<<"Case #"<<T-t<<": "<<(rez-1)/2 + ((rez-1)&1)<<" "<<(rez-1)/2<<"\n";
    }

    fin.close();
    fout.close();
    return 0;
}
