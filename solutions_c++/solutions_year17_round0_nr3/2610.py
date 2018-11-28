#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <map>
#include <vector>
#include <algorithm>
using namespace std;

#define FGETS(s,n,p)		{ s[0] = 0; fgets(s,n,p); }
#define FOR(i,a,b)		for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i,a,b)		for (int i(a), _b(b); i >= _b; --i)
#define REP(i,n)		for (int i(0), _n(n); i < _n; ++i)
#define REPD(i,n)		for (int i((n)-1); i >= 0; --i)
#define FILL(a,c)		memset(a,c,sizeof(a))

#define SQPOS(n,i,j)		POS((n),(n),(i),(j))
#define POS(mx,my,x,y)		((x)*(my)+(y))
#define POS3D(mx,my,mz,x,y,z)	((x)*(my)*(mz)+POS((my),(mz),(y),(z)))
#define INSIDE(i,min,max)	((min)<=(i)&&(i)<(max))
#define REMIN(v,n)		{ if ((n)<(v)) { (v)=(n); } }
#define REMAX(v,n)		{ if ((n)>(v)) { (v)=(n); } }
#define SWAP(a,b)		((a)^=((b)^=((a)^=(b))))

#define MIN(a,b)		((a)<(b)?(a):(b))
#define MAX(a,b)		((a)>(b)?(a):(b))
#define	EPS			1e-11	// 1e-6

#define POW2(n)			(1<<(n))
#define HASBIT(v,bit)		(((v)&POW2(bit))!=0)

typedef unsigned long long	ull;
typedef long long		ll;

template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<class T> T cross(T x0, T y0, T x1, T y1, T x2, T y2)
{ return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0); }

int ccw(double x0, double y0, double x1, double y1, double x2, double y2)
{ double t = cross(x0, y0, x1, y1, x2, y2); return (fabs(t) <= EPS? 0: (t < 0? -1: 1)); }
bool line_intersect(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4)
{ return (	ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) < 0 &&
		ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) < 0); }
int sscanf_ilist(char *s, int n_size, int *n)
{
	int nz = 0, pos = 0, len = 0;
	for (nz = 0; nz < n_size; nz++, pos += len)
	{
		n[nz] = -1; sscanf(s+pos, "%d%n", n+nz, &len);
		if (n[nz] == -1) break;
	}
	return nz;
}

typedef struct {
	ull n;
	ull cnt[2];
} slot;

ull left(ull n)
{
	n--;
	return n / 2 + (n % 2);
}
ull right(ull n)
{
	n--;
	return n / 2;
}

slot slit(slot S)
{
	slot Q;
	Q.n = left(S.n);
	Q.cnt[0] = S.cnt[0];
	Q.cnt[1] = 0;
	Q.cnt[left(S.n) == right(S.n) ? 0 : 1] += S.cnt[0];
	Q.cnt[left(S.n) == left(S.n-1) ? 0 : 1] += S.cnt[1];
	Q.cnt[left(S.n) == right(S.n-1) ? 0 : 1] += S.cnt[1];
//printf("S = %llu -> %llu | %llu : ", S.n, left(S.n), right(S.n));
//printf("Q = %llu -> %llu,  %llu -> %llu\n", Q.n, Q.cnt[0], Q.n-1, Q.cnt[1]);
	return Q;
}

// Main Program (Start Here)
int main(int argc, char *argv[])
{
	char buf[4096];
	FILE *in = stdin;
	int T;

	FGETS(buf, 4096, in);
	sscanf(buf, "%d", &T);
	REP(c,T)
	{
		ull N, K, v;
		slot S;

		FGETS(buf, sizeof(buf), in);
		sscanf(buf, "%llu %llu", &N, &K);
		S.n = N;
		S.cnt[0] = 1;
		S.cnt[1] = 0;

		while (K > S.cnt[0] + S.cnt[1]) {
			K -= S.cnt[0] + S.cnt[1];
			S = slit(S);
		}

		v = K <= S.cnt[0] ? S.n : S.n - 1;
//printf("K = %llu, v = %llu\n", K, v);
		printf("Case #%d: ", c+1);
		printf("%llu %llu\n", left(v), right(v));
	}
	return 0;
}
