#include<bits/stdc++.h>

using namespace std;

typedef long long ll;


int T;
ll N,K;


int getLevel (ll x) {
    int pw = 0;
    ll num = 1;
    while (num <= x) {
        pw++;
        num <<= 1;
    }
    return pw - 1;
}


int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("Csmall-2-LogN.out", "w", stdout);
    cin >> T;
    for(int kase = 1; kase <= T; kase++) {
        cin >> N >> K;
        if (K == 1) {
             if (N % 2) {
                cout << "Case #" << kase << ": " << N/2 << " " << N/2 << endl;
             } else {
                cout << "Case #" << kase << ": " << N/2 << " " << (N/2) - 1 << endl;
             }
             continue;
        }
        int lvl = getLevel(K);
        //cout << lvl << endl;
        ll nodeIndex = K - (1 << lvl);
        //cout << nodeIndex << endl;
        ll tmpNodeIndex = nodeIndex;
        map<ll,ll> nums;
        nums[N/2]++;
        if (N%2) {
            nums[N/2]++;
        } else {
            nums[(N/2) - 1]++;
        }
        map<ll, ll> tmpNums;
        int tmpLvl = 2;
        while (tmpLvl <= lvl) {
            for(map<ll,ll>::iterator it = nums.begin(); it != nums.end(); it++) {
                if(it->first % 2) {
                    tmpNums[it->first/2] += it->second * 2;
                } else {
                    tmpNums[it->first/2] += it->second;
                    tmpNums[(it->first/2) - 1] += it->second;
                }
            }
            nums = tmpNums;
            tmpNums.clear();
            tmpLvl++;
//            cout << "for level " << tmpLvl << ":" << endl;
//            for(map<ll,ll>::iterator it = nums.begin(); it != nums.end(); it++) {
//                cout << it->first << " -> " << it->second << endl;
//            }
        }
        //cout << tmpLvl << " after done" << endl;
        vector<pair<ll, ll> > prs(2);
        int idx = 1;
        for(map<ll,ll>::iterator it = nums.begin(); it != nums.end(); it++) {
            prs[idx].first = it->first;
            prs[idx].second = it->second;
            idx--;
        }
        ll finalNode;
        if(nodeIndex < prs[0].second) {
            finalNode = prs[0].first;
        } else {
            finalNode = prs[1].first;
        }
        //cout << "finalNode : " << finalNode << endl;
        if (finalNode % 2) {
            cout << "Case #" << kase << ": " << finalNode/2 << " " << finalNode/2 << endl;
        } else {
            cout << "Case #" << kase << ": " << finalNode/2 << " " << (finalNode/2) - 1 << endl;
        }
    }
}
