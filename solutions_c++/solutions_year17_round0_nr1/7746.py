#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int main() {
    int N;
    cin >> N;
    for(int n=1;n<=N;n++) {
        string s;
        int k, d = 0;
        cin >> s >> k;
        for(int i=0;i<=s.size()-k;i++) {
            if(s[i] == '-') {
                d++;
                for(int j=0;j<k;j++) {
                    if(s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                }
            }
        }
        for(int i=0;i<k;i++) if(s[s.size()-1-i] == '-') d = -1;
        printf("Case #%d: ", n);
        if(d != -1) cout << d << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}

