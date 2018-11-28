#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int T;
	int N;
	double D;


  freopen ("A-large.in","r",stdin);
  freopen("A-large-output.out", "w", stdout);

//Getting number of times
	scanf("%d", &T);


	//For each number
	for(int t=1;t<=T;t++){
		cin >> D >> N;
		vector<double> K(N,0);
		vector<double> S(N,0);
		vector<double> T(N,0);
		
		for(int i=0; i<N; i++){
			cin >> K[i] >> S[i];
			T[i] = (D - K[i])/S[i];		
		}	
		
		double max = *max_element(T.begin(),T.end());
		
		printf("Case #%d: %.6f\n", t, D/max);
		
	}

	return 0;
}