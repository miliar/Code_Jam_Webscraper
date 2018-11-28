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

int k;
string change(string w, int pos){
	for(int i=pos; i<pos+k; i++){
		if(w[i]=='+')w[i]='-';
		else w[i]='+';
	}
	return w;
}

int main(int argc, char const *argv[]){
	int  t, counter=1;
	scanf("%d", &t);
	while(t--){
		string s;
		cin >> s >> k;
		int ans=0;
		bool flag=true;
		for(int i=0; i<s.size(); i++){
			if(s[i]=='-' && i>s.size()-k){
				flag=false;
				break;
			}else if(s[i]=='-'){
				s=change(s, i);
				ans++;
			}
		}
		printf("Case #%d: ", counter++);
		if(flag)printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}