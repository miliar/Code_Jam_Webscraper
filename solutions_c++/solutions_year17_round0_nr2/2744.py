#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

bool valid(string N){
	for (int i = 0; i < N.length()-1; ++i)
	{
		if (N[i]>N[i+1])
			return false;
	}
	return true;
}

string nines(int k){
	string ans="";
	for (int x=0; x<k; x++)
		ans+="9";
	return ans;
}

string reduce(string N){
	string ans=N;
	int n=N.length();
	string p1;
	string p2;
	for (int i = 0; i <n-1; ++i)
	{
		if(N[i]>N[i+1]){
			p1=to_string(stoll(N.substr(0,i+1))-1);
			p2=nines(n-1-i);
			ans=p1+p2;
			break;
		}
	}
	if (ans[0]=='0')
		ans=ans.substr(1);
	return ans;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		string N;
		cin>>N;
		string ans=N;
		while(!valid(ans))
			ans=reduce(ans);
		cout<<"Case #"<<tc+1<<": "<<ans<<endl;
	}
}