#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mk make_pair
#define vi vector<int>
using namespace std;
typedef pair<int, int> pii;
vi a;
int T;
long long n;
void tran(){
	a.clear();
	do{
		a.pb(n%10);
		n/=10;
	}while(n);
	reverse(a.begin(), a.end());
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%lld", &n);
		tran();
		printf("Case #%d: ", cas);
		for(int i=1; i<(int)a.size(); i++){
			if(a[i]<a[i-1]){
				int at=i;
				while(at>0&&a[at]<a[at-1]){
					a[at-1]--;
					a[at]=9;
					at--;
				}
				for(int j=i; j<(int)a.size(); j++)
					a[j]=9;
			}
		}
		int i;
		for(i=0; i<(int)a.size(); i++){
			if(a[i])break;
		}
		for(; i<(int)a.size(); i++)
			printf("%d", a[i]);
		puts("");
	}
	return 0;
}


