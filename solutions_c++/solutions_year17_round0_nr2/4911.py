#include <iostream>
#include <string>
using namespace std;

bool compare(string n1, string n2){
	for (int i = 0; i < n1.size(); ++i)
	{
		if (n1[i] > n2[i]){
			return true;
		}
		else if(n1[i] == n2[i])
			continue;
		else
			return false;
	}
	return true;
}

void testcase(int ncase, string N){
	cout << "Case #" << ncase << ": ";
	string ans = "";
	
	for (int i = 0; i < N.size(); ++i){
		char c = N[i];
		string nn = ans;
		for (int j = i; j < N.size(); ++j){
			nn = nn + c;
		}
		if ( compare(N, nn) ){
			// cout << "HERE 2: " << N << " ; " << nn << endl;
			ans = ans + c;
		}
		else{
			// cout << "HERE: " << ans << endl;
			c = c-1;
			ans += c;
			for (int j = i+1; j < N.size(); ++j){
				ans += "9";
			}
			if (ans[0] == '0'){
				ans = ans.substr(1);
			}
			cout << ans << endl;
			return;
		}
	}
	if (ans[0] == '0'){
		ans = ans.substr(1);
	}
	cout << ans << endl;
	return;
}

int main(){
	int T;
	cin >> T;
	string N;
	for (int i = 0; i < T; ++i)
	{
		cin >> N;
		testcase(i+1, N);
	}

	return 0;
}