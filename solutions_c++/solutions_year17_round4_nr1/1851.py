#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

const int N = 102;
int arr2[N][N];
int arr3[N][N][N];
int arr4[N][N][N][N];
void precomp(){
	// Pieces = 2
	arr2[0][0] = 0;
	for(int i=0;i<=100;i++)
	for(int j=0;j<=100;j++){
		if(i+j==0 || (i+j)>100)continue;
		arr2[i][j] = 0;
		if(i!=0){
			arr2[i][j] = (arr2[i-1][j]+1);
		} else if(j!=0){
			if(j>=2)  arr2[i][j] = (arr2[i][j-2]+1);
		}
	}
	// Pieces = 3
	arr3[0][0][0] = 0;
	for(int i=0;i<=100;i++)
	for(int j=0;j<=(100-i);j++)
	for(int k=0;k<=(100-i-j);k++){
		if(i+j+k==0 || (i+j+k)>100)continue;
		arr3[i][j][k] = 0;
		if(i!=0){
			arr3[i][j][k] = (arr3[i-1][j][k]+1);
		} else if(j!=0){
			if(j>=3) arr3[i][j][k] = max(arr3[i][j][k], arr3[i][j-3][k]+1);
			if(k>=1 && j>=1) arr3[i][j][k] = max(arr3[i][j][k], arr3[i][j-1][k-1]+1);
		} else if(k!=0){
			if(k>=3)
				arr3[i][j][k] = arr3[i][j][k-3]+1; 
		}
	}
	// Pieces = 4
	arr4[0][0][0][0] = 0;
	for(int i=0;i<=100;i++)
	for(int j=0;j<=(100-i);j++)
	for(int k=0;k<=(100-i-j);k++)
	for(int l=0;l<=(100-i-j-k);l++){
		if(i+j+k+l==0 || (i+j+k+l)>100)continue;
		arr4[i][j][k][l] = 0;
		if(i!=0){
			arr4[i][j][k][l] = (arr4[i-1][j][k][l]+1);
		} else if(j!=0){
			if(j>=4) arr4[i][j][k][l] = max(arr4[i][j][k][l], arr4[i][j-4][k][l]+1);
			if(j>=2 && k>=1) arr4[i][j][k][l] = max(arr4[i][j][k][l], arr4[i][j-2][k-1][l]+1);
			if(j>=1 && l>=1) arr4[i][j][k][l] = max(arr4[i][j][k][l], arr4[i][j-1][k][l-1]+1);
		} else if(k!=0){
			if(k>=2) arr4[i][j][k][l] = max(arr4[i][j][k][l], arr4[i][j][k-2][l]+1);
			if(k>=1 && l>=2) arr4[i][j][k][l] = max(arr4[i][j][k][l], arr4[i][j][k-1][l-2]);
		} else if(l!=0) {
			if(l>=4) arr4[i][j][k][l] = arr4[i][j][k][l-4];
		}
	}
}
int solve(){
	int n,p,v,sm=0;
	s(n);s(p);
	int arr[4]={0};
	for(int i=0;i<n;i++){
		s(v);
		sm += v;
		arr[v%p]++;
	}
	if(p==2)
		return arr2[arr[0]][arr[1]] + ((sm%p==0)?0:1);
	if(p==3)
		return arr3[arr[0]][arr[1]][arr[2]] + ((sm%p==0)?0:1);
	if(p==4)
		return arr4[arr[0]][arr[1]][arr[2]][arr[3]] + ((sm%p==0)?0:1);
	return 0;
}
int main()
{
	precomp();
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: ",tt+1);
		cout<<solve();
		printf("\n");
	}
    return 0;
}
