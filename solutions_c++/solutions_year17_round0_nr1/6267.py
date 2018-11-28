#include <iostream>
#include <vector>
//#include <tuple>
#include <string>
#include <fstream>

using namespace std;
typedef long long		ll;
typedef vector<ll>		vll;
typedef vector<int>		vi;
typedef vector<vi>		vvi;
//typedef pair<int, int>	ii;
//typedef vector<ii>		vii;
#define INF 1000000000
// ans = a ? b : c; // if(a) ans = b; else ans = c;
// index = (index + 1) % n; // index++; if(index >= n) index = 0;
// index = (index + n - 1) % n; // index--; if (index < 0) index = n - 1;
// int ans = (int)((double)d + 0.5); // for rounding to nearest integer
// ans = min(ans, new_computation)

int main() {
	ofstream f;
	f.open("output.txt");
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int K, flips = 0;
		bool possible = true, incomplete = true;
		string S;
		cin >> S >> K;
		vector <char> s(S.begin(), S.end());
		if(S == string(s.size(), '+')) possible = false;
		while(possible and incomplete){
    		for(int j = 0; j <= s.size() - K; j++){
    		    if(s[j] == '-'){
    		        flips++;
    		        for(int k = j; k < j+K; k++){
    		            s[k] = (s[k] == '-')? '+' : '-';
  		    		}
    		        cout << string(s.begin(), s.end()) << endl;
    		    }
    		}
    		incomplete = false;
    		for(int j = 0; j < s.size(); j++){
    		    if(s[j] != s[j-1] && j > s.size()-K){
    		        possible = false;
    		        break;
    		    }
    		    if(s[j] == '-') incomplete = true;
    		}
		}
		if(S == string(s.size(), '+')) f << "Case #" << i+1 << ": 0" << endl;
		else if(possible) f << "Case #" << i+1 << ": " <<  flips << endl;
		else f << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
	}
}
