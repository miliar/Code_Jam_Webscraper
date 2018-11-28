#include <bits/stdc++.h>

using namespace std;

void solve(long long int n,int cases){
	long long int x = n;
	vector<int> X;
	while(x){
		X.push_back(x%10);
		x /= 10;
	}
	int size = X.size();

	for(int i=0;i<size/2;i++){
		x = X[i];
		X[i] = X[size-i-1];
		X[size-i-1] = x;
	}

	//printf("X[0] : %d\tX[1] : %d\n",X[0],X[1] );

	int i=0;
	int current = X[i];
	i++;
	while(i<size){
		if(current<=X[i]){
			current = X[i];
			i++;
		}
		else{
			break;
		}
	}
	
	if(i<size){
		int j= i-1;
		if(X[j]==1){
			X[0] = 0;
			for(int k=1;k<size;k++) X[k] = 9;
		}
		else{
			for(int k=i;k<size;k++) X[k] = 9;
			i--;
			if(i==0){
				X[i] -= 1;
			}
			else{
				if(X[i]!=X[i-1]) X[i] -= 1;
				else{
					while(i>0 && X[i]==X[i-1]){
						X[i] = 9;
						i--;
					}
					X[i] -= 1;
				}
			} 
		}
	}


	/*
	if(i<size){
		int j = i;
		if(X[j-1]!=1){
			X[j-1]--;
			while(j>=2 && X[j-1]==X[j-2]){
					X[j-1] -= 1;
				j--;
			}
			X[j-1]--;
		}
		else{
			X[j-1] = 9;
			j--;
			while(j>=0){
				X[j] = 9;
				j--;
			}
			X[0] = 0;
		}
		while(i<size){
			X[i] = 9;
			i++;
		}
	}
	*/


	printf("Case #%d: ",cases);
	if(X[0]!=0) printf("%d", X[0]);

	for(int i=1;i<size;i++)
		printf("%d",X[i]);

	cout<<endl;

	
}

int main(){
	int t;
	long long int n;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%lld",&n);
		solve(n,i);
	}
}