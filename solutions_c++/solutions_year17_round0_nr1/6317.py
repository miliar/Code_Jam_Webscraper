#include <bits/stdc++.h>
using namespace std;

int solve(string s, int k, int l){
	//cout << "l: " << l << ' ' << s << endl;
	if(l==0)
		return 0;
	int t1, t2;
	if(s[l-1] == '+'){
		t1 = solve(s, k, l-1);
	}
	else{
		int i;
		if(l>=k){
			for(i = l-2; i>= l-k; --i){
				if(s[i]=='+'){
					s[i]='-';
				}
				else{
					s[i]='+';
				}
			}
			for(i = l-2; i>= l-k; --i){
				if(s[i]=='-')
					break;
			}
			if(i<l-k){
				t1 = solve(s, k, l-k);
				t1 = (t1==-1)?t1:t1+1;
			}
			else{
				t1 = solve(s, k, i+1);
				t1 = (t1==-1)?t1:t1+1;
			}
		}
		else
			t1 = -1;
	}
	return t1;
}

int main(){
	int t;
	cin >> t;
	int i;
	for(i=0;i<t;++i){
		int k;
		string s;
		cin >> s >> k;
		int r = solve(s, k, s.size());
		if(r == -1)
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, r);
	}
}