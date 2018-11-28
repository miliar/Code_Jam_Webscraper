#include<bits/stdc++.h>
#define FOR(a,b,c) for(a=b;a<c;a++)
#define PI acos(-1)
using namespace std;
string s,s2;
int t,tc,n,i,j,pos1,pos2,maxi;
bool benar;
int main()
{
	scanf("%d",&tc);
	FOR(t,1,tc+1){
		printf("Case #%d: ",t);
		benar = true;
		cin >> s;
		s2 = "";
		n = s.length();
		FOR(i,1,n)
			if (s[i]<s[i-1]) benar=false;
		if (benar) cout<<s<<endl;
		else{
			while(!benar){
				pos1 = 0;
				pos2 = 0;
				FOR(i,1,n){
					if (s[i]>s[i-1]) pos1=i;
					else if (s[i]==s[i-1]) continue;
					else{
						FOR(j,0,pos1) s2=s2+s[j];
						s[pos1]=s[pos1]-1;
						s2=s2+s[pos1];
						FOR(j,pos1+1,n) s2=s2+"9";
						break;
					}
				}
				while (s2[0]=='0') s2.erase(0,1);
				benar=true;
			}
			cout<<s2<<endl;
		}
	}
}
	
