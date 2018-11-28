#include<iostream>
#include<vector>
using namespace std;

void calculate_left(vector<bool> &A, vector<int> &left){
	left[0]=0;
	if(A[0]==1){
		left[0] =-1;
	}
	for (int i = 1; i < A.size(); ++i){
		if(A[i]==0){
			left[i] = left[i-1]+1;
		}else{
			left[i] = -1;
		}
	}
}
void calculate_right(vector<bool> &A, vector<int> &right){
	right[right.size()-1]=0;
	if(A[right.size()-1]==1){
		right[right.size()-1] = -1;
	}
	for (int i = right.size()-2; i >=0; i--){
		if(A[i]==0){
			right[i] = right[i+1]+1;
		}else{
			right[i] = -1;
		}
	}
}
int main(){
	int T;
	cin>>T;
	freopen("output.txt","w",stdout);
	for(int t=1;t<=T;t++){
		unsigned long long int N,K;
		cin>>N>>K;
		vector<bool> A(N,0);
		vector<int> left(N,0);
		vector<int> right(N,0);
		calculate_left(A,left);
		calculate_right(A,right);
		int best_place = 0;
		int result[2];
		result[0] = max(left[0] , right[0]);
		result[1] = min(left[0] , right[0]);
		for (int j = 0; j < K; j++){
			for(int i=1;i<N;i++){
				if(min(left[i] , right[i]) > min( left[best_place],right[best_place] ) ){
					best_place = i;
					result[0] = max(left[i] , right[i]);
					result[1] = min(left[i] , right[i]);
				}else if( (min(left[i] , right[i]) == min(left[best_place],right[best_place]))  &&  (max(left[i] , right[i])>max(left[best_place],right[best_place]) ) ){
					best_place = i;
					result[0] = max(left[i] , right[i]);
					result[1] = min(left[i] , right[i]);
				}
			}
			A[best_place] = 1;
			calculate_left(A,left);
			calculate_right(A,right);
		}
		cout<<"Case #"<<t<<": "<<result[0]<<" "<<result[1]<<endl;
	}
}