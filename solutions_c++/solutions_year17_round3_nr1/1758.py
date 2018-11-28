#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#include <functional>
using namespace std;
# define PI   3.14159265358979323846
typedef struct{
	double R,H,a,b;
}Cy;
Cy cy[1001];
//double mi[1001];
//double R[1001],H[1001];
//double a[1001],b[1001];//a,上表面，b,侧面积
int compare(const void * a,const void * b){
	if((*(Cy*)a).a>(*(Cy*)b).a)return 1;
	else return -1;

}

double findMin(int K,int end){
	double ans = 1;
	for(int i = end-K+1;i<=end;i++){
		ans = min(cy[i].b,ans);
	}
	return ans;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int N,K;
	double sam;
	double mi;
	for(int i = 1;i <= T;i++){
		cin>>N>>K;
		priority_queue <double,vector<double>,greater<double>> cak;
		for(int j = 1;j <= N;j++){
			cin>>cy[j].R>>cy[j].H;
			cy[j].a = PI*cy[j].R * cy[j].R;
			cy[j].b = 2*PI * cy[j].R*cy[j].H;
		}
		qsort(cy+1,N,sizeof(Cy),compare);
		//sam[0] = 0;
		sam = 0;
		mi = 0;
		for(int j = 1;j < K;j++ ){
			sam+=cy[j].b;
			cak.push(cy[j].b);
		}
		double ans = 0;

		for(int j = K;j <= N;j++ ){
			ans = max(ans,sam+cy[j].a+cy[j].b);
			if(!cak.empty()){
			mi = cak.top();
			if(cy[j].b>mi){
			sam = sam - mi + cy[j].b;
			cak.pop();
			cak.push(cy[j].b);}}

		}
		printf("Case #%d: %.9lf\n",i,ans);
		//cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
}