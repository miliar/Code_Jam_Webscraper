#include <bits/stdc++.h>
#define ll long long
#define INF 1000000005
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

typedef pair<int,int>P;

const int MAX_N = 20;

int T,ch;
bool flag;
string s;
int a[MAX_N];

int main()
{
	scanf("%d",&T);
	rep(t,T){
		cin >> s;
		rep(i,s.length()){
			a[i] = (int)(s[i] - '0');
		}
		ch = -1;
		rep(i,s.length()-1){
			if(a[i] > a[i+1]){
				ch = i;
				break;
			}
		}
		if(ch < 0){
			printf("Case #%d: ",t+1);
			rep(i,s.length()){
				printf("%d",a[i]);
			}
			printf("\n");
		}else{
			for(int i=ch+1;i<s.length();i++){
				a[i] = 9;
			}
			if(a[ch] == a[0]){
				if(a[0] == 1){
					printf("Case #%d: ",t+1);
					rep(i,s.length()-1){
						printf("9");
					}	
					printf("\n");
				}else{
					printf("Case #%d: %d",t+1,a[0]-1);
					for(int i=1;i<s.length();i++){
						printf("9");
					}	
					printf("\n");
				}
			}else{
				for(int i=ch;i>=0;i--){
					a[i]--;
					if(a[i-1] <= a[i]){
						break;
					}
				}
				printf("Case #%d: ",t+1);
				rep(i,s.length()){
					printf("%d",a[i]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
