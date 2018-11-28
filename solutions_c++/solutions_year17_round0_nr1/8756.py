#include <iostream>
using namespace std;

int solution=0;
int p;

void back(string s, int k, string q, int t){
	if (s==q) p=1;
	if (p==0 and s.size()-k>=t){
	if (s[t]=='-'){
	for (int i=t; i<t+k; i++){
			if (s[i]=='-') s[i]='+';
			else s[i]='-';
	}
	solution++;
	back(s,k,q,t+1);
}
else back (s,k,q,t+1);
}
return;
}

int main(){
	int n;
	while (cin>>n){
		for(int i=1; i<=n; i++){
			string s;
			int k; 
			solution=0;
			p=0;
			cin>>s>>k;
			string perfect (s.size(), '+');
			back (s,k,perfect,0);
			if (p==1) cout<<"Case #"<<i<<": "<<solution<<endl;
			else cout<<"Case #"<<i<<": " <<"IMPOSSIBLE"<<endl;
}
}
}
