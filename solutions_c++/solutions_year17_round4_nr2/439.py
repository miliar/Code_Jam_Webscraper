#include <bits/stdc++.h>
using namespace std;

int isOk(vector<int> seats, int k){
    vector<int> sobr(seats.size(), 0);
    for (int i = 1; i < seats.size(); i++){
        sobr[i]  = sobr[i-1] + max(0, k-seats[i]);
    }
    int ans = 0, used = 0;
    for (int i = seats.size()-1; i >= 1; i--){
        used = max(0, used-max(0, k-seats[i]));
        if (seats[i] > k){
            if (sobr[i]-used < seats[i]-k) return -1;
            ans += seats[i]-k;
            used += seats[i]-k;
        }
    }
    return ans;
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        int n, c, m;
        cin >> n >> c >> m;
        vector<int> seats(n+1, 0), clients(c+1, 0);
        int rides = 0;
        for (int i = 0; i < m; i++){
            int a, b;
            cin >> a >> b;
            seats[a]++;
            clients[b]++;
            rides = max(rides, clients[b]);
        }

        cout << "Case #" << cases++ << ": ";

        for (int k = rides; k <= m; k++){
            int prom = isOk(seats, k);
            if (prom != -1){
                cout << k << " " << prom << endl;
                break;
            }
        }
    }
    return 0;
}
