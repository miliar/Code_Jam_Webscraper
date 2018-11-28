#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("inputBLarge.txt", "r", stdin);
	freopen("outputBLarge.txt", "a", stdout);
	int tc;
	cin >> tc;
	long long int n;
	long long int num;
	for(long long int i = 1; i <= tc; i++) {
		cin >> n;
		vector <int> v;
		num = n;
		long long int remainder;
		long long int count = 0;
		long long int lastRem = 0;
		while(num != 0)
		{
			remainder = num % 10;
			v.push_back(remainder);
			num /= 10;
			count++;
		}
		if(count == 1)
			printf("Case #%lld: %lld\n", i, n);

		else {
			while(lastRem != count - 1) {
				lastRem=0;
				for(long long int j = count - 1;j > 0; j--){
					if(v[j] > v[j-1]){
						v[j] = v[j] - 1;
		 
						for(long long int k = 0; k < j; k++){
							v[k]=9;
						}
					}

					else
					{
						lastRem++;
					}
				}
			}

		bool flag = false;
		printf("Case #%lld: ", i);
		for(long long int j = count - 1; j >= 0; j--) {
			
			if(v[j] != 0) {
				cout<<v[j];
				flag = true;
			}

			if(v[j] == 0 && flag == true){
				cout << v[j];
			}
		}
 
		cout << endl;
		}


	}

	return 0;
}