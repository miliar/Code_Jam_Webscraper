/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	ifstream cin("A-large.in");
	ofstream cout("a_large_output.txt");

	int t, i, j;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		string s;
		int k, ct = 0;
		cin>>s>>k;
		for(i=0;i<=(((int)s.length())-k);i++){
			if(s[i]=='-'){
				ct++;
				for(j=i;j<(i+k);j++){
					if(s[j]=='-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		for(i=0;i<(int)s.length();i++){
			if(s[i]=='-')
				break;
		}
		if(i==(int)s.length()){
			cout<<ct<<endl;
		}
		else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
