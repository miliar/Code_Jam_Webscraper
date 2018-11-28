#include <iostream>
#include <string>

using namespace std;

int N;

void solve(string s, int K){
	static int caseNumber = 1;
	int res = 0;
	for(int i=0;i<s.size()-K+1;i++)
		if(s[i] == '-'){
			for(int j=i;j<i+K;j++)
				s[j] = (s[j] == '-' ? '+' : '-');
			res++;
		}
	for(int i=s.size()-K+1;i<s.size();i++)
		if(s[i] == '-'){
			cout << "Case #" << caseNumber++ << ": " << "IMPOSSIBLE" << endl;
			return;
		}
	cout << "Case #" << caseNumber++ << ": " << res << endl;
}

int main(){
	string s;
	int k;
	cin >> N;
	for(int i=0;i<N;i++){
		cin >> s >> k;
		solve(s, k);
	}
}