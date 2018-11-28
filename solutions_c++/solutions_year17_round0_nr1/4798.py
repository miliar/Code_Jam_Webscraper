#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
#include <set>
#include <queue>
#include <sstream>
#include <stack>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int casenum = 1; casenum<=T; casenum++){
		string cakes;
		cin>>cakes;
		int k;
		cin>>k;
		int flips = 0;
		int i=0;
		while(i<cakes.length()){
		//	cout<<cakes<<i<<endl;
			while(i<cakes.length() && cakes[i] == '+') i++;
			if(i<=cakes.length()-k){
				flips++;;
				for(int j=0; j<k; j++){
					if(cakes[i+j] == '+') cakes[i+j] = '-';
					else cakes[i+j] = '+';
				}
				i++;
			}
			else break;
		}
		if(i<cakes.length()) printf("Case #%d: IMPOSSIBLE\n", casenum);
		else printf("Case #%d: %d\n", casenum, flips);
	}
	return 0;
}