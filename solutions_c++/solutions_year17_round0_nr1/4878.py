#include <iostream>
#include <cstring>

using namespace std;

int main(){
	int T, f, j, a;
	char P[1000];
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> P >> f;
		j = strlen(P);
		int k = 0, l, plus, minus;
		plus = minus = a = 0;
		while(k < j - f)
			if(P[k] == '-'){
				for(l = k; l < k + f; l++)
					P[l] = (P[l] == '-' ? '+' : '-');
				a++;
			}
			else{
				k++;
			}
		for(; k < j; k++)
			if(P[k] == '+')
				plus = 1;
			else if(P[k] == '-')
				minus = 1;
		if(plus && minus){
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
		}
		else if(minus){
			cout << "Case #" << i + 1 << ": " << a + 1 << "\n";
		}
		else if(plus){
			cout << "Case #" << i + 1 << ": " << a << "\n";
		}
	}
	return 0;
}