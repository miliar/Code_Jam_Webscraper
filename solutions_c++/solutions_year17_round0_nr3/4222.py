#include <bits/stdc++.h>

using namespace std;

#define MAX 2147483647
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push

typedef long long int ll;
typedef pair<ll,ll> ii;
typedef pair<string,string> ss;
typedef vector<ss> vss;
typedef pair<ll, ii> iii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef vector<ii> vii;
typedef deque<ll> dqi;
typedef unordered_set<ll> usi;
typedef set<ll> si;
typedef unordered_set<ii> usii;
typedef set<ii> sii;
typedef unordered_map<ll,ll> umii;
typedef map<ll,ll> mii; 
typedef map<string,int> msi;
typedef map<int,string> mis;

ll n,k,stalls;
bool visited[1000008];

struct myComp
{
	bool operator()(ii a, ii b){
		ll mida = (a.second + a.first)/2;
		ll midb = (b.second + b.first)/2;
		ll maxa = max(abs(a.second-mida), abs(mida-a.first));
		ll mina = min(abs(a.second-mida), abs(mida-a.first));
		ll maxb = max(abs(b.second-midb), abs(midb - b.first));
		ll minb = min(abs(b.second-midb), abs(midb - b.first));
		// printf("a: (%lld,%lld)\t b: (%lld, %lld)\n",a.first, a.second, b.first, b.second );
		// printf("mina: %lld,  maxa: %lld,  minb: %lld, maxb: %lld\n",mina, maxa, minb, maxb );
		// if((mina > minb or (mina == minb and maxa > maxb) or (mina == minb and maxa == maxb and mida <= midb)))
		// 	printf("a first pops\n");
		// else
		// 	printf("b first pops\n");
		return !(mina > minb or (mina == minb and maxa > maxb) or (mina == minb and maxa == maxb and mida < midb));
	}
};

// void check(){
// 	priority_queue<ii, vii, myComp> q;
// 	ii temp;
// 	ll mid,maxa, mina;
// 	ll count=0;
// 	q.push(make_pair(1,4));
// 	q.push(make_pair(1,1));
// 	q.push(make_pair(3,4));
// 	q.push(make_pair(4,4));
// 	q.push(make_pair(1,9));
// 	q.push(make_pair(5,8));
// 	q.push(make_pair(5,9));
// 	while(!q.empty()){
// 		temp = q.top();
// 		mid = (temp.first + temp.second)/2;
// 		count++;
// 		printf("%lld %lld %lld     %lld\n", temp.first, temp.second, mid, count);
// 		q.pop();
// 	}
// }

ii simultate(){
	priority_queue<ii, vii, myComp> q;
	ii temp;
	ll mid,maxa, mina;
	ll count=0;
	q.push(make_pair(1,stalls));
	while(!q.empty()){
		temp = q.top();
		q.pop();
		mid = (temp.first + temp.second)/2;
		if(temp.first > temp.second)
			continue;
		count++;
		// printf("%lld %lld %lld     %lld\n", temp.first, temp.second, mid, count);
		
		
		if(count == k){
			mid = (temp.first + temp.second)/2;
			maxa = max(abs(temp.second-mid), abs(temp.first - mid));
			mina = min(abs(temp.second-mid), abs(temp.first - mid));
			return make_pair(maxa, mina);
		}
		if(mid == temp.second and temp.first == mid)
			continue;
		if(temp.second > temp.first){
			if(mid + 1 <= temp.second)
				q.push(make_pair(mid+1, temp.second));
			if(mid - 1 >= temp.first)
				q.push(make_pair(temp.first, mid-1));
		}
	}

	return make_pair(-1,-1);
}

int main(){
	int testcases;
	ii result;
	scanf("%d",&testcases);
	for(int xl=1;xl<=testcases;xl++){
		scanf("%lld %lld",&n, &k);
		// printf("%lld %lld\n",n,k );
		stalls = n;
		result = simultate();
		printf("Case #%d: %lld %lld\n",xl, result.first, result.second);
	}
	return 0;
}

// int main(){
// 	check();
// }