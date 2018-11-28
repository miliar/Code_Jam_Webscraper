#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <tuple>
#include <math.h>

using namespace std;
/*
long findUL(long temp){
	vector<int> digits;
	while(temp>0){
		digits.push_back(temp%10);
		temp/=10;
	}

	long uLimit = 0;
	int i;
	for(i = 1; i < digits.size()+1; i++){
		if(i<digits.size()-1){
			if(digits[i]==0)
				digits[i-1]=9;
			else
			digits[i-1]=digits[i]-1;
		}
		uLimit+=digits[i-1]*pow(10,i-1);
	}
	return uLimit;
}
*/

bool checkNumber(long temp){
	vector<int> digits;
	while(temp>0){
		digits.push_back(temp%10);
		temp/=10;
	}
	for(int i = 0; i< digits.size()-1; i++){
		if(digits[i]<digits[i+1])
			return false;
	}
	return true;
}

long findTidy(long temp){
	vector<int> digits;
	long tidyT=0;
	while(temp>0){
		digits.push_back(temp%10);
		temp/=10;
	}
	int i=0;
	for(i = 0; i< digits.size()-1; i++){
		if(digits[i]<digits[i+1]){
			for(int j = i; j>=0; j--){
				digits[j]=9;
			}
			digits[i+1]=(digits[i+1]+9)%10;
		}
		/*for(auto c:digits)
			cout<<c<<" ";
		cout<<endl;*/
	}
	for(i = 0; i< digits.size(); i++){
		//cout<<tidyT<<" "<<digits[i]*pow(10,i)<<endl;
		tidyT+=(long)digits[i]*(long)pow(10,i);
	}
	return tidyT;
}
int main()

{
    freopen("B-large.in.txt","rt",stdin);
	freopen("B-large.out.txt","wt",stdout);
	cout.precision(18);
    int N;
    cin >> N;

    long T=0;
	for (int caseN = 1; caseN <= N; ++caseN) {
		cout << "Case #" << caseN << ": ";
		cin >> T;
		bool tidyT = checkNumber(T);	//precheck
		if(T>9 && tidyT==false){
			T=findTidy(T);
			tidyT = checkNumber(T);
		}
		cout<<T<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}
