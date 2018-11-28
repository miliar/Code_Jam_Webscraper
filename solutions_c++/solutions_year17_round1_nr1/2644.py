#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#define all(a) a.begin(), a.end()

using namespace std;

typedef unsigned long long int UINT64;
typedef map< UINT64, UINT64 > MII;
typedef vector< UINT64 > VI;
typedef set< UINT64 > SI;
typedef vector < char > VC;
typedef vector < VC > VVC;


//#define DEBUG

#ifdef DEBUG
    #define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)
    void DE_MII(MII &m) {
        for (MII::iterator mit = m.begin(); mit != m.end(); ++mit)
            DE(" %llu:%llu", mit->first, mit->second);
        DE("\n");
    }
    void DE_VVC(VVC &v) {
        for (size_t i=0; i < v.size(); ++i) {
            for (size_t j=0; j< v[i].size(); j++) {
                DE("%c", v[i][j]);
            }
            DE("\n");
        }
        DE("\n");
    }
    #define DI for(int i=0;i<indent;i++) DE("  ");
#else
    #define DI
    #define DE(format, ...)
    #define DE_MII(m)
    #define DE_VVC(v)
#endif


void solve()
{
	UINT64 R, C;
    #define BUF_MAX (100)
    char buff[BUF_MAX];
	scanf("%llu %llu", &R, &C);
	DE("R=%llu C=%llu\n", R, C);
    fgets(buff, BUF_MAX, stdin);
    
    VVC m(R);
    for(int i=0;i<R;i++) {
        fgets(buff, BUF_MAX, stdin);
        for(int j=0; j<C; j++) {
            m[i].push_back(buff[j]);
        }
    }
    fprintf(stderr,"Orig:\n");
    for(int i=0;i<R;i++) {
        for(int j=0; j<C; j++) {
            fprintf(stderr, "%c",m[i][j]);
        }
        fprintf(stderr, "\n");
    }
    VVC m_orig = m;
    
    set<char> handled;
	
    for(int i=0;i<R;i++) {
        for(int j=0; j<C; j++) {
            if('?' == m[i][j]) continue;
            char initial = m[i][j];
            if (handled.find(initial) != handled.end()) continue;
            handled.insert(initial);
            
            DE("Initial %c at %d,%d\n", initial, i,j);
            int r;
            for(r=j;r<C;r++) {
                m[i][r] = initial;
                if (C-1 == r || ('?' != m[i][r+1] && initial != m[i][r+1])) {
                    break;
                }
            }
            int l;
            for(l=j;l>=0;l--) {
                m[i][l] = initial;
                if (0 == l || ('?' != m[i][l-1] && initial != m[i][l-1])) {
                    break;
                }
            }
            DE("l=%d, r=%d\n",l,r);
            
            for(int u=i-1;u>=0;u--) {
                bool can_fill = true;
                for(int q = l; q<=r; q++) {
                    if ('?' != m[u][q]) {
                        can_fill = false;
                        break;
                    }
                }
                if (!can_fill) {
                    break;
                }
                for(int q = l; q<=r; q++) {
                    m[u][q] = initial;
                }
            }
            for(int d=i+1;d<R;d++) {
                bool can_fill = true;
                for(int q = l; q<=r; q++) {
                    if ('?' != m[d][q]) {
                        can_fill = false;
                        break;
                    }
                }
                if (!can_fill) {
                    break;
                }
                for(int q = l; q<=r; q++) {
                    m[d][q] = initial;
                }
            }
        }
    }
            
    fprintf(stderr, "result:\n");
    for(int i=0;i<R;i++) {
        for(int j=0; j<C; j++) {
            fprintf(stderr, "%c",m[i][j]);
        }
        fprintf(stderr, "\n");
    }

    printf("\n");
    for(int i=0;i<R;i++) {
        for(int j=0; j<C; j++) {
            printf("%c",m[i][j]);
        }
        printf("\n");
    }
    for (int i=0;i<R;i++) {
        for (int j = 0; j<C; j++) {
            assert('?' != m[i][j]);
            if ('?' != m_orig[i][j]) {
                assert(m[i][j] == m_orig[i][j]);
            }
        }
    }

    for (int i=0;i<R;i++) {
        for (int j = 0; j<C; j++) {
            for (int b=i; b<R;b++) {
                for(int r=j;r<C;r++) {
                    if (m[i][j] != m[b][r]) continue;
                    for(int q=i;q<=b;q++) {
                        for (int w=j;w<=r;w++) {
                            assert(m[i][j] == m[q][w]);
                        }
                    }
                }
            }
        }
    }

}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		fprintf(stderr, "Debug Case #%d\n", i);
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
