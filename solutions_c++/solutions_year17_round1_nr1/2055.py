#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define scan(x) scanf("%d",&x)
#define scanll(y) scanf("%lld",&y)
#define print(x) printf("%d\n",x)
#define printll(y) printf("%lld\n",y)

typedef pair<int,int>pii;
const int maxn=30;

int r,c;
char a[maxn][maxn];

int main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t;
	scan(t);
	for(int tc=1 ; tc<=t ; tc++) {
		scan(r); scan(c);
		for(int i=0 ; i<r ; i++) {
			for(int j=0 ; j<c ; j++) {
				cin>>a[i][j];
			}
		}
		for(int i=0 ; i<r ; i++) {
			for(int j=0 ; j<c ; j++) {
				if(a[i][j]=='?')
					continue;
				for(int k=j-1 ; k>=0 ; k--) {
					if(a[i][k]=='?') {
						a[i][k]=a[i][j];
					}
					else {
						break;
					}
				}
				for(int k=j+1 ; k<c ; k++) {
					if(a[i][k]=='?') {
						a[i][k]=a[i][j];
					}
					else {
						break;
					}
				}
			}
		}
		for(int i=0 ; i<r-1 ; i++) {
			for(int j=0 ; j<c ; j++) {
				if(a[i][j]!='?' && a[i+1][j]=='?') {
					a[i+1][j]=a[i][j];
				}
			}
		}
		for(int i=r-1 ; i>0 ; i--) {
			for(int j=0 ; j<c ; j++) {
				if(a[i][j]!='?' && a[i-1][j]=='?') {
					a[i-1][j]=a[i][j];
				}
			}
		}
		cout<<"Case #"<<tc<<":\n";
		for(int i=0 ; i<r ; i++) {
			for(int j=0 ; j<c ; j++) {
				cout<<a[i][j];
			}
			cout<<"\n";
		}
	}	
}