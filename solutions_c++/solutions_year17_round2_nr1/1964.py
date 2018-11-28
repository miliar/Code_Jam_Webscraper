#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <utility>
#include <math.h>

#define FOR(i,x,y) for(int i=x;i<=y;i++)
#define ROF(i,x,y) for(int i=x;i>=y;i--)
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define sz(X) ((int)(X).size()) 
#define MAX_int (1<<31)-1
#define MIN_int -(1<<31)+1

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI; 


int k[200000],s[200000];
double et;
int main(){

	int t,n;
	double d;
	cin >> t;
	for(int lap=1; lap<=t; lap++){
		scanf("%lf %d",&d,&n);
		double mint = -1;
		for(int i=0;i<n;i++){
			scanf("%d %d",&k[i],&s[i]);
			double et = (d-k[i])/s[i];
			mint = max(et, mint);
		}
		cout << "Case" << " #" << lap << ": ";
		printf("%lf\n",d/mint);

	}
	return 0;
}