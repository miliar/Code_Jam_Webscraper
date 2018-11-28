#include<bits/stdc++.h>
using namespace std;

struct stall_pair{
	int L, R;
	stall_pair(int L, int R) : L(L), R(R){}
	int getOpt(){
		return (R-L)/2 + L;
	}
	int getMin(){
		return min(getOpt()-L-1, R-getOpt()-1);
	}
	int getMax(){
		return max(getOpt()-L-1, R-getOpt()-1);
	}
	friend bool operator<(stall_pair A, stall_pair B){
		if(A.getMin()==B.getMin()){
			if(A.getMax()==B.getMax()){
				return A.getOpt()>B.getOpt();
			}
			return A.getMax()<B.getMax();
		}
		return A.getMin()<B.getMin();
	}
};

int main(){
	int tcn = 1;
	int t; cin>>t;
	while(t--){
		int N, K;
		cin>>N>>K;
		priority_queue<stall_pair> pq;
		pq.push(stall_pair(0,N+1));
		for(int i = 0; i<K-1; i++){
			stall_pair c = pq.top(); pq.pop();
			int opt = c.getOpt();
			pq.push(stall_pair(c.L,opt));
			pq.push(stall_pair(opt,c.R));
		}
		stall_pair lastc = pq.top();
		cout<<"Case #"<<tcn++<<": "<<lastc.getMax()<<" "<<lastc.getMin()<<endl;
	}
}