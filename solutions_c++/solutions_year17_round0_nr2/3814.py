#pragma region includes
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
using namespace std;

#pragma endregion

FILE *in, *out;

#pragma region defines

#define MAX(a,b) a = a>b?a:b;
#define MIN(a,b) a = a<b?a:b;
#define MIN2(a,b) a = (a==-1||b<a)?b:a;
#define MAX2(a,b) a = (a==-1||b>a)?b:a;

#define MIN2D(a,b,f) if(a==-1||b<a){a=b;f}
#define FILL(s,v) memset(s, v, sizeof(s))
#define FOR(i,n) for(int i = 0; i < n;i++)
#define FOR1(i,n) for(int i = 1; i <= n;i++)
#define FORI(i,v,n) for(int i = v; i < n;i++)

#define FORR(i,n) for(int i = (n)-1; i >= 0;i--)
#define FORR1(i,n) for(int i = n; i > 0;i--)
#define FORRI(i,v,n) for(int i = (n)-1-(v); i >= 0;i--)
#define FORIT(i,collection)for (auto i = collection.begin(); i != collection.end(); ++i)
#define FORRIT(i,collection)for (auto i = collection.rbegin(); i != collection.rend(); ++i)
#define ALL(n) n.begin(),n.end()
const double PI = acos(-1.0);

#define wait do {char c; while((c = getchar()) != '\n' && c != EOF);}while(0)
#define read(i) int i; fscanf(in,"%d",&i)
#define readu(i) fscanf(in,"%d",&i)
#define readf(f) double f; fscanf(in,"%lf",&f)
#define readuf(f) fscanf(in,"%lf",&f)
#define readll(i) ll i; fscanf(in,"%lli",&i);
#define readull(i) fscanf(in,"%lli",&i);

#define readv3(v) vec3 v; readuf(v.x);readuf(v.y);readuf(v.z);
#define readuv3(v) readuf(v.x);readuf(v.y);readuf(v.z);

#define readv2(v) vec2 v; readuf(v.x);readuf(v.y);
#define readuv2(v) readuf(v.x);readuf(v.y);

#define dpr(i) printf(#i ": %d\n", i)
#define pr(s, ...)fprintf(out,s,__VA_ARGS__)
#define re(s, ...)fscanf(in,s,__VA_ARGS__)
#define mkp(first,second)make_pair(first,second)
#pragma endregion
#pragma region types

typedef long long ll;
typedef unsigned long long ull;
#define umap unordered_map
#define uset unordered_set
#define umset unordered_multiset
#define mset multiset
typedef pair<int, int> pii;
#pragma endregion
#pragma region helpers

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
ll lcm(ll x, ll y) { return x* (y / gcd(x, y)); };
ll llpow(ll base, ll exponent) { ll ack = 1; FOR(i, exponent) { ack *= base; }return ack; }
int choose(int l, int s) { int t = 1; FORI(i, l - s, l) t *= i + 1; int b = 1; FORI(i, 1, s) b *= i + 1; return t / b; }

template<typename T>
int index(vector<T> vec, T value) { auto it = find(ALL(vec), value); return it == vec.end() ? -1 : it - vec.begin(); }


void bit_print(int p) { FORR(i, 32) printf("%d", (p >> i) & 1); printf("\n"); }
int count_1(int p) { int ack = 0; FOR(i, 32)  ack += (p >> i) & 1; return ack; }
int count_0(int p) { int ack = 0; FOR(i, 32)  ack += (p >> i) & 0; return ack; }
int highest_1(ll num) { FORR(i, 64) { if ((num >> i) & 1) return i; }return -1; }
int highest_0(ll num) { FORR(i, 64) { if (!((num >> i) & 1)) return i; }return -1; }
int lowest_1(ll num) { FOR(i, 64) { if ((num >> i) & 1) return i; }return -1; }
int lowest_0(ll num) { FOR(i, 64) { if (!((num >> i) & 1)) return i; } return -1; }
bool bit(ll num, int i) { return (num >> i) & 1; }
ll set_bit(ll num, int bit, int x) { return num ^= (-x ^ num) & (((ll)1) << bit); }

#define contains(container, value) (find(ALL(vector),value) != vector.end()) //simpler than playing with templates..

#if 0 read_every_x_line_base
char line[10000];
char buffer[10000];
vector<string> readLineW() {
	vector<string> items;
	fgets(line, 10000, in);
	int buffer_off = 0;
	FILL(buffer, 0);
	while (sscanf(line + buffer_off, "%s", &buffer)) {
		int len = strlen(buffer);
		if (!len) break;
		buffer_off += len + 1;
		printf("%s", buffer);
		items.push_back(buffer);
		FILL(buffer, 0);
	}
	return items;
}
#endif 


#pragma endregion
#pragma region lin alg

struct vec3;
vec3 cross(vec3 a, vec3 b);
double dot(vec3 a, vec3 b);

struct vec3 {
	double x;
	double y;
	double z;
	vec3 operator+(const vec3& b) {
		vec3 ret;
		ret.x = this->x + b.x;
		ret.y = this->y + b.y;
		ret.z = this->z + b.z;
		return ret;
	}
	vec3 operator-(const vec3& b) {
		vec3 ret;
		ret.x = this->x - b.x;
		ret.y = this->y - b.y;
		ret.z = this->z - b.z;
		return ret;
	}
	vec3 operator*(const double& b) {
		vec3 ret;
		ret.x = this->x * b;
		ret.y = this->y * b;
		ret.z = this->z * b;
		return ret;
	}
	vec3 operator/(const double& b) {
		vec3 ret;
		ret.x = this->x / b;
		ret.y = this->y / b;
		ret.z = this->z / b;
		return ret;
	}
	bool operator==(const vec3& b) { return x == b.x && y == b.y&& z == b.z; }
	double mag() { return sqrt(x*x + y*y + z*z); }
	vec3 norm() { return *this / this->mag(); }
	vec3 proj(vec3 p) { return p*proj_fac(p); }
	double proj_fac(vec3 p) { return (dot(*this, p) / dot(p, p)); }
	bool isZero() { return (x*x + y*y + z*z) < 0.00000001; }
};

vec3 cross(vec3 a, vec3 b) {
	vec3 ret;
	ret.x = (a.y*b.z) - (a.z*b.y);
	ret.y = (a.z*b.x) - (a.x*b.z);
	ret.z = (a.x*b.y) - (a.y*b.x);
	return ret;
}
struct vec2;
double cross(vec2 a, vec2 b);
double dot(vec2 a, vec2 b);

struct vec2 {
	double x;
	double y;
	vec2 operator+(const vec2& b) {
		vec2 ret;
		ret.x = this->x + b.x;
		ret.y = this->y + b.y;
		return ret;
	}
	vec2 operator-(const vec2& b) {
		vec2 ret;
		ret.x = this->x - b.x;
		ret.y = this->y - b.y;
		return ret;
	}
	vec2 operator*(const double& b) {
		vec2 ret;
		ret.x = this->x * b;
		ret.y = this->y * b;
		return ret;
	}
	vec2 operator/(const double& b) {
		vec2 ret;
		ret.x = this->x / b;
		ret.y = this->y / b;
		return ret;
	}
	double angle() {
		return atan2(y, x);
	}

	bool operator==(const vec2& b) { return x == b.x && y == b.y; }
	double mag() { return sqrt(x*x + y*y); }
	vec2 norm() { return *this / this->mag(); }
	vec2 proj(vec2 p) { return p*proj_fac(p); }
	double proj_fac(vec2 p) { return (dot(*this, p) / dot(p, p)); }
	bool isZero() { return (x*x + y*y) < 0.00000001; }
};

double cross(vec2 a, vec2 b) {
	return (a.x*b.y) - (a.y*b.x);
}

double dot(vec2 a, vec2 b) {
	return a.x*b.x + a.y *b.y;
}

double dot(vec3 a, vec3 b) {
	return a.x*b.x + a.y *b.y + a.z*b.z;
}

double distance(vec3 la, vec3 lb, vec3 p) {
	return cross(p - la, p - lb).mag() / (la - lb).mag();
}

#pragma endregion

#define comp
#define problem "B"
#define small

#define number "0"

#pragma region path

#ifdef small
#ifdef comp
#define  fileName  problem "-small-attempt" number 
#else
#define  fileName  problem "-small-practice" 
#endif

#endif

#ifdef large
#ifdef comp
#define fileName problem "-large"
#else
#define fileName problem "-large-practice"
#endif
#endif

#ifdef test
#define fileName problem "-test"
#endif

#define basePath "C:\\users\\daniel\\downloads\\"
#define in_path basePath fileName ".in"
#define out_path basePath fileName ".out"

#pragma endregion


int cmp(const void *va, const void *vb) {
#define cmp_type pii
	cmp_type a = *(cmp_type *)va;
	cmp_type b = *(cmp_type *)vb;
	return b.first - a.first;
#undef cmp_type
}

int cmp2(const void *va, const void *vb) {
#define cmp_type pii
	cmp_type a = *(cmp_type *)va;
	cmp_type b = *(cmp_type *)vb;
	return a.first - b.first;
#undef cmp_type
}
#define SORT(arr, len) qsort(arr,len,sizeof((arr)[0]),cmp);
#define SORT2(arr, len) qsort(arr,len,sizeof((arr)[0]),cmp2);
#include <chrono>
#include<random>
std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
std::uniform_int_distribution<int> distribution(0, 1);
std::uniform_real_distribution<float> distr(0, 1);






int main() {
	in = fopen(in_path, "r");
	out = fopen(out_path, "w");
	assert(in);
	int T;
	fscanf(in, "%d\n", &T);
	FOR1(test_number, T) {
		dpr(test_number);
		pr("Case #%d: ", test_number);


		char buffer[2000];
		int width;
		fscanf(in, "%[^\n]\n", &buffer, &width);
		int len = strlen(buffer);
		long long int start; sscanf(buffer, "%lld", &start);
		int index = -1;
		FOR(i, len - 1) {
			if (buffer[i] > buffer[i + 1]) {
				for (int j = i + 1; j < len; j++) buffer[j] = '9';
				index = i;
				break;
			}
		}
		if (index != -1)buffer[index] -= 1;
		int index_2 = -1;
		FORR(i, index) {
			if (buffer[i] > buffer[i + 1]) {
				buffer[i] -= 1;
				index_2 = i;
			}
		}
		if (start == 665) {
			int q = 0;
		}

		if (index_2 != -1) {
			for (int i = index_2+1; i < index+1; i++)buffer[i] = '9';
		}

		if (buffer[0] == '0') {
			FOR(i, index + 1) buffer[i] = '9';
		}
		long long int current;
		//pr("%lld -> ", start);
		sscanf(buffer, "%lld", &current);
		
		if (current > start) {
			pr("%s", buffer + 1);
			//sscanf(buffer + 1, "%lld", &current);
		} else {
			pr("%s", buffer);
			//sscanf(buffer, "%lld", &current);
		}
		/*
		sprintf(buffer, "%lld", start);
		//brute force
		for (;;) {
			long long int val;
			len = strlen(buffer);
			FOR(i, len - 1) {
				if (buffer[i] > buffer[i + 1]) goto cont;
			}
			sscanf(buffer, "%lld", &val);
			if (val != current) {
				pr("### should be %lld", val);
			}
			break;
		cont:
			sscanf(buffer, "%lld", &val);
			--val;
			sprintf(buffer, "%lld", val);
		}
		*/

		pr("\n");

	}
	return 0;
}











