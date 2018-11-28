#include<iostream>
#include<string.h>
using namespace std;

void change(char& x){
	if(x == '+') x = '-';
	else x = '+';
}

bool check (char* s){
	for(unsigned int i = 0; i < strlen(s) ; i++)
		if(s[i] == '-') return 0; 
	return 1;
}

int flip (char* s, int k){
	int count = 0;
	for(unsigned int i = 0; i <= strlen(s) - k  ; i++){
		if(check(s))	return count;	
		if( s[i] == '-'){
			count++;
			for(unsigned int j = i; j < i + k ; j++)
				change(s[j]);
		}
	//	cout<<s<<endl;
	}
	//cout<<endl<<count<<endl;
	if(check(s))
		return count;
	else
		return -1;
}

int main(){
	int n;
	cin>>n;
	for(int i = 0 ; i < n ; i++){
		char test_case[1001];
		cin>>test_case;
		int k;
		cin>>k;
		int ans = flip(test_case, k);
		if(ans >= 0)
			cout<<"Case #"<<(i + 1)<<": "<< ans <<endl;
		else
			cout<<"Case #"<<(i + 1)<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}