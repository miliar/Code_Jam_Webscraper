#include <bits/stdc++.h>
#define rep(a,b,c) for(int a = b; a < c; a++)
#define ll long long
#define s second
#define f first
#define pb push_back

using namespace std;

priority_queue<pair<ll,ll> > pq;
//int l[1000], r[1000];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("/afs/ms/u/m/mo08/Downloads/in.in", "r", stdin);
	freopen("/afs/ms/u/m/mo08/Downloads/out.txt", "w", stdout);
	int t, t0; ll k, n;
	bool c;
	long double d = 2;
	cin >> t;
	t0 = t;
	int out;
	while(t-->0) {
        cin >> n >> k;
        int x1, x2;
        int out1, out2;/*
        rep(i, 0, n) {
            l[i] = 10000;
            r[i] = 10000;
        }
        r[n-1] = 1;
        l[0] = 1;
        rep(i, 0, k) {
            out1 = 0;
            out2 = 0;
            rep(j, 1, n) {
                l[j] = min(l[j-1]+1, l[j]);
                r[n-1-j] = min(r[n-j]+1, r[n-1-j]);
            }
            rep(j, 0, n) {
                if(min(l[j], r[j]) > out2 || min(l[j], r[j]) == out2 && max(l[j], r[j]) > out1) {
                    x1 = j;
                    out2 = min(l[j], r[j]);
                    out1 = max(l[j], r[j]);
                }
            }
            r[x1] = 0;
            l[x1] = 0;
        }
        cout << out1-1 << " " << out2-1 << "\t\t";*/
        while(!pq.empty()) pq.pop();
        pq.push({n, 1});
        pair<ll, ll> p;
        while(!pq.empty())
        {
            p = pq.top(); pq.pop();
            while(!pq.empty() && p.f == pq.top().f) {
                p.s += pq.top().s;
                pq.pop();
            }
            k -= p.s;
            if(k <= 0) {
                out2 = floor((p.f-1)/d), out1 = ceil((p.f-1)/d);
                break;
            }
            else {
                if(floor((p.f-1)/d) == ceil((p.f-1)/d)) pq.push({floor((p.f-1)/d), p.s*2});
                else {
                    pq.push({floor((p.f-1)/d), p.s});
                    pq.push({ceil((p.f-1)/d), p.s});
                }
            }
        }
        cout << "Case #" << t0-t << ": ";
        cout << out1 << " " << out2 << endl;
	}
	return 0;
}
