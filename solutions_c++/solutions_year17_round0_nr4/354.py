#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define DBG(x) {cout << #x << ": " << x << endl;}

#define FOR(i,b) for(int (i)=0; (i)<(b); ++(i))
#define FORI(i,a,b) for(int (i)=(a); (i)<(b); ++(i))
#define pb push_back
#define mp make_pair
#define xx first
#define yy second

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define IX(x,y) ((x)+(y)*N)

void print(vi v, int N)
{
    FOR(j,N) {
        FOR(i,N) {
            switch(v[IX(i,j)]) {
              case 0:
                cout << ". ";
                break;
              case 1:
                cout << "+ ";
                break;
              case 2:
                cout << "x ";
                break;
              case 3:
                cout << "o ";
                break;
            }
        }
        cout << endl;
    }
}

int main(int argc, char *argv[])
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;

    
    FOR(cas,T) {
        int N,M;
        cin >> N >> M;

        vi v(N*N);
        vi nxrow(N);
        vi nxcol(N);

        int len = 2*N-1;
        vi fwd(len);
        vi bwd(len);
        
        FOR(j,M) {
            char c;
            int x,y;
            cin >> c >> y >> x;
            --x; --y;

            int val = 0;
            switch (c) {
              case '+':
                  fwd[x+y] += 1;
                  bwd[(x-y+len)%len] += 1;
                  val = 1;
                  break;
              case 'x':
                  nxcol[x]++;
                  nxrow[y]++;
                  val = 2;
                  break;
              case 'o':
                  fwd[x+y] += 1;
                  bwd[(x-y+len)%len] += 1;
                  nxcol[x]++;
                  nxrow[y]++;
                  val = 3;
                  break;
            }
            v[IX(x,y)] = val;
        }

        vi nfwd(len);
        vi nbwd(len);


        FOR(i,N) FOR(j,N) {nfwd[i+j]++;nbwd[(i-j+len)%len]++;}
        
        vector<pii> perm;
        FOR(i,N) FOR(j,N) perm.pb({i,j});
        sort(perm.begin(), perm.end(), 
             [&nfwd,&nbwd,len](pii i, pii j) -> bool{
                 return
                     (nfwd[i.xx+i.yy]+nbwd[(i.xx-i.yy+len)%len])<
                     (nfwd[j.xx+j.yy]+nbwd[(j.xx-j.yy+len)%len]);
             });

        vi oldv = v;

        for (pii p : perm) {
            int x = p.xx;
            int y = p.yy;
            if (fwd[x+y]==0 && bwd[(x-y+len)%len]==0) {
                fwd[x+y]++;
                bwd[(x-y+len)%len]++;
                v[IX(x,y)] |= 1;
            }
        }
        // Place crosses
        FOR(y,N) {
            if (nxrow[y] == 0) {
                FOR(x,N) {
                    if (nxcol[x] == 0) {
                        v[IX(x,y)] |= 2;
                        nxcol[x]++;
                        nxrow[y]++;
                        break;
                    }
                }
            }
        }
        
        // Calc points and changes
        int points = 0;
        int changes = 0;
        FOR(j,N*N) {
            points += !!(v[j]&1) + !!(v[j]&2);
            changes += (v[j] != oldv[j]);
        }

        cout << "Case #" << cas+1 << ": ";
        cout << points << " " << changes << endl;
        
        FOR(y,N) {
            FOR(x,N) {
                char piece = 0;
                if (v[IX(x,y)] > oldv[IX(x,y)]) {
                    switch (v[IX(x,y)]) {
                      case 1:
                          piece = '+';
                          break;
                      case 2:
                          piece = 'x';
                          break;
                      case 3:
                          piece = 'o';
                          break;
                    }
                    cout << piece << " " << y+1 << " " << x+1 << endl;
                }
            }
        }
        //cout << "=== old ===" << endl;
        //print(oldv, N);
        //cout << "=== new ===" << endl;
        //print(v, N);
    }
    
    return 0;
}
