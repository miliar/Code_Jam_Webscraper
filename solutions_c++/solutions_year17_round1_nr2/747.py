#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define VVI vector<VI>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>
#define VS vector<string>
#define VVS vector<VS>
#define MAXN 60
#define MAXP 60
#define EPS 1e-9

VVI Q;
int ell[MAXN][MAXP],arr[MAXN][MAXP];
int R[MAXN];
int N,P;
int idx[MAXN];

int leftRange(int q,int r){
	long double num = q;
	long double den = r;
	den *= 1.1;
	long double eps = 1e-9;
	long double res = num / den - eps;
	return (int)ceil(res);
}

int rightRange(int q,int r){
	long double num = q;
	long double den = r;
	den *= 0.9;
	long double eps = 1e-9;
	long double res = num / den + eps;
	return (int)floor(res);
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/1a/B_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/1a/B_output2.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		cin>>N>>P;
		for(int i=0;i<N;i++)
			cin>>R[i];

		Q.clear();
		Q.resize(N);
		for(int i=0;i<N;i++){
			Q[i].resize(P);
			for(int j=0;j<P;j++){
				cin>>Q[i][j];
			}
			sort(Q[i].begin(),Q[i].end());
		}

		for(int i=0;i<N;i++){
			for(int j=0;j<P;j++){
				ell[i][j] = leftRange(Q[i][j],R[i]);
				arr[i][j] = rightRange(Q[i][j],R[i]);
				//printf("range for (%d,%d) is (%d,%d)\n", Q[i][j],R[i], ell[i][j],arr[i][j]);
			}
		}

		for(int i=0;i<N;i++)
			idx[i] = 0;

		int ans = 0;

		while(true){
			int k = -1;
			bool finish = false;
			for(int i=0;i<N;i++){
				if(idx[i] == P){
					finish = true;
					break;
				}
				k = max(k,ell[i][idx[i]]);
			}
			if(finish)
				break;

			for(int i=0;i<N;i++){
				while(arr[i][idx[i]] < k){
					idx[i]++;
					if(idx[i] == P){
						finish = true;
						break;
					}
				}
				if(finish)
					break;
			}
			if(finish)
				break;

			bool good = true;
			for(int i=0;i<N;i++){
				if(ell[i][idx[i]] > k){
					good = false;
					break;
				}
			}
			if(good){
				ans++;
				for(int i=0;i<N;i++)
					idx[i]++;
			}
			else{
				continue;
			}
		}

		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}

	return 0;
}
