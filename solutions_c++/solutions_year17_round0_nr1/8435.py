#include <bits/stdc++.h>
using namespace std;

struct tipe{
	string str;
	int jar;
};

string str,str2,str1,s;
map<string,bool> f;
int jar,t,n,hasil;
queue<tipe> q;
tipe q1;

int bfs(string s){
	q1.jar=0; q1.str=s;
	f[s]=true;
	while (!q.empty()) q.pop();
	q.push(q1);
	str2.clear();
	f.clear();
	for (int i=0; i<s.length(); i++) str2+='+';
	while (!q.empty()){
		jar=q.front().jar;
		str=q.front().str;
		q.pop();
		if (str==str2) return jar;
			for (int j=0; j<=s.length(); j++){
				str1=str;
				if (j+n-1>=s.length()) break;
				for (int k=j; k<=j+n-1; k++){
					if (str[k]=='-') str1[k]='+';
					else str1[k]='-';
				}
				q1.jar=jar+1;
				q1.str=str1;
				if (!f[str1]){
					f[str1]=true;
					q.push(q1);
				}
			}
	}
	return -1;
}
int main(){
	scanf("%d",&t);
	for (int i=1; i<=t; i++){
		cin>>s>>n;
		hasil=bfs(s);
		if (hasil==-1) printf("Case #%d: IMPOSSIBLE\n",i);
		else printf("Case #%d: %d\n",i,hasil);
	}
	return 0;
}
