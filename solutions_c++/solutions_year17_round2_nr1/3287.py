#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <limits>
#include <cmath>
#include <stdio.h>

#define MOD 1000000007
#define CANT_H 2502
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define forn2(a, n) for(; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define output_case(i) cout<<"Case #"<<(int)i<<":"
typedef long long tint;

using namespace std;

template<typename T>
void print(T &coleccion){
	forall(elem, coleccion) cout<<" "<<*elem;
	cout << endl;
}

typedef std::numeric_limits< double > dbl;

int horses[1000][2];

double TimeToD(int D, int K, int S){
	return ((double)D-K)/((double)S);
}
void solve(int times){
	int D,N;
	double max_time = 0,res=0;
	cin >> D >> N;
	forn(i,N){
		cin>>horses[i][0]>>horses[i][1];
	}
	forn(i,N){
		max_time = max(max_time, TimeToD(D, horses[i][0], horses[i][1]) );
	}

	if(max_time ==0)
		res = D;
	else
		res = ((double)D)/max_time;

	output_case(times);cout << " ";
	//res = floor(res * 100 + 0.5)/100;

	//cout.precision(dbl::max_digits10-4);
	//cout << res << endl;
	//cout << res << endl;
	printf("%.6lf",res);
	cout << endl;
}

int main(){
	int i=0,T;
	cin>>T; 
	forn(i,T)solve(i+1);
	return 0;
}