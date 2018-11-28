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

		string s;
		cin >> s;

		for(int i=1; i<sz(s); i++){
			if(s[i] < s[i-1] && s[i-1] > '1'){
				s[i-1]--;
				for(int j=i; j<sz(s); j++)
					s[j] = '9';
				for(int j=i-1; j>0; j--){
					if(s[j] < s[j-1]){
						s[j] = '9';
						s[j-1]--;
					}
				}
				break;
			}
			else
			if(s[i] < s[i-1] && s[i-1] == '1'){
				string st = "";
				for(int j=0; j<sz(s)-1; j++){
					st += "9";
				}
				s = st;
				break;
			}

		}

		cout << "Case #" << num_of_cases << ": " << s << endl;


	}
	return 0;
}