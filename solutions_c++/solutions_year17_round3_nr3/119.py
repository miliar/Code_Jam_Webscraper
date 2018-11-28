#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int T;

double arr[53];
double sum[53];

int main(){
	cin>>T;
	for(int cs = 1; cs<=T; ++cs){
		int N, K;
		cin>>N>>K;
		double U;
		cin>>U;
		for(int i = 0; i<N; ++i){
			cin>>arr[i];
		}

		std::sort(arr, arr+N);
		sum[0] = arr[0];
		for(int i = 1; i<N; ++i){
			sum[i] = sum[i-1] + arr[i];
		}
		for(int i = 0;i <N; ++i){
			int now = N-i-1;
			int cnt = N-i;
			if(cnt* arr[now]- sum[now] < U){
				U -= cnt * arr[now] - sum[now];
				arr[now] += U / cnt;
				if(arr[now] > 1){
					arr[now] = 1;
				}
				for(int j = 0; j < now; ++j){
					arr[j] = arr[now];
				}
				break;
			}
		}

		double res = 1;
		for(int i = 0; i< N; ++i){
			res *= arr[i];
		}
		printf("Case #%d: %.6lf\n", cs, res);
		
	}
	return 0;
}
