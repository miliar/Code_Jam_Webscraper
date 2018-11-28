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
	cin>>T; getchar();
	for(int casenum = 1; casenum<=T; casenum++){
		string str;
		getline(cin, str);
		char prev = str[0];
		int i = 1;
		int same = 0;
		while(i<str.length() && str[i]>=prev){
			if(str[i]==prev) same++;
			else same = 0;
			prev = str[i];
			i++;
		}

		string sol;
		if(i<str.length()){
			char cur = str[i];
			sol = str.substr(0,i-same);
		//	cout<<i-same<<"f"<<sol<<endl;
			sol[i-same-1] = str[i-same-1]-1;
			int left = str.length()-sol.length();
			for(int j = 0; j<left; j++){
				sol+='9';
			}
		//	cout<<str<<endl;
		}
		else sol = str;
	//	cout<<sol<<endl;
		if((int)sol[0]<=(int)'0') sol = sol.substr(1,sol.length()-1);
		printf("Case #%d: %s\n", casenum, sol.c_str());

	}
	return 0;
}