#include <bits/stdc++.h>

using namespace std;

const int N=1000070; //10e6

#define ll long long int
#define inf 0x3f3f3f3f
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define ii tuple<int, int>
#define all(x) (x).begin(), (x).end()

string tostring(ll k){
	string s, w;
	while (k){
		s+=(k%10)+'0';
		k/=10;
	}
	for(int i=0; i<s.size(); i++){
		w+=s[s.size()-i-1];
	}
	return w;
}

string x[N];

int main(int argc, char const *argv[]){
	int t;
	scanf("%d", &t);
	int curr=1;
	string s;
	for(int i=1; i<=200000; i++){
		s=tostring(curr++);
		bool flag=true;
		for(int i=1; i<s.size(); i++){
			if(s[i]<s[i-1])flag=false;
		}
		if(flag)x[i]=s;
		else x[i]=x[i-1];
	}
	int counter=1;
	while(t--){
		ll n;
		scanf("%lld", &n);
		printf("Case #%d: ", counter++);
		cout << x[n] << endl;
	}
	return 0;	
}