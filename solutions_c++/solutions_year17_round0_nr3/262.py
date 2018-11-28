#include <bits/stdc++.h>
using namespace std;
/***********************************************/
/* Dear online judge:
 * I've read the problem, and tried to solve it.
 * Even if you don't accept my solution, you should respect my effort.
 * I hope my code compiles and gets accepted.
 *  ___  __     _______    _______      
 * |\  \|\  \  |\  ___ \  |\  ___ \     
 * \ \  \/  /|_\ \   __/| \ \   __/|    
 *  \ \   ___  \\ \  \_|/__\ \  \_|/__  
 *   \ \  \\ \  \\ \  \_|\ \\ \  \_|\ \ 
 *    \ \__\\ \__\\ \_______\\ \_______\
 *     \|__| \|__| \|_______| \|_______|
 */
const long long mod = 1000000007;

void add(deque<pair<long long,long long> > & q,long long ad,long long num) {
	if(ad <= 0) {
		return;
	}
	if(!q.empty() && q.back().first == ad) {
		q.back().second += num;
	} else if(q.size() >= 2 && q[q.size() - 2].first == ad) {
		q.back().second += num;
	} else {
		q.push_back({ad,num});
	}
}

long long solve(long long N,long long K) {
	deque<pair<long long,long long> > q;
	q.push_back({N,1ll});
	int cnt = 0;
	while(!q.empty() && K > q.front().second) {
		cnt++;
		long long sz = q.front().first;
		long long num = q.front().second;
		q.pop_front();
		K -= num;
		add(q,(sz-1) - ((sz-1)>>1),num);
		add(q,((sz-1)>>1),num);
	}
	cerr<<cnt<<'\n';
	assert(!q.empty());
	return q.front().first;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C = 1;
	long long N,K,sz;
	cin>>T;
//	{
//		srand(time(NULL));
//		T = 100;
//	}
	while(T--) {
		cout<<"Case #"<<C++<<": ";

		cin>>N>>K;
//		{
//			N = 1000000000ll - rand() * 1ll * rand();
//			K = N - rand() * 1ll * (rand()%10000);
//			cerr<<N<<' '<<K<<endl;
//		}
		sz = solve(N,K);
		cout<<((sz-1ll) - ((sz-1ll)>>1ll))<<' '<<((sz-1ll)>>1ll);

		cout<<'\n';
	}
	return 0;
}
/**/
