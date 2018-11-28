#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define inf 1e18
#define pb push_back
#define mp make_pair
#define Int long long
#define fs first
#define sc second
#define pii pair<int, int>

int main(){

	int t, T, i, j;

	cin>>T;

	for(t = 1; t <= T; t++){
		string S, Ans;
		bool cond = 1;
		cin>>S;

		while(cond){
			cond = 0;
			for(i = 1; i < S.size(); i++){
				if(S[i] < S[i-1]){
					S[i-1]--;
					cond = 1;
					for(j = i; j < S.size(); j++)
						S[j] = '9';
				}
			}
		}
		for(i = 0; i < S.size(); i++)
			if(S[i] != '0')
				break;
		for(; i < S.size(); i++)
			Ans += S[i];
		cout<<"Case #"<<t<<": "<<Ans<<endl;
	}

	return 0;
}