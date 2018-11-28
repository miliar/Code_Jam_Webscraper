#include <iostream>
#include <vector>

using namespace std;

int k;

int main() {	
	int t;
	freopen("./B-small-attempt0.in.txt", "r", stdin);
	freopen("./B-small-attempt0.out.txt", "w", stdout);
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		vector <int> v; 
		printf("Case #%d: ", i);
		long int N;
		scanf("%ld", &N);
		while(N != 0){
			v.push_back(N % 10); 
			N = N / 10;
		}
		
		int s = 0;
		while(s < v.size() - 1){		
			if(v[s] < v[s + 1]){
				int j = s - 1;
				while(v[j] == 0 && j > 0){
					v[j] = 9;
					j--;
				}
				v[j] = 9;
				v[s] = 9;
				v[s + 1] -= 1;
			}
			else{
				++s;
			}
		}
		bool firstZero = false;
		for(int kk = v.size() - 1; kk >= 0; --kk){
			if(!firstZero && v[kk] == 0){
				continue;
			}
			else{
				firstZero = true;
			}
			printf("%d", v[kk]);
		}
		printf("\n");
	}		
	
	return 0;
}