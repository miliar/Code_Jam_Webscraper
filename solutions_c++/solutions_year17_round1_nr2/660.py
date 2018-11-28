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

deque<pair<long long,long long> > rng[51];
long long R[51];

bool cmp(pair<long long,long long> a,pair<long long,long long> b) {
	return make_pair(a.second,a.first) < make_pair(b.second,b.first);
}

void bs(int i,long long s,long long e,long long & res,bool movee, long long Q) {
	res = -1;
	while(s <= e) {
		long long md = (s + e) >> 1;
		if((md * R[i] * 110) / 100 >= Q && (md * R[i] * 90 + 100 - 1) / 100 <= Q) {
			res = md;
			if(movee) {
				e = md - 1;
			} else {
				s = md + 1;
			}
			continue;
		} 

		if((md * R[i] * 90 + 100 - 1) / 100 > Q) {
			e = md - 1;
		} else {
			s = md + 1;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	srand(time(NULL));

	int T,C = 1;
	cin>>T;
	while(T--) {
		cout<<"Case #"<<C++<<": ";

		int N,P;
		long long Q;
		cin>>N>>P;
		for(int i = 0;i < N;i++) {
			cin>>R[i];
		}
		for(int i = 0;i < N;i++) {
			rng[i].clear();
			for(int j = 0;j < P;j++) {
				cin>>Q;
				long long lo,hi;
				bs(i,1,INT_MAX,lo,true,Q);
				bs(i,1,INT_MAX,hi,false,Q);
				assert(lo <= hi);
				assert(lo != -1 || hi == -1);
				if(lo == -1 || hi == -1) {
					continue;
				}
				//				cerr<<lo<<' '<<hi<<' '<<Q<<' '<<R[i]<<endl;
				rng[i].push_back({lo,hi});
			}
			sort(rng[i].begin(),rng[i].end(),cmp);
		}

		bool can = true;
		int res = 0;
		while(can) {
			long long mn = LLONG_MAX;
			long long mx = LLONG_MIN;
			for(int i = 0;i < N;i++) {
				if(rng[i].empty()) {
					can = false;
					break;
				}
				mx = max(mx,rng[i][0].first);
				mn = min(mn,rng[i][0].second);
			}
			if(!can)
				break;
			if(mn < mx) {
				for(int i = 0;i < N;i++) {
					if(rng[i][0].second < mx) {
						rng[i].pop_front();
					}
				}
			} else {
				res ++;
				for(int i = 0;i < N;i++) {
					rng[i].pop_front();
				}
			}
		}
		cout<<res;

		cout<<'\n';
	}
	return 0;
}
/**/
