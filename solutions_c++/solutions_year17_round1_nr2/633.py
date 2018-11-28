/* Bismillahir Rahmanir Rahim */

#include <bits/stdc++.h>

#define rep(i, n)	for(int i=0;i<n;i++)
#define repn(i, n)	for(int i=1;i<=n;i++)
#define set(i, n)	memset(i, n, sizeof(i))

#define pb	push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 55;
const int M = 1000005;

int n, q[N][N], r[N], p;
vector<int>cnt[M][N];

long long get_lo(long long a, long long b){
    long long f = a * b;
    long long ret = (long long)(ceil((double(f) / 10.0) * 9.0));
    return ret;
}

long long get_hi(long long a, long long b){
    long long f = a * b;
    long long ret = (long long)(ceil((double(f) / 10.0) * 11.0));
    return ret;
}

void process(){
    repn(i, n){
        sort(q[i]+1, q[i]+1+p);
        for(int cn=1;cn<=1000000;cn++){
            long long lo = get_lo(r[i], cn), hi = get_hi(r[i], cn);
            repn(ptr, p){
                if(q[i][ptr] >= lo && q[i][ptr] <= hi){
                    cnt[cn][i].push_back(ptr);
                }
            }
            reverse(cnt[cn][i].begin(), cnt[cn][i].end());
        }
    }
}

int main(){
    int tc, cas=1;
    scanf("%d", &tc);
    while(tc--){
        rep(i, M) rep(j, N) cnt[i][j].clear();
        scanf("%d %d", &n, &p);
        repn(i, n) scanf("%d", &r[i]);
        repn(i, n) repn(j, p) scanf("%d", &q[i][j]);
        process();
        int ret = 0;;
        repn(i, 1000000){
            int mn = 1000000000;
            repn(j, n){
                mn = min(mn, int(cnt[i][j].size()));
            }

            ret += mn;

            rep(j, mn){
                repn(k, n){
                    int val = cnt[i][k].back();
                    for(int f=i;;f++){
                        if(cnt[f][k].empty()) break;
                        if(cnt[f][k].back() != val) break;
                        cnt[f][k].pop_back();
                    }
                }
            }

        }
        printf("Case #%d: %d\n", cas++, ret);



        cerr << "SOLVED # " << cas-1 << endl;

    }
	return 0;
}

