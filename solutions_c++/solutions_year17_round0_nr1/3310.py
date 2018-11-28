// Author: Psyho
// Blog: http://psyho.gg/
// Twitter: https://twitter.com/fakepsyho

#include <bits/stdc++.h>
#include <sys/time.h>

using namespace std;

#define INLINE   inline __attribute__ ((always_inline))
#define NOINLINE __attribute__ ((noinline))

#define ALIGNED __attribute__ ((aligned(16)))

#define likely(x)   __builtin_expect(!!(x),1)
#define unlikely(x) __builtin_expect(!!(x),0)

#define SSELOAD(a)     _mm_load_si128((__m128i*)&a)
#define SSESTORE(a, b) _mm_store_si128((__m128i*)&a, b)

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define byte        unsigned char
#define LL          long long
#define ULL         unsigned long long
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII         pair<int, int>
#define PDD         pair<double, double>
#define VI          VC<int>
#define VVI         VC<VI>
#define VVVI        VC<VVI>
#define VPII        VC<PII>
#define VVPII       VC<VPII>
#define VVVPII      VC<VVPII>
#define VD          VC<double>
#define VVD         VC<VD>
#define VVVD        VC<VVD>
#define VPDD        VC<PDD>
#define VVPDD       VC<VPDD>
#define VVVPDD      VC<VVPDD>
#define VS          VC<string>
#define VVS         VC<VS>
#define VVVS        VC<VVS>
#define DB(a)       cerr << #a << ": " << (a) << endl;

template<class A, class B> ostream& operator<<(ostream &os, pair<A,B> &p) {os << "(" << p.X << "," << p.Y << ")"; return os;}
template<class A, class B, class C> ostream& operator<<(ostream &os, tuple<A,B,C> &p) {os << "(" << get<0>(p) << "," << get<1>(p) << "," << get<2>(p) << ")"; return os;}
template<class T> ostream& operator<<(ostream &os, VC<T> &v) {os << "{"; REP(i, v.S) {if (i) os << ", "; os << v[i];} os << "}"; return os;}
template<class T> ostream& operator<<(ostream &os, set<T> &s) {VC<T> vs(ALL(s)); return os << vs;}
template<class A, class B> ostream& operator<<(ostream &os, map<A, B> &m) {VC<pair<A,B>> vs; for (auto &x : m) vs.PB(x); return os << vs;}
template<class T> string i2s(T x) {ostringstream o; if (floor(x) == x) o << (int)x; else o << x; return o.str();}
VS splt(string s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {all.PB(s.substr(p, np - p)); p = np + 1;} all.PB(s.substr(p)); return all;}

double getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

struct RNG {
    unsigned int MT[624];
    int index;
	
	RNG(int seed = 1) {
		init(seed);
	}
    
    void init(int seed = 1) {
        MT[0] = seed;
        FOR(i, 1, 624) MT[i] = (1812433253UL * (MT[i-1] ^ (MT[i-1] >> 30)) + i);
        index = 0;
    }
    
    void generate() {
        const unsigned int MULT[] = {0, 2567483615UL};
        REP(i, 227) {
            unsigned int y = (MT[i] & 0x8000000UL) + (MT[i+1] & 0x7FFFFFFFUL);
            MT[i] = MT[i+397] ^ (y >> 1);
            MT[i] ^= MULT[y&1];
        }
        FOR(i, 227, 623) {
            unsigned int y = (MT[i] & 0x8000000UL) + (MT[i+1] & 0x7FFFFFFFUL);
            MT[i] = MT[i-227] ^ (y >> 1);
            MT[i] ^= MULT[y&1];
        }
        unsigned int y = (MT[623] & 0x8000000UL) + (MT[0] & 0x7FFFFFFFUL);
        MT[623] = MT[623-227] ^ (y >> 1);
        MT[623] ^= MULT[y&1];
    }
    
    unsigned int rand() {
        if (index == 0) {
            generate();
        }
        
        unsigned int y = MT[index];
        y ^= y >> 11;
        y ^= y << 7  & 2636928640UL;
        y ^= y << 15 & 4022730752UL;
        y ^= y >> 18;
        index = index == 623 ? 0 : index + 1;
        return y;
    }
    
    INLINE int next() {
        return rand();
    }
    
    INLINE int next(int x) {
        return rand() % x;
    }
    
    INLINE int next(int a, int b) {
        return a + (rand() % (b - a));
    }
    
    INLINE double nextDouble() {
        return (rand() + 0.5) * (1.0 / 4294967296.0);
    }
};

int main() {
	int tc; cin >> tc;
	FOR(atc, 1, tc+1) {
		string s;
		int len = 0;
		int rv = 0;
		cin >> s >> len;
		bool bad = false;
		REP(i, s.S) {
			if (s[i] == '-') {
				if (i + len > s.S) {
					bad = true;
					break;
				}
				FOR(j, i, i+len) s[j] = s[j] == '-' ? '+' : '-';
				rv++;
			}
		}
		if (bad) {
			printf("Case #%d: IMPOSSIBLE\n", atc);
		} else {
			printf("Case #%d: %d\n", atc, rv);
		}
	}
}