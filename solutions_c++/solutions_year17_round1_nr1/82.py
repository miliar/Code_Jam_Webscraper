#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

char A[30][30];

void solve(int p1) {
    printf("Case #%d:\n",p1);
    int r,s;
    scanf("%d %d",&r,&s);
    For(i,r) For(j,s) scanf(" %c",&A[i][j]);
    For(i,r) {
        For(j,s) {
            if(j!=0 && A[i][j]=='?' && A[i][j-1]!='?') A[i][j]=A[i][j-1];
        }
        for(int j=s-1; j>=0; j--) {
            if(j!=s-1 && A[i][j]=='?' && A[i][j+1]!='?') A[i][j]=A[i][j+1];
        }
    }
    For(i,r) {
        For(j,s) {
            if(i!=0 && A[i][j]=='?' && A[i-1][j]!='?') A[i][j]=A[i-1][j];
        }
    }
    for(int i=r-1; i>=0; i--) {
        For(j,s) {
            if(i!=r-1 && A[i][j]=='?' && A[i+1][j]!='?') A[i][j]=A[i+1][j];
        }
    }
    For(i,r) {For(j,s) printf("%c",A[i][j]); printf("\n");}
}

int main() {
    int t1;
    scanf("%d",&t1);
    For(i,t1) solve(i+1);
}
