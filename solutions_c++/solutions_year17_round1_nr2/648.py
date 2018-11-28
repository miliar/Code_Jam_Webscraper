#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int t[55][55];
int pos[55];
int c[55];

int main() {
    int N;
    cin >> N;
    for(int n=1;n<=N;n++) {
        int k, p, v = 0;
        cin >> k >> p;
        memset(pos,0,sizeof(pos));
        for(int i=0;i<k;i++) cin >> c[i];
        for(int i=0;i<k;i++) for(int j=0;j<p;j++) cin >> t[i][j];
        for(int i=0;i<k;i++) sort(t[i],t[i]+p);
        int b = 0;
        while(1) {
            int i, m = 0, M = 1e9;
            for(i=0;i<k;i++) {
                int mm = (10*t[i][pos[i]] + 11*c[i]-1)/(11*c[i]);
                int MM = (10*t[i][pos[i]])/(9*c[i]);
                if(10*MM*c[i] < t[i][pos[i]]*9) MM--;
                if(mm > M) {
                    pos[0]++;
                    if(pos[0] == p) b = 1;
                    break;
                }
                
                m = max(m,mm);
                M = min(M,MM);
                if(M < m) {
                    pos[i]++;
                    if(pos[i] == p) b = 1;
                    break;
                }
            }
            if(i == k) {
                v++;
                for(int i=0;i<k;i++) {
                    pos[i]++;
                    if(pos[i] == p) b = 1;
                }
            }
            if(b) break;
        }
        printf("Case #%d: %d\n", n, v);
    }
    return 0;
}

