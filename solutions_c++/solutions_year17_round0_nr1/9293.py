#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    short t = 0;
    cin >> t;

    short k = 0;
    string buf;

    for (int i=1; i<=t; ++i) {
        cin >> buf;
        cin >> k;

        bool ok = true;
        short num_flips = 0;

        //cout << buf << "\n";
        
        for (int j=0;j<buf.size(); ++j) {
            //cout << "\t" << buf << "\n";
            if (buf[j] == '+')
                continue;

            if (buf.size() - j < k) {
                ok = false;
                break;    
            }

            for (int p=j; p<j+k; ++p) {
                buf[p] = buf[p] == '-' ? '+' : '-'; 
            }
            ++num_flips;                
        }

        cout << "Case #" << i << ": ";
        if (!ok) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << num_flips;
        }
        cout << "\n";
    }
     
    return 0;
} 
