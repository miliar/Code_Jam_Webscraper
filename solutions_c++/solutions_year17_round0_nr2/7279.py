#include <bits/stdc++.h>
using namespace std;

typedef int64_t ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef set<ii> sii;
typedef queue<ll> q;

#define FOR(i,n) for(i=0;i<n;i++)
#define all(a) a.begin(), a.end()
#define endl '\n'
#define pb push_back
#define mp make_pair
#define F first
#define S second


int main(){

	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n,i,m,k,ans;
	cin>>n;
	k = n;

	while(n--){
		string temp;
		vector<int> num;

		cin>>temp;

		FOR(i,temp.size()){
			num.pb(temp[i]-48);
		}

		for(i = num.size()-1; i>0; i--){
			if(num[i] < num[i-1]){
				num[i-1] -= 1;
				num[i] = 9;
			}
		}

		cout<<"Case #"<<(k-n)<<": ";

		bool flag=0;
		FOR(i, num.size()){
			if(num[i] == 9){
				flag=1;
			}
			if(flag)
				cout<<"9";
			else if(num[i])
				cout<<num[i];
		}
		cout<<endl;
	}


	return 0;
}
