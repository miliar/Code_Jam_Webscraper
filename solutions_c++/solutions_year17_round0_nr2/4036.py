#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#define REP(i, n) for(int i = 0; i < n; ++i)
#define RANGE(i, x, n) for(int i = x; i < n; ++i)
using namespace std;

typedef long long ll;

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    RANGE(k, 1, T+1) {
        ll N;
        cin >> N;
        ll a, b;
        string sa, sb, sn;
        sn = to_string(N);
        int pos = 0;
        sa.assign(sn.size(), sn[0]);
        sb.assign(sn.size(), '9');
        sb[0] = sn[0];
        while(pos < sn.size()) {
            a = stoll(sa);
            b = stoll(sb);
            if(a <= N && N <= b) {
                ++pos;
            }else if(b < N){
                sn = sb;
                break;
            }else {
                --sn[pos];
            }
            REP(i, pos + 1) {
                sa[i] = sb[i] = sn[i];
            }
            RANGE(i, pos + 1, sn.size()) {
                sa[i] = sn[pos];
                sb[i] = '9';
            }
        }
        cout << "Case #" << k << ": " << stoll(sn) << endl;
    }
}
