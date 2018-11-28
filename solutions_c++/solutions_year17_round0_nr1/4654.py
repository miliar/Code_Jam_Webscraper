/*	In the name of God	*/
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

string s;
int main(){
	int tc,k;
	 freopen("A-large.in", "r", stdin);
	 freopen("program.out", "w", stdout);
	cin>>tc;
	for (int ti = 0; ti < tc; ++ti) {
		cin>>s>>k;
		bool f=1;
		int c=0;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i]=='-'){
				c++;
				for (int j = 0; j < k; ++j) {
					if (i+j<s.size()){
						if (s[i+j]=='+')
							s[i+j]='-';
						else
							s[i+j]='+';
					} else
						f=0;
				}
			}
		}
		printf("Case #%d: ",ti+1);
		if (f)
			printf("%d\n",c);
		else
			printf("IMPOSSIBLE\n");
	}
	
	
	return 0;
}