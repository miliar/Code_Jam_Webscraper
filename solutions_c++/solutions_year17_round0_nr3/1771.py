//Freaking VIM Editor :p
//Tapopadma Tripathy
#include<bits/stdc++.h>
using namespace std;
#ifdef ONLINE_JUDGE
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif

void print(map<long long int, long long int>mm){
	puts("--------------");
	tr(mm, it){
		cout << it->first << " " << it->second << endl;
	}
	puts("--------------");
}

void test1(long long int n, long long int k){
	map<long long int, long long int>mm;
	set<long long int>s;
	mm[n] = 1;
	s.insert(n);
	print(mm);
	for (long long int i = 1; i < k; ++i){
		long long int num = *s.rbegin();
		--mm[num];
		if (mm[num] == 0)s.erase(num);
		if (num & 1){
			long long int a = num >> 1;
			if (a){
				mm[a] += 2;
				s.insert(a);
			}
		}
		else{
			long long int b = num >> 1, a = b - 1;
			if (a > 0){
				++mm[a]; s.insert(a);
			}
			if (b > 0){
				++mm[b]; s.insert(b);
			}
		}
		print(mm);
	}
	long long int num = *s.rbegin();
	long long int cc = num >> 1;
	if (num & 1){
		cout << cc << " " << cc << endl;
	}
	else{
		cout<<cc<< " "<<(cc - 1) << endl;
	}
}

long long int Total(map<long long int, long long int>mm){
	long long int ret = 0;
	tr(mm, it){
		ret += it->second;
	}
	return ret;
}

void solve(long long int n, long long int k){
	map<long long int, long long int>mm;
	mm[n] = 1;
	long long int tot;
	while ((tot = Total(mm)) <= k){
		map<long long int, long long int>nn;
		tr(mm, it){
			long long int num = it->first;
			long long int counterr = it->second;
			long long int num1 = (num >> 1ll) - ((num & 1ll) == 0);
			if (num1 > 0)nn[num1] += counterr;
			long long int num2 = (num >> 1ll);
			if (num2 > 0)nn[num2] += counterr;
		}
		mm = nn;
		k -= tot;
	}
	vector<pair<long long int, long long int> > vv;
	tr(mm, it){
		vv.push_back(make_pair(it->first, it->second));
	}
	sort(vv.begin(), vv.end());
	long long int sz = vv.size();
	bool done = false;
	for (long long int i = sz - 1; i >= 0; --i){
		long long int num = vv[i].first, counterr = vv[i].second;
		if (counterr <= k){
			k -= counterr; continue;
		}
		printf("%lld %lld\n", num >> 1ll, (num >> 1ll) - ((num & 1ll) == 0));
		done = true; break;
	}
	if (!done){
		printf("0 0");
	}
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; 
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs){
		long long int n, k;
		scanf("%lld %lld", &n, &k);
		--k;
		//test1(n, k);
		printf("Case #%d: ", cs);
		solve(n, k);
	}
	return 0;
}