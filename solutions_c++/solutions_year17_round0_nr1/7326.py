#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;

	cin >> t;

	for(int y=1; y<=t; y++){
		int k;
		string s;

		cin >> s >> k;

		int count=0;
		for(int i=0; i<=(int)s.size()-k; i++){
			if(s[i]=='+') continue;

			for(int j=0; j<k; j++)
				s[i+j]=s[i+j]=='-' ? '+' : '-';

			count++;
		}

		bool flag=true;
		for(int i=0; i<(int)s.size(); i++){
			if(s[i]=='-') flag=false;
		}

		printf("Case #%d: ", y);

		if(flag)
			printf("%d\n", count);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
