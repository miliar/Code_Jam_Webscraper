#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;
typedef long long i64;




int S[MAX];
int K[MAX];

int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'

    int T; cin >> T;
    for(int tt = 0; tt < T; tt++){
    	cout << "Case #" << tt + 1 << ": ";
    	int ar[6];
    	int N;
    	cin >> N;
    	char lett[7] = "ROYGBV";
    	for(int i = 0; i  < 6; i++)cin >> ar[i];
    	bool eedd = false;
    	for(int i = 0; i < 6; i += 2){
    		if(ar[i] + ar[(i + 3 ) % 6] == N){
    			if(ar[i] == ar[(i + 3 ) % 6]){
    				for(int j = 0; j < N/2 ;j++){
						cout << lett[i] << lett[(i + 3 ) % 6];
					}
    				cout << endl;
    			}
    			else{
    				cout << "IMPOSSIBLE" << endl;
    			}
    			eedd = true;
    			break;

    		}
    	}
    	if(eedd)continue;
    	bool poss = true;
    	for(int i = 1; i < 6 && poss; i+= 2){
    		if(ar[i] > 0 && ar[i] + 1 > ar[(i + 3) % 6])poss = false;
    	}
    	for(int i = 0; i < 6 && poss; i+= 2){
			if(ar[(i + 5) % 6] + ar[(i + 1) % 6] + ar[i] > N / 2)poss = false;
		}
    	if(!poss){
    		cout << "IMPOSSIBLE" << endl;
    		continue;
    	}

    	int tot = 0;
    	int beg = 0;
    	while(beg < 6 && ar[beg] == 0)beg+=2;
    	if(beg == 6){
    		cout << "IMPOSSIBLE" << endl;
			continue;
    	}

    	vector<int> ans (N);
    	ans[0] = beg;
    	tot++;
    	ar[beg]--;
    	int cur = beg;
    	while(tot < N){
			if(ar[(cur + 3) % 6] > 0){
				ans[tot] = (cur + 3) % 6;
				ar[(cur + 3) % 6]--;
				if(ar[cur] == 0){
					break;
				}
				ar[cur]--;
				ans[tot + 1] = cur;
				tot += 2;
			}
			else{
				if(ar[(cur + 2) % 6] > ar[(cur + 4) % 6] ){
					ar[(cur + 2) % 6]--;
					ans[tot] = (cur + 2) % 6;
					tot += 1;
					cur = (cur + 2) % 6;
				}
				else if(ar[(cur + 2) % 6] == ar[(cur + 4) % 6] ){
					if(ar[(cur + 2) % 6] == 0)break;
					if((cur + 2) % 6 == ans[0]){
						ar[(cur + 2) % 6]--;
						ans[tot] = (cur + 2) % 6;
						tot += 1;
						cur = (cur + 2) % 6;
					}
					else{
						ar[(cur + 4) % 6]--;
						ans[tot] = (cur + 4) % 6;
						tot += 1;
						cur = (cur + 4) % 6;
					}
				}
				else{
					ar[(cur + 4) % 6]--;
					ans[tot] = (cur + 4) % 6;
					tot += 1;
					cur = (cur + 4) % 6;
				}
			}
    	}
    	if(tot == N and ans[0] != ans[N - 1]){
    		for(int i = 0; i < 6; i++)assert(ar[i] == 0);
    		for(int i = 0; i < N; i++){
    			cout << lett[ans[i]];
    			assert(ans[i] != ans[(i + 1) % N]);
    		}

    		cout << endl;
    	}
    	else{
    		cout << "IMPOSSIBLE" << endl;
    	}

    }

}

