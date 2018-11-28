#include <iostream>
#include <vector>
#include <queue>

#include <fstream>

using namespace std;
typedef unsigned long long ULONG;

vector<ULONG> ans(ULONG n, ULONG k){
    priority_queue<ULONG> q;
    q.push(n);
    vector<ULONG> ret;

    for (ULONG i = 0; i < k; i++){
        ULONG n = q.top(); q.pop();

        ULONG lo = 0;
        ULONG hi = n - 1;
        ULONG mid = hi / 2;
        ULONG Ls = mid - lo;
        ULONG Rs = hi - mid;

        if (i == k-1){
            ret.push_back(max(Ls, Rs));
            ret.push_back(min(Ls, Rs));
        }
        else {
            q.push(Ls);
            q.push(Rs);
        }
    }

    return ret;
}

int main(){
    ifstream cin ("C-small-2-attempt0.in");
    ofstream cout ("output-bathroom-medium.txt");

    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        ULONG n, k;
        cin >> n >> k;
        vector<ULONG> answers = ans(n, k);
        cout << "Case #" << (i+1) << ": " << answers[0] << " " << answers[1] << endl;
    }


    return 0;
}
