#include <iostream>
#include <set>

using namespace std;

long long n, k;
long long Max, Min;
typedef pair<long long, long long> PLL;
long long p[65], odd[65], even[65];

PLL split(long long x) {
	if (x % 2 == 0)
		return make_pair( x/2, (x-1)/2 );
	else return make_pair( (x-1)/2, (x-1)/2);
}

long long min(long long a, long long b){
	if (a < b) return a; else return b;
}

long long min(long long a, long long b, long long c, long long d){
	return min(min(a,b), min(c,d));
}

long long max(long long a, long long b){
	if (a > b) return a; else return b;
}

long long max(long long a, long long b, long long c, long long d){
	return max(max(a,b), max(c,d));
}


void solve() {
	
	int dep = 0;
	long long sum = 1;
	while (sum < k) {
		dep++;
		sum = sum + p[dep];
	}
	sum = sum - p[dep];

	if (n % 2 == 0) {
		odd[0] = 1; even[0] = 1;
		Max = n/2; Min = (n-1)/2;
	}
	else {
		Max = (n-1) / 2; Min = (n-1) /2;
		if (Max % 2 == 0){
			odd[0] = 0; even[0] = 2;
		}
		else {
			odd[0] = 2; even[0] = 0;
		}
	}

	for (int i = 1; i < dep; i++){
		odd[i] = even[i-1];
		even[i] = even[i-1];
		if (Max % 2 == 1) {
			long long tt = (Max-1) / 2;
			if (tt % 2 == 0)
				even[i] += odd[i-1]*2;
			else odd[i] += 2*odd[i-1];
		}
		else if (Min % 2 == 1) {
			long long tt = (Min-1) / 2;
			if (tt % 2 == 0)
				even[i] += odd[i-1]*2;
			else odd[i] += 2*odd[i-1];
		}
		PLL a1 = split(Max);
		PLL a2 = split(Min);
		Max = max(a1.first, a1.second, a2.first, a2.second);
		Min = min(a1.first, a1.second, a2.first, a2.second);

		
		//cout << i << " " << odd[i] << " " << even[i] << endl;
	}



	set<PLL> s;
	s.insert(make_pair(n, n));
	for (int i = 0; i <= dep; i++) {
		set<PLL> t;
		for (set<PLL>::iterator itr = s.begin(); itr!=s.end(); itr++) {
			t.insert(split((*itr).first));
			t.insert(split((*itr).second));
		}

		s.clear();
		for (set<PLL>::iterator itr = t.begin(); itr!=t.end(); itr++) 
			s.insert(*itr);
	}

	PLL a[2];
	int j = 0;
	for (set<PLL>::iterator itr = s.begin(); itr!=s.end(); itr++) {
		if (j == 2)
			break;
		a[j] = *itr;
		j++;
	}

	if (j == 1) {
		cout << a[0].first << " " << a[0].second << endl;
		return;
	}

	long long t;
	PLL tmp;
	if (a[0].second > a[1].second) {
		tmp = a[0]; a[0] = a[1]; a[1] = tmp;
	}

	//cout << endl;
	//cout << a[0].first << " " << a[0].second << endl;
	//cout << a[1].first << " " << a[1].second << endl;

	if (a[0].second < a[1].second) {
		if ((a[1].first + a[1].second) % 2 == 0) {
			t = odd[dep-1];
		}
		else t = even[dep-1];

		//cout << t << endl;
		if (sum + t >=k)
			cout << a[1].first << " " << a[1].second << endl;
		else cout << a[0].first << " " << a[0].second << endl;
	}
	else {

		if (a[0].first < a[1].first) {
			tmp = a[0]; a[0] = a[1]; a[1] = tmp;
		}
			
		if ((a[0].first + a[0].second) % 2 == 0) {
			t = odd[dep-1];
		}
		else t = even[dep-1];

		if (sum + t >=k)
			cout << a[0].first << " " << a[0].second << endl;
		else cout << a[1].first << " " << a[1].second << endl;
	}
}

int main() {
	
	p[0] = 1;
	for (int i = 1; i <= 60; i++)
		p[i] = p[i-1]*2;


	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		cin >> n >> k;
		cout << "Case #" << kase <<": ";
		solve();
	}
	return 0;
}