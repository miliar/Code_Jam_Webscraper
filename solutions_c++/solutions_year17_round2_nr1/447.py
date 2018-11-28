#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

int fu[N];

int fuf(int x) {
	if (fu[x] == x) return x;
	fu[x] = fuf(fu[x]);
	return fu[x];
}

void fuu(int a, int b) {
	fu[fuf(a)] = fuf(b);
}

long double test() {
	int n, d;
	vector<pair<long double, long double> > v;
	scanf("%d%d", &d, &n);
	for (int i = 0; i <= n; i ++) {
		fu[i] = i;
	}
	v.resize(n + 1);
	long double czas = 0;
	for (int i = 0; i < n; i ++) {
		int a, b;
		scanf("%d%d", &a, &b);
		v[i] = make_pair(a, b);
		czas = max(czas, (d - a)/(long double)b);
//	printf("%Lf\n", czas);
	}
	return d / czas;
	
	/*
	
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	for (int i = 0; i < n; i ++) {
		int j = 1;
		while (v[i].y <= v[i+j].y) {
			j ++;
		}
		for (int k = 0; k < j; k ++) {
			v[i + k] = make_pair(-1, -1);
		}
		i += j - 1;
	}
	int m = n;
	for (int i = 0; i < n; i ++) {
		if (v[i].y < 0) {
			m --;
			for (int j = i; j < n - 1; j ++) {
				v[j] = v[j+1];
			}
		}
	}
	v.resize(m);
	n = m;
	v.push_back(make_pair(d, 0));
	vector<int> pre;
	vector<int> nex;
	vecotr<long double> czas;
	for (int i = 0; i <= n; i ++) {
		pre.push_back(i-1);
		nex.push_back(i+1);
		czas.push_back(0);
	}
	set<pair<long double, int> > spotkania;
	for (int i = 0; i < n; i ++) {
		spotkania.insert(make_pair((v[i+1].x - v[i].x)/(long double)(v[i].y - v[i+1].y), i));
	}
	bool zmiana = true;
	while (zmiana) {
		long double t = 1e10;
		int where = -1;
		for (int i = 0; i < v.size() - 1; i ++) {
			long double tt = (v[i+1].x - v[i].x)/(long double)(v[i].y - v[i+1].y);
			if (tt < t) {
				where = i;
				t = tt;
			}
		}
		if (where == -1) break;
		for (int i = 0; i < v.size() - 1; i ++) {
			
		}
	}*/
}

void print_test() {
	printf("%Lf", test());
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		print_test();
		printf("\n");
	}
}
