#include <iostream>

using namespace std;

void solveLeft(string &s){
	while(s.size() > 0 && s[0] == '+'){
		s.erase(0,1);
	}
}

void solveRight(string &s){
	int m = s.size();
	while(m > 0 && s[m-1] == '+'){
		s.erase(m-1,1);
		m--;
	}
}

int main(){
	int n, k, m, res;
	string s;
	cin >> n;
	for(int i = 1; i <= n; i++){
		cin >> s >> k;
		solveLeft(s);
		solveRight(s);

		res = 0;
		
		while(s.size()>0){
			if(s.size() < k) break;
			for(int j = 0; j < k; j++){
				s[j] = s[j] == '+' ? '-' : '+';
			}
			solveLeft(s);
			res++;
		}
		if(s.size() == 0)
			cout << "Case #" << i << ": " << res << endl;
		else cout << "Case #" << i << ": IMPOSSIBLE\n";

			
	}
}