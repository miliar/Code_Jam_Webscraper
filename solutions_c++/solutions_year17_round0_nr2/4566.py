#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define pb push_back
#define vint vector<int>

int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt", "w", stdout);
	string s;
	int t,i,j,k,l,m,n,x,y;
	sd(t);
	for(x=1;x<=t;x++){
		cin>>s;
		l = s.size();
		for(k=0;k<l;k++){
			for(i=0;i<l-1;i++){
				if(s[i]>s[i+1]){
					s[i]--;
					for(j=i+1;j<l;j++)
						s[j]='9';
					break;
				}
			}
		}
		printf("Case #%d: ",x);
		for(i=0;i<l;i++){
			if(i>0 || s[i]!='0')
				printf("%c",s[i]);
		}
		printf("\n");
	}
	return 0;
}