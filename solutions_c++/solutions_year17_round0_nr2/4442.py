#include<bits/stdc++.h>

#define lld long long int

using namespace std;

int main()
{
	int T;
	lld n;
	vector<int> num;
	cin>>T;
	for(int t = 1; t <= T; t++){
		cin>>n;
		if(n < 10){
			cout<<"Case #"<<t<<": "<<n<<endl;
			continue;
		}
		num.clear();
		lld m = n;
		while(m > 0){
			num.push_back(m%10);
			m /= 10;
		}
		for(int i = 1; i < (int)num.size(); i++){
			if(num[i] > num[i-1]){
				for(int j = 0; j < i; j++){
					num[j] = 9;
				}
				num[i] -= 1;
			}
		}
		m = 0LL;
		for(int i = (int)num.size() - 1; i >= 0; i--){
			m = m*10LL + num[i];
		}
		cout<<"Case #"<<t<<": "<<m<<endl;
	}
	return 0;
}