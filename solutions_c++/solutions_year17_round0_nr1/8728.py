#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

char invert(char x){
	if (x == '+') return '-';
	if (x == '-') return '+';
	else return '0';
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin>>tt;
	for (int ttt=0; ttt<tt; ttt++){
		
		string s;
		
		int k;
		cin>>s>>k;
		int l = s.length();   //l=5   k=3
		int x = l-k;      /// x=2
		int count=0;
		bool b=true;
		while (x>=0){
			if (s[x+k-1]=='-'){
				count++;
				for (int i=0; i<k; i++){
						s[x+i]=invert(s[x+i]);
					}	
			}
			x--;
		}
		for (int i=0; i<k; i++){
			if (s[i]!='+') {b=false; break;}
		}	

		cout<<"Case #"<<ttt+1<<": ";
		if (b==false) cout<<"IMPOSSIBLE"<<endl;
		else cout<<count<<endl;
	}
}