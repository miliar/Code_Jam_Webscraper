#include <bits/stdc++.h>
#define test int t; cin >> t;while(t--)
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

typedef long long ll;

using namespace std;

int main(){
	freopen("B-large(2).in","r",stdin);
	freopen("A3.out","w",stdout);
	int z=1;
	test{
		printf("Case #%d: ",z++);
	string s; cin >> s;

	int l=s.length();


	int index=-1;

	for(int i=l-2;i>=0;i--){
		if(s[i]>s[i+1]){
			s[i]=s[i]-1;
			index=i;
		}
	}

	if(index==-1){
		cout << s << endl;
	}
	else{
		int k=0;

		while(s[k]=='0')k++;


		for(int i=k;i<=index;i++)cout << s[i];


		for(int i=index+1;i<l;i++)cout << '9';

		cout << endl;
	}

	}
	return 0;
}
