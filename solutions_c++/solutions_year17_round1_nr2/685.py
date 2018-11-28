#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

int N,P;

pair<int,int> bounds(double x,double k){
	return mp(ceil(x/(1.1*k)),floor(x/(0.9*k)));
}

vector<int> solve(vector<int> &req,vector<vector<int>>&packages,vector<int>&servings,int lb,int ub,int &kits){
	for (int i = lb; i <= ub; ++i)
	{
		vector<int>cur=req;
		bool works=true;
		for (int j = 1; j < N; ++j)
		{
			works=false;
			for(int k=req[j]+1; k<P; k++){
				double ratio=(double)packages[j][k]/((double)i*(double)servings[j]);
				if (0.9<= ratio && ratio<=1.1){
					cur[j]=k;
					works=true;
					break;
				}
			}
			if (!works)
				break;
		}
		if (works){
			kits++;
			return cur;
		}
	}
	return req;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		cin>>N>>P;
		vector<int>servings(N);
		for (int i = 0; i < N; ++i)
		{
			cin>>servings[i];
		}
		vector<vector<int>>packages(N,vector<int>(P));
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < P; ++j)
			{
				cin>>packages[i][j];
			}
		}
		for (int i = 0; i < N; ++i)
		{
			sort(packages[i].begin(),packages[i].end());
		}
		vector<int>dp(P);
		vector<vector<int>>used(P,vector<int>(N,-1));
		for (int i = 0; i < P; ++i)
		{
			int kits=0;
			pair<int,int> pos=bounds(packages[0][i],servings[0]);
			vector<int>req(N,-1);
			used[i]=solve(req,packages,servings,pos.first,pos.second,kits);
			dp[i]=kits;
			for (int j = 0; j < i; ++j){
				kits=dp[j];
				req=solve(used[j],packages,servings,pos.first,pos.second,kits);
				if (kits>dp[i]){
					dp[i]=kits;
					used[i]=req;
				}
			}
		}
		// for (int i = 0; i < N; ++i)
		// {
		// 	for (int j = 0; j < P; ++j)
		// 	{
		// 		cout<<packages[i][j]<<" ";
		// 	}
		// 	cout<<endl;
		// }
		cout<<"Case #"<<tc+1<<": "<<dp[P-1]<<endl;
	}
}