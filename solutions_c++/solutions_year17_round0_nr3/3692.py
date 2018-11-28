#include <iostream>
#include <queue>
#define endl '\n'
#define jizz cin.tie(0);ios_base::sync_with_stdio(0);
using namespace std;
priority_queue< int,vector<int>,less<int> > pq;
int main(){jizz
	int T,p = 0;cin >> T;
	while(T--){
		while(!pq.empty())pq.pop();
		int n,k;cin >> n >> k;
		pq.push(n);
		for(int i = 1 ; i < k ; i++){
			int tmpp,tmp = pq.top();
			if(tmp % 2)tmpp = tmp/2;
			else tmpp = tmp/2-1;
			pq.pop();
			tmp /= 2;
			pq.push(tmp);pq.push(tmpp);
		}
		cout << "Case #"<< ++p <<": ";
		int anss,ans = pq.top();
		if(ans % 2)anss = ans/2;
		else anss = ans/2-1;
		ans /= 2;
		cout << ans << ' ' << anss << endl;
	}
}
