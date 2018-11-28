#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

int main(){
	int t,caso = 1;
	scanf("%d",&t);
	while(t--){
		long long n,k;
		multiset<int> s;
		scanf("%lld %lld",&n,&k);
		long long at = 1, i = 1,ansl,ansr;
		s.insert(n);
		while(i != k + 1){
			auto it = s.end();
			it--; 
			//printf("%d\n",*it );
			if(i == k){
				if(*it%2){
					ansl = ansr = *it/2;
				}
				else{
					ansl = *it/2;
					ansr = *it/2 - 1;
				}
				break;
			}
			if(*it%2){
				s.insert(*it/2);
				s.insert(*it/2);
			}
			else{
				s.insert(*it/2 - 1);
				s.insert(*it/2);
			}
			s.erase(it);
			i++;
		}
		printf("Case #%d: %lld %lld\n",caso,ansl,ansr);
		caso++;
	}
	return 0;
}