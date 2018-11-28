#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

typedef pair<int,int> pii;
typedef pair<int,double> pid;
typedef pair<double,double> pdd;
typedef pair<double,int> pdi;
typedef vector<int> vi;
typedef vector<pid> vid;

typedef pid Edge;
typedef vid EdgeList;
typedef vector<EdgeList> Graph;

#define sp ' '
#define tab '\t'

#define loop(n,i) for(int i=0;i<(n);i++)
#define loopOn(arr,x) for(auto& x:arr)
#define iterOn(arr,iter) for(auto& iter=arr.begin();iter!=arr.end();iter++)


void doatest(int D,int N,vector<pii> H){
	double L=-1000000000;
	int P=-1;
	for(int n=0;n<N;n++){
		double t=(double)(D-H[n].first)/H[n].second;
		if(t>L){
			L=t;
			P=n;
		}
	}
	printf("%.6Lf\n",D/L);
}


int main(){
	
	int T;
	cin>>T;
	loop(T,t){
		int D,N;
		cin>>D>>N;
		vector<pii> H;
		loop(N,n){
			int k,s;
			cin>>k>>s;
			H.push_back(pii(k,s));
			
			
		}
		printf("Case #%d: ",t+1);
		
		doatest(D,N,H);

	}

	return 0;
}