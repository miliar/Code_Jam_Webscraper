#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

void flip(string &s,int k, int d){
	for (int x=d; x<d+k; x++){
		if (s[x]=='-')
			s[x]='+';
		else
			s[x]='-';
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		string s;
		int K;
		cin>>s>>K;
		int count=0;
		for (int i = 0; i < s.length()-K+1; ++i)
		{
			if (s[i]=='-'){
				flip(s,K,i);
				count++;
			}
			// cout<<s<<endl;
		}
		bool possible=true;
		for (int x=0; x<s.length(); x++){
			if (s[x]=='-')
				possible=false;
		}
		string ans="IMPOSSIBLE";
		if (possible){
			ans=to_string(count);
		}
		cout<<"Case #"<<tc+1<<": "<<ans<<endl;
	}
}