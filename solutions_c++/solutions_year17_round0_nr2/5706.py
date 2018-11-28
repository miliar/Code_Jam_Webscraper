#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,haveChanged,step;
	string num;
	cin >> T;
	for (int testCase = 1; testCase <= T;++testCase){
		cin >> num;
		haveChanged = num.size();
		step =1;
		for (int i = 0; i < num.size(); i+=step){
			if (haveChanged<=i) num[i] = '9';
			
			if (i==num.size()-1) continue;
			
			if (num[i] <= num[i+1] || haveChanged <=i+1) step = 1;
			else {
				num[i]-=1;
				haveChanged = i+1;
				if (i!=0)step = -1;else step = 1;
			}
		}
		printf("Case #%d: ",testCase);
		for (int i = 0; i < num.size();++i){
			if (num[i] != '0') printf("%c",num[i]);
		}
		printf("\n");
	}
	return 0;
}
