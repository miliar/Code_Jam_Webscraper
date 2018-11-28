//============================================================================
// Name        : Tidy.cpp
// Author      : Fezo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;
int T,N;
bool isTidy(int x){
	string number="",sortedNumber="";
	while(x){
		number+=char(x%10 + '0');
		x/=10;
	}
	if(number[0]=='0') return false;
	reverse(number.begin(),number.end());
	sortedNumber = number;
	sort(sortedNumber.begin(),sortedNumber.end());
	//cout << sortedNumber << " " << number << endl;
	return sortedNumber==number;
}
int main() {
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int t = 1;
	cin >>T;
	while(T--){
		cin >>N;
		while(!isTidy(N)){
			N--;
		}
		cout << "Case #" << t <<": " << N << endl;
		t++;
	}
	return 0;
}
