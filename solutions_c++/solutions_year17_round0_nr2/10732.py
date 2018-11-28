#include<iostream>
using namespace std;
int main() {
	int T;
	unsigned long long N, num, a, b;
	cin>>T;

	for(int i=1; i<=T; i++){
		cin>>N;
		int result = 0;

		while(!result){
			num = N;
			while(num > 0){
				a = num % 10;
				b = (num/10) % 10;
				if(a < b){
					result = 0;
					break;
				}
				result = 1;
				num = num/10;
			}
			N--;
		}

		cout<<"Case #"<<i<<": "<<N+1<<endl;
		
	}

	return 0;
}