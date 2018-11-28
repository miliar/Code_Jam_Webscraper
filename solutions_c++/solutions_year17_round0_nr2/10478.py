#include <bits/stdc++.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
bool ascend (int n){
	string s,sx;
	s=to_string(n);
	sx=s;
	sort(s.begin(),s.end());
	if(s==sx)return true;
	else return false;
	
}
int main() {
	ios_base::sync_with_stdio(false);
	int a,t;
	
	cin>>t;
	for(int i=0;i < t;i++){
		cin>>a;
		while(!ascend(a)){a--;}
	cout<<"Case #"<<i+1<<": "<<a<<endl;
	}
	
	return 0;
}
