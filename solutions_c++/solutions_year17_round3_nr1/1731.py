#include <iostream>
#include <queue>

using namespace std;

typedef pair<long long, long long> pll;
# define M_PIl 3.141592653589793238462643383279502884L
#define fi first
#define se second
priority_queue<pll> q;
vector<pll> h;
vector<pll> r;
vector<pll> v;
int main(){
    long long testcase; scanf("%lld", &testcase);
    for(long long i = 1; i <= testcase; i++){
        printf("Case #%lld: ", i);
        r.clear();
        h.clear();
        v.clear();
        long long N; long long K;
        scanf("%lld%lld", &N, &K);
        for(long long j = 1; j <= N; j++){
            long long R, H;
            scanf("%lld%lld", &R, &H);
            r.push_back(pll(R, j));
            long long area = 2*R*H;
            h.push_back(pll(area , j));
            v.push_back(pll(R, H));
        }
        sort(r.rbegin(), r.rend());
        sort(h.rbegin(), h.rend());
        long long ans = 0;
        for(long long j = 0; j < r.size(); j++){
            long long areachoose = 0;
            long long z = K-1;
            long long p1 = r[j].se;
            long long hh = v[p1-1].se;
            long long rr = v[p1-1].fi;
            areachoose += 2*rr*hh;
            long long pos = 0;
            while(z > 0 && pos < N){
                long long p2 = h[pos].se;
                if(p2 == p1) pos++;
                else {
                    long long area = h[pos].fi;
                    areachoose += area;
                    z--; pos++;
                }
            }
            if(z == 0)ans = max(ans, r[j].fi*r[j].fi + areachoose);
        }
        double print = ans;
        print = print*M_PIl;
         cout.setf(ios::showpoint);

        cout.precision(9);        

        cout.setf(ios::fixed);
        cout << print << endl;
    }
}
