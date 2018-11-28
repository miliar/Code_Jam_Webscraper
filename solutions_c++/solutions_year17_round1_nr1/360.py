#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define size(t) ((int)(t.size())) 


int t,q = 1;
char a[102][102];
int main(){
	scanf("%d", &t);
	while(t){
		printf("Case #%d:", q);
		cout<<endl;
		int n,m;
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				cin>>a[i][j];
			}
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				if(j!=0 && a[i][j] == '?') a[i][j] = a[i][j-1];
			}
		for(int i=0;i<n;i++){
			for(int j = m-1;j>=0;j--){
				if(j!=m-1 && a[i][j] == '?') a[i][j] = a[i][j+1];
			}
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				if(a[i][j] == '?' && i!=0) a[i][j] = a[i-1][j]; 
			}
		for(int i=n-1;i>=0;i--)
			for(int j=0;j<m;j++){
				if(a[i][j] == '?' && i!=n-1) a[i][j] = a[i+1][j];
			}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) cout<<a[i][j];
			cout<<endl;
		}

		t--;
		q++;
	}
	return 0;
}