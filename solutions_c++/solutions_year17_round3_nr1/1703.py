#include <fstream>
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


//#define defFile
#ifdef defFile
ifstream fin ("a.in");
ofstream fout ("a.out");
#define cin fin
#define cout fout
#endif

struct P{
	int R,H;
}arr[2000];

double H[1010][1010];

double pi;

int cmp(const void* pa,const void* pb){
	P a=*(P*)pa;
	P b=*(P*)pb;
	
	return b.R-a.R;
}

void doatest(){

	int N,K;
	cin>>N>>K;
	for(int i=0;i<N;i++)
		cin>>arr[i].R>>arr[i].H;

	qsort(arr,N,sizeof(P),cmp);
	
	for(int k=0;k<=K;k++)
		H[N][k]=-1000000;
	for(int start=0;start<=N;start++)
		H[start][0]=0.0;
	for(int k=1;k<=K;k++){
		for(int start=N-1;start>=0;start--){
			if(k<K)
				H[start][k]=max(H[start+1][k],
					H[start+1][k-1]+(double)arr[start].H*arr[start].R*2*pi);
			else
			{
				H[start][k]=max(H[start+1][k],
					H[start+1][k-1]+(double)arr[start].H*arr[start].R*2*pi+(double)arr[start].R*arr[start].R*pi);
			}
		}
	}

	double best=-1000000;
	for(int start=0;start<N-K+1;start++){
		double temp=H[start][K];
		if(temp>best)
			best=temp;
	}
	printf("%.9lf\n",best);

}

int main(){
	int T;
	pi=atan(1.0)*4.0;
	cin>>T;
	loop(T,t){
		cout<<"Case #"<<t+1<<": ";
		doatest();
	}

	return 0;
}