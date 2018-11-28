#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    long long int n, temp;
    cin >> t;
    for(int z = 1; z <= t; z++) {
        cin >> n;
        temp = n;
        vector <int> v;
        while(temp > 0) {
            v.push_back(temp % 10);
            temp /= 10;
        }
        reverse(v.begin(), v.end());
        int start = 0, i = 0;
        bool inverse = false;
        for(i = 0; i < v.size()-1; i++) {
            if(v[i] > v[i+1]) {
                inverse = true;
                start = i;
                break;
            }
        }
        if(!inverse) {
            cout << "Case #" << z << ": " << n << endl;
            continue;
        }
        for(int j = i-1; j >= 0; j--) {
            if(v[j] == v[i])
                start = j;
        }
        v[start] -= 1;
        for(i = start + 1; i < v.size(); i++)
            v[i] = 9;
        long long int ans = 0;
        for(int i = 0; i < v.size(); i++) {
            ans *= 10;
            ans += v[i];
        }
        cout << "Case #" << z << ": " << ans << endl;
    }
    return 0;
}