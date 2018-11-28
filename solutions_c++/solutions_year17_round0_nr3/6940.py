#include<bits/stdc++.h>
using namespace std;
vector<pair<long long,long long>> parts;
int main(){
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2.out", "w", stdout);
	int tc;
	long long n, k;
	scanf("%d", &tc);
	for(int i=1; i<=tc; i++){
		scanf("%lld %lld", &n, &k);
		long long div = 1;
		int count = 0;
		while((div-1)<(k)){
			div<<=1;
			count++;
		}
		div>>=1;
		count--;
		long long offset = k-(div-1);
		//cout<<offset<<endl;
		n--;
		parts.push_back({n/2,n-(n/2)});
		while(count>0){
			int sz=parts.size();
			for(int j=0; j<sz; j++){
				pair<long long, long long> num = parts[j];
				int a=num.first-1;
				a=max(0, a);
				int b=num.second-1;
				b=max(0, b);
				parts.push_back({a/2, a-(a/2)});
				parts.push_back({b/2, b-(b/2)});
			}
			parts.erase(parts.begin(),parts.begin()+sz);
			count--;
		}
		sort(parts.rbegin(),parts.rend());
		//for(auto x: parts) printf("(%lld, %lld) ", x.first, x.second);
		//cout<<endl;
		printf("Case #%d: %lld %lld\n", i, parts[offset-1].second, parts[offset-1].first);
		parts.clear();
	}
}
