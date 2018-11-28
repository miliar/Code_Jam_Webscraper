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

int N, Q;
ull E[101], S[101];
ull D[101][101];
ull U[101], V[101];

double ride(int step, ull preE, ull preS)
{
	double max = 1e12, t = 0;
	if (step >= N - 1) return 0.0;
	if (preE >= D[step][step+1]) {
		t = ride(step + 1, preE - D[step][step+1], preS);
		t += (double)D[step][step+1]/preS;
		remin(max, t);
//printf("%d-1: %lf\n", step, t);
	}
	if (E[step] >= D[step][step+1]) {
		t = ride(step + 1, E[step] - D[step][step+1], S[step]);
		t += (double)D[step][step+1]/S[step];
		remin(max, t);
//printf("%d-1: %lf\n", step, t);
	}
	return max;
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
//		int S[1001], Sz, K;
//		char s[1001];
//		int cnt = 0, fail = 0;
//		FGETS(buf, sizeof(buf), in);
		fscanf(in, "%d %d", &N, &Q);
		REP(i, N) {
			fscanf(in, "%llu %llu", E+i, S+i);
//printf("E = %llu, S= %llu\n", E[i], S[i]);
		}
		REP(i, N) {
			REP(j, N) {
				fscanf(in, "%llu", &(D[i][j]));
			}
		}
double res;
		// Multi Casse... FIXME
		REP(zz, Q) {
			fscanf(in, "%llu %llu", U, V);
			res = ride(0, 0, 0);	
		}
		// Code here
//		sscanf(buf, "%s %d", s, &K);

		printf("Case #%d: ", c+1);
		// Result Here
		printf("%.8lf\n", res);
	}
	return 0;
}
