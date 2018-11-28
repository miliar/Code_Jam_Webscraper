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
	int num_of_case = 0;

	while(t--){
		num_of_case++;
		string s;
		cin >> s;

		int k;
		cin >> k;

		int coun = 0;
		for(int i=0; i<sz(s); i++){
			if(i+k-1 < sz(s)){
				if(s[i] != '+'){
					coun++;
					for(int j=i; j<i+k; j++){
						if(s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
					}
				}
			}
			else
				break;
		}

		int i;
		for(i=0; i<sz(s); i++){
			if(s[i] == '-'){
				cout << "Case #" << num_of_case << ": IMPOSSIBLE" << endl;
				break;
			}
		}

		if(i == sz(s))
			cout << "Case #" << num_of_case << ": " << coun << endl;
	}
	return 0;
}