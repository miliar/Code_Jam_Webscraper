#include<bits/stdc++.h>
#define FOR(a,b,c) for(a=b;a<c;a++)
#define PI acos(-1)
using namespace std;
bool benar;
int n,t,tc,i,j,k,x,hasil;
string s;
int main(){
	scanf("%d",&tc);
	FOR(t,1,tc+1){
		hasil=0;
		benar=true;
		cin >> s >> k;
		n = s.length();
		FOR(i,0,n-k+1){
			if (s[i]=='-'){
				FOR(j,i,i+k){
					if (s[j]=='-') s[j]='+';
					else s[j]='-';
				}
				hasil++;
			}
		}
		printf("Case #%d: ",t);
		FOR(i,0,n) if (s[i]=='-') benar=false;
		if (!benar) puts("IMPOSSIBLE");
		else printf("%d\n",hasil);
	}
}

