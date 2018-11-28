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

bitset<1001> S,K;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C = 1;
	string s;
	int k;
	cin>>T;
//	{
//		srand(time(NULL));
//		T = 100;
//	}
	while(T--) {
		cout<<"Case #"<<C++<<": ";

		cin>>s>>k;
		K.reset();
		S.reset();
		for(int i = 0;i < k;i++) {
			K[i] = true;
		}
		for(int i = 0;i < (int)s.size();i++) {
			S[i] = s[i] == '-';
		}
		
		int res = 0;
		bool can = true;
		for(int i = 0;i < (int)s.size();i++) {
			if(S[i]) {
				res++;
				if(i + k - 1 >= (int)s.size()) {
					can = false;
					break;
				}
				S ^= K<<i;
//				cerr<<S<<'\n';
			}
		}
		if(can)
			cout<<res;
		else
			cout<<"IMPOSSIBLE";

		cout<<'\n';
	}
	return 0;
}
/**/
