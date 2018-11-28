#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main () {

	int t;
	cin>>t;
	for(int c = 1;c<=t;c++){
		printf("Case #%d: ", c);
		string s;
		cin>>s;
		int k;
		cin>>k;

		int ans = 0;
		bool ok = true;
		for(int i = 0;i<s.size() && ok;i++){
			if(s[i] == '-'){
				if(i+k-1>=s.size())ok = false;
				else{ans++;for(int j = i;j<i+k;j++)s[j] = (s[j]=='-')?'+':'-';}
			}
		}
		if(!ok)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);

	}

	return 0;
}