#include <bits/stdc++.h>

using namespace std;

const int inf = 2e9 + 20;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii;
typedef priority_queue<int> pqmax;
typedef priority_queue<int, vector<int>, greater<int> > pqmin; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

int main(){
	int t;
	cin >> t;

	int num_of_cases = 0;

	while(t--){
		num_of_cases++;

		int n,k;
		cin >> n >> k;

		vi ls(n);
		vi rs(n);
		vector<bool> occupied(n, false);

		for(int i=0; i<n; i++){
			ls[i] = i;
			rs[i] = n-1-i;
		}

		int minlr, maxlr;
		while(k--){
			for(int i=0; i<n; i++){
				if(!occupied[i]){
					int index = i;
					minlr = min(ls[i], rs[i]);
					maxlr = max(ls[i], rs[i]);

					for(int j=i+1; j<n; j++){
						if(occupied[j])
							continue;
						if(min(ls[j], rs[j]) > minlr){
							minlr = min(ls[j], rs[j]);
							maxlr = max(ls[j], rs[j]);
							index = j;
						}

						else
						if(min(ls[j], rs[j]) == minlr && max(ls[j],rs[j]) > maxlr){
							minlr = min(ls[j], rs[j]);
							maxlr = max(ls[j], rs[j]);
							index = j;
						}
					}
					occupied[index] = true;
					break;
				}
			}

			for(int i=1; i<n; i++){
				if(!occupied[i-1])
					ls[i] = 1 + ls[i-1];
				else
					ls[i] = 0;
			}

			for(int i=n-2; i>=0; i--){
				if(!occupied[i+1])
					rs[i] = 1 + rs[i+1];
				else
					rs[i] = 0;
			}

		}		

		cout << "Case #" << num_of_cases << ": " << maxlr << " " << minlr << endl;


	}
	return 0;
}