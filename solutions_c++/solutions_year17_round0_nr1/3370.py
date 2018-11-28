#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		string S;
		int K;
		cin >> S >> K;
		int res = 0;

		int j = 0;
		for (; j <= (((int) S.size()) - K); ++j)
		{
			if (S[j] == '-'){
				for (int k = 0; k < K; ++k)
				{
					if (S[j+k] == '-'){
						S[j+k] = '+';
					} else{
						S[j+k] = '-';
					}
				}
				res++;
			}
		}

		bool valid = true;
		while (j < (int)S.size()){
			if (S[j] == '-'){
				valid = false;
			}
			j++;
		}

		cout << "Case #" << i << ": ";
		if (valid){
			cout << res << endl;
		} else{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}