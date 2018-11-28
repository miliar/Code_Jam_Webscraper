#include <bits/stdc++.h>

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

typedef long long int ll;

const ll LIM = 1e18;

vector < pair < ll, ll > > A;
vector < pair < ll, ll > > ans;

ll gen = 0;
inline void makeAnotherOne() {
    map < ll, ll > Map;
    for(auto const &it: A) {
        ll dis = it.first - 1;
        Map[dis / 2] += it.second;
        Map[dis / 2 + dis % 2] += it.second;
    }

    A.clear();
    for(auto const &it: Map) {
        if(it.first != 0) {
            A.push_back({it.first, it.second});
            gen += it.second;
        }
    }

    for(int i = (int)A.size() - 1; i >= 0; i--) {
        ans.push_back(A[i]);
    }
}

int main() {
    ios::sync_with_stdio(false);

    int t;
    fin >> t;

    int level = 0;
    while(t--) {
        level++;

        ll n, k;
        fin >> n >> k;

        ans.clear();
        A.clear();

        ans.push_back({n, 1});
        A.push_back({n, 1});

        while(!A.empty()) makeAnotherOne();

        ll best = 0;
        for(auto const &it: ans) {
            k -= it.second;

            if(k <= 0) {
                best = it.first;
                break;
            }
        }

        fout << "Case #" << level << ": ";
        ll dis = best - 1;
        fout << dis / 2 + dis % 2 << " " << dis / 2;
        fout << "\n";
    }

    return 0;
}
