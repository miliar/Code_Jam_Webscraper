#include<stdio.h>
#include<iostream>
#include<vector>
#include <math.h>
#include <map>
#include <string>
using namespace std;

int main()
{
	int T;
	int N, K;
	double D;


  freopen ("A-large.in","r",stdin);
  freopen("A-large-output.out", "w", stdout);

//Getting number of times
	scanf("%d", &T);
	
	//For each number
	for(int t=1;t<=T;t++){
		cin >> N >> K;
		vector<double> R(N,0);
		vector<double> H(N,0);
		vector<double> C(N,0);
		vector<double> A(N,0);
		double max_sum;

		for(int i=0; i<N; i++){
			cin >> R[i] >> H[i];
			A[i] = M_PI * R[i] * R[i];
			//AC[i] = M_PI * R[i] * R[i] + 2 * M_PI * R[i] * H[i];
			C[i] = 2 * M_PI * R[i] * H[i];
		}
		
		max_sum=0;
		for(int i=0; i<N; i++){
			double sum=A[i] + C[i];
			vector<double> temp;

			for(int j=0; j< N;j++){
				if(R[j]<=R[i] && j != i)
					temp.push_back(C[j]);
			}
			sort(temp.begin(),temp.end());
			reverse(temp.begin(),temp.end());			
			for(int j=0;j<K-1 && j<temp.size();j++)
				sum+=temp[j];
				//printf("%.6f\n", sum);
			if(sum>max_sum)
				max_sum = sum;
		}
			
		printf("Case #%d: %.6f\n",t, max_sum);
		
		
		

		
	}

	return 0;
}