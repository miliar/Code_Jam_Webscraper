#include <bits/stdc++.h>

#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

#define pd(n) printf("%d\n",n)
#define pld(n) printf("%lld\n",n)

#define test int t; sd(t);while(t--)
#define MAXI (int)1e6 + 1

typedef long long ll;


using namespace std;

char grid[25][25];
int n,m;
int fill(int in){
	int flag=0;char first;

	for(int i=0;i<m;i++){
		if(grid[in][i]!='?'){
			flag=1;
			first=grid[in][i];
			break;
		}
	}
	if(flag==0)return -1;

	for(int i=0;i<m;i++){
		if(grid[in][i]!='?')first=grid[in][i];

		grid[in][i]=first;
	}

	return 1;

}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);

	int z=1;
	test{
		printf("Case #%d:\n",z++);
		sd(n);sd(m);

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++)cin >> grid[i][j];
		}

		int index=0;
		while(fill(index)==-1){
			index++;
		}

		for(int i=index-1;i>=0;i--){
			for(int j=0;j<m;j++){
				grid[i][j]=grid[i+1][j];
			}
		}

		for(int i=index+1;i<n;i++){
			if(fill(i)==1)continue;

			for(int j=0;j<m;j++)grid[i][j]=grid[i-1][j];
		}

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout << grid[i][j];
			}
			cout << endl;
		}

	}
}
