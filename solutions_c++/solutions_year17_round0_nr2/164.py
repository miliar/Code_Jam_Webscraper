#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef __int128 LL;

const double EPS = 1e-8;
const double PI = acos(-1);

double sq(double x){ return x*x; }
ll sq(ll x){ return x*x; }
LL sq(LL x){ return x*x; }
int sign(ll x){ return x < 0? -1 : x > 0? 1 : 0; }

pii operator+(const pii &l, const pii &r){
	return pii(l.first + r.first, l.second + r.second);
}
pii operator-(const pii &l, const pii &r){
	return pii(l.first - r.first, l.second - r.second);
}
ll operator^(const pii &l, const pii &r){
	return (ll)l.first * r.second - (ll)l.second * r.first;
}
ll operator*(const pii &l, const pii &r){
	return (ll)l.first * r.first + (ll)l.second * r.second;
}

pdd operator+(const pdd &l, const pdd &r){
	return pdd(l.first + r.first, l.second + r.second);
}
pdd operator-(const pdd &l, const pdd &r){
	return pdd(l.first - r.first, l.second - r.second);
}
double operator^(const pdd &l, const pdd &r){
	return l.first * r.second - l.second * r.first;
}
double operator*(const pdd &l, const pdd &r){
	return l.first * r.first + l.second * r.second;
}
pdd operator*(const pdd &l, const double &r){
	return pdd(l.first * r, l.second * r);
}
pdd operator-(const pdd &l){
	return pdd(-l.first, -l.second);
}
double size(pdd x){ return hypot(x.first, x.second); }
double size2(pdd x){ return sq(x.first) + sq(x.second); }
ll size2(pii x){ return sq((ll)x.first) + sq((ll)x.second); }
double polar(pdd x){ return atan2(x.second, x.first); }
pdd unit(double a){ return pdd(cos(a), sin(a)); }
pdd norm(pdd a){ return a * (1.0 / size(a)); }
pdd rotate(pdd v, double a){ return unit(a) * v.first + unit(a + PI / 2) * v.second; }

void normalize(double &a){
	while (a < 0) a += 2 * PI;
	while (a >= 2 * PI) a -= 2 * PI;
}

struct circle{
	pdd O;
	double r;
};

int tangent(circle &A, circle &B, pdd des[4]){
	// outer
	int top = 0;
	double d = size(A.O - B.O), a = polar(B.O - A.O), b = PI + a;

	double t = sq(d) - sq(A.r - B.r);
	if (t >= 0){
		t = sqrt(t);
		double p = atan2(B.r - A.r, t);
		des[top++] = pdd(a + p + PI / 2, b + p - PI / 2);
		des[top++] = pdd(a - p - PI / 2, b - p + PI / 2);
	}
	// inner
	t = sq(d) - sq(A.r + B.r);
	if (t >= 0){
		t = sqrt(t);
		double p = atan2(B.r + A.r, t);
		des[top++] = pdd(a + p - PI / 2, b + p - PI / 2);
		des[top++] = pdd(a - p + PI / 2, b - p + PI / 2);
	}
	return top;
}

int intersect(circle &A, circle &B, pdd des[2]){
	double d = size(A.O - B.O), t = (sq(A.r) + sq(d) - sq(B.r)) / 2 / A.r / d, u = (sq(B.r) + sq(d) - sq(A.r)) / 2 / B.r / d;
	if (abs(d) < EPS) return 0;
	if (1 - t*t < 0 || 1 - u*u < 0) return 0;
	double a = atan2(sqrt(1 - t*t), t), b = atan2(sqrt(1 - u*u), u), p = polar(B.O - A.O), q = PI + p;
	des[0] = pdd(p + a, q - b);
	des[1] = pdd(p - a, q + b);
	return 2;
}

int intersect(circle &A, pdd &s, pdd &d, pdd des[2]){
	double c = size2(A.O - s) - sq(A.r), b = d * (s - A.O), a = size2(d);

	if (b*b - a*c < 0) return 0;
	des[0].second = (-b + sqrt(b*b - a*c)) / a;
	des[1].second = (-b - sqrt(b*b - a*c)) / a;
	des[0].first = polar(s + d*des[0].second - A.O);
	des[1].first = polar(s + d*des[1].second - A.O);
	return 2;
}

int intersect(pdd a, pdd b, pdd u, pdd v, pdd &des){
	if (abs(b^v) < EPS) return 0;
	des = pdd(((a - u) ^ v) / (v^b), ((a - u) ^ b) / (v^b));
	return 1;
}

double dist(const pdd &A, const pdd &p, const pdd &d){
	if( size(A-p) <= EPS ) return 0;
	else if( size(d) <= EPS ) return size(A-p);
	double sina = ((A-p) ^ d) / size(A-p) / size(d);
	double cosa = ((A-p) * d) / size(A-p) / size(d);
	double r = abs(size(A - p) * sina), e = size(A - p) * cosa;
	if (0 < e && e < size(d));
	else r = min(size(A - p), size(A - p - d));
	return r;
}

struct V3{
	double x, y, z;
	V3(){}
	V3(double x, double y, double z) :x(x), y(y), z(z){}

	V3 operator-()const{ return V3(-x, -y, -z); }
	V3 operator-(const V3 &l)const{
		return V3(x - l.x, y - l.y, z - l.z);
	}
	V3 operator+(const V3 &l)const{
		return V3(x + l.x, y + l.y, z + l.z);
	}
	V3 operator*(const double c)const{
		return V3(x*c, y*c, z*c);
	}
	double operator*(const V3 &l)const{
		return x*l.x + y*l.y + z*l.z;
	}
	V3 operator^(const V3 &l)const{
		return V3(y*l.z - z*l.y, z*l.x - x*l.z, x*l.y - y*l.x);
	}
	double size(){ return sqrt(sq(x) + sq(y) + sq(z)); }
	double size2(){ return sq(x) + sq(y) + sq(z); }
	V3 norm(){
		double p = size();
		return V3(x / p, y / p, z / p);
	}
	void print(){ printf("%lf %lf %lf\n", x, y, z); }

	bool operator < (const V3 &l) const {
		if (abs(x - l.x) >= EPS) return x < l.x;
		if (abs(y - l.y) >= EPS) return y < l.y;
		if (abs(z - l.z) >= EPS) return z < l.z;
		return false;
	}
	bool operator == (const V3 &l) const {
		return abs(x - l.x) < EPS && abs(y - l.y) < EPS && abs(z - l.z) < EPS;
	}
};

struct Quad{
	double a;
	V3 v;
	Quad(double a, V3 v) :a(a), v(v){}
	Quad operator * (const double &c)const{
		return Quad(a * c, v * c);
	}
	Quad operator~() const {
		return Quad(-a, -v);
	}
	Quad operator-() const {
		return Quad(a, -v) * (1 / (sq(a) + sq(v.x) + sq(v.y) + sq(v.z)));
	}
	Quad operator * (const Quad &l)const{
		return Quad(a*l.a - v*l.v, l.v*a + v*l.a + (v^l.v));
	}
	V3 apply(V3 p){
		return ((*this) * Quad(0, p) * -(*this)).v;
	}
};

Quad set_rotate(V3 axis, double a){
	return Quad(cos(a / 2), axis.norm() * sin(a / 2));
}

struct sphere{
	V3 O;
	double r;
};

int intersect(sphere A, V3 s, V3 d, double des[2]){
	double c = (A.O - s).size2() - sq(A.r), b = d * (s - A.O), a = d.size2();

	if (b*b - a*c < 0) return 0;
	des[0] = (-b + sqrt(b*b - a*c)) / a;
	des[1] = (-b - sqrt(b*b - a*c)) / a;
	return 2;
}

bool isintersect(pdd &a, pdd &b, pdd &u, pdd &v){
	if( (((u-a)^(b-a)) < 0) ^ (((v-a)^(b-a)) < 0) );
	else return false;
	if( (((a-u)^(v-u)) < 0) ^ (((b-u)^(v-u)) < 0) ) return true;
	else return false;
}

// == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == // == //

#include<string>
#include<iostream>

char buf[1005];

void solve()
{
	/*
	ll N;
	scanf("%lld", &N);
	for(ll i = N; i >= 0; i--){
		ll c = i, d = 10, e = 1;
		while(c){
			if( c%10 <= d ) d = c%10;
			else e = 0;
			c /= 10;
		}
		if( e ){
			printf("%lld\n", i);
			break;
		}
	}
	/*/
	string D, E;
	cin >> D;
	E = D;
	for(int i = 1; i < E.size(); i++){
		if( E[i-1] > E[i] ){
			for(int j = i-1; j >= 0; j--){
				if( j && E[j-1] == E[i-1] );
				else{
					E[j]--;
					for(int k = j+1; k < E.size(); k++) E[k] = '9';
					break;
				}
			}
			break;
		}
	}
	if( E[0] == '0' ) for(int i = 1; i < E.size(); i++) printf("9");
	else printf("%s", E.c_str());
	printf("\n");// */
}

int main()
{
	int TT;
	scanf("%d", &TT);
	for(int tt = 1; tt <= TT; tt++){
		printf("Case #%d: ", tt);
		solve();
	}
}
