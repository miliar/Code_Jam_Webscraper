#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;
const int N = 1000005;

string number;

void init(){

	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		cin >> number;	
	int len = number.length();
	for (int i =len -2; i >-1; i--)
	{		
		if(number[i]>number[i+1]){
			for (int j = i+1; j < len; ++j)
			{
				number[j]='9';
			}
			number[i]--;
			
		}
	}
	cout << "Case #"<<t<<": ";
	if(number[0]=='0'){
		for (int i = 1; i < len; ++i)
		{
			cout << number[i];
		}
		cout<< endl;
	}
	else{
		cout << number << endl;
	}
	}
	
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	init();
	return 0;
}