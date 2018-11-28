#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iomanip>
using namespace std;

#define PI  3.1415926535898 
int T,K,N;
double re = -1;
struct PAN{
	long long int R,H;
	double S;
}P[1050];
ofstream fout("fout.txt");

bool cmp(PAN x, PAN y){
	if(x.R!=y.R)
		return x.R>y.R;
	return x.H>y.H;
}

double DFS(int s,int l,double t){
	int i,j,k;
	if( K-s+l>N ) //not correct
		return -1;
	if( s == K ) //answer
		return t;
	for( i = l+1 ; i <= N ;i++){
		double S = t;
		if( l )
			S += P[i].S - PI*P[i].R*P[i].R;
		else
			S += P[i].S;
		S = DFS(s+1,i,S);
		if( S > 0 )
			re = max(S,re);
	}
	return re;
}

int main(){
	int t;
	int i,j;

	P[0].H=P[0].R=P[0].S=0;
	cin>>T;
	for( j = 1; j<=T ; j++){
		cin>>N>>K;
		for( i = 1; i <=N ; i++){
			cin>>P[i].R>>P[i].H;
			P[i].S = 2*PI*P[i].R*P[i].H + PI*P[i].R*P[i].R;
		}
		sort(P+1,P+1+N,cmp);
		re = -1;
		fout.setf(ios::fixed);
		fout<<"Case #"<<j<<": ";
		fout<<setprecision(9)<<DFS(0,0,0)<<endl;
	}
	system("pause");
	return 0;
}