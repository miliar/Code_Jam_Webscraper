#include <bits/stdc++.h>
#define PI 3.14159265358979323846264338327950
struct tre{
	int r, h;
	double size;
	void calc(){
		size = PI * r * 2 * h;
	}
}a[1111];
int n, k;
double test(int p){
	std::vector<tre> vec;
	for (int i = p + 1; i <= n; i ++ )
		vec.push_back(a[i]);
	double res = PI * a[p].r * a[p].r + a[p].size;
	std::sort(vec.begin(), vec.end(), [] (tre x, tre y) { return x.size > y.size; });
	for (int i = 0; i < k - 1; i ++ )
		res += vec[i].size;
	return res;
}
void Main(){
	scanf("%d%d", &n, &k);
	for (int i = 1; i <= n; i ++ ){
		scanf("%d%d", &a[i].r, &a[i].h);
		a[i].calc();
	}
	std::sort(a + 1, a + n + 1, [] (tre x, tre y) { return x.r > y.r; });
	double max = 0;
	for (int i = 1; i <= n; i ++ ){
		if (n - i + 1 < k) break;
		double res = test(i);
		if (res > max) max = res;
	}
	printf("%.10f\n", max);
}
int main(){
	freopen("t.out","w",stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("Case #%d: ", i);
		Main();
	}
}
