#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mk make_pair
#define vi vector<int>
using namespace std;
typedef pair<int, int> pii;
int T;
long long n, cnt, k;
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%lld %lld", &n, &k);
		priority_queue<long long, vector<long long>, less<long long> > q;
		map<long long, long long> F;
		F.clear();
		q.push(n);
		F[n]=1;
		printf("Case #%d: ", cas);
		cnt=0;
		while(!q.empty()){
			long long t=q.top(), a, b;
			q.pop();
			cnt+=F[t];
			a=b=t/2;
			if(t%2==0)
				b--;
			if(cnt>=k){
				if(t&1)
					printf("%lld %lld\n", t/2, t/2);
				else
					printf("%lld %lld\n", t/2, t/2-1);
				break;
			}
			if(a==b){
				if(!F[a])
					q.push(a);
			}
			else{
				if(!F[a])
					q.push(a);
				if(!F[b])
					q.push(b);
			}
			F[a]+=F[t];
			F[b]+=F[t];
		}
	}
	return 0;
}
