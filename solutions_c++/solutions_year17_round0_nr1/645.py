#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;

int t;
string s;
int k;
int main(){
	cin>>t;
	int f = 1;
	while(t){
		printf("Case #%d: ", f);
		f++;
		cin>>s>>k;
		int n = (int)(s.size());
		int answ = 0;
		bool z = true;
		for(int i=0;i<n;i++){
			if(s[i] == '+') continue;
			answ++;
			if(i+k-1 >= n) {z = false; break;}
			for(int j=i;j<=i+k-1;j++){
				if(s[j] == '+') s[j] = '-'; 
				else s[j] = '+';
			}
		}
		if(z) cout<<answ<<endl;
		else cout<<"IMPOSSIBLE"<<endl; 
		t--;
	}

	return 0;
}