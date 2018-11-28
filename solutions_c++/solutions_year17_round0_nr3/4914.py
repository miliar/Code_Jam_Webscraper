// Author : Muhammad Rifayat Samee
// Problem : C
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
struct Node{
    int id;
    int l;
    int h;
    int leftmax;
    int rightmax;
    int f;
}tree[2200005];
int n,K,f;
int A[1000005];

void do_it(int i,int l,int h,int w){
    //if(w == 1)
    //    printf("%d %d %d\n",i,l,h);
    int mid = (h+l)/2;
    if (tree[i].f == 0){

        tree[2*i].l = l;
        tree[2*i].h = mid-1;
        tree[2*i+1].l = mid+1;
        tree[2*i+1].h = h;
        tree[i].f = 1;
        tree[2*i].f = 0;
        tree[2*i+1].f = 0;
        tree[i].leftmax = tree[2*i].h-tree[2*i].l + 1;
        tree[i].rightmax = tree[2*i+1].h-tree[2*i+1].l + 1;
        f = i;
        return;
    }
    if(tree[i].leftmax>=tree[i].rightmax){
        do_it(2*i,l,mid-1,w);
        tree[i].leftmax = max(tree[2*i].leftmax,tree[2*i].rightmax);

    }
    else{
        do_it(2*i+1,mid+1,h,w);
        tree[i].rightmax = max(tree[2*i+1].leftmax,tree[2*i+1].rightmax);
    }



}

int main(){

	freopen("C_s2.in","r",stdin);
	//freopen("C_s2.out","w",stdout);
    int cases,i,j,p,k,in,L,R,ct=1;

    scanf("%d",&cases);
    while(cases--){
        scanf("%d %d",&n,&K);
        memset(A,0,sizeof(A));
        tree[1].id = 1;
        tree[1].f = 0;
        tree[1].l = 1;
        tree[1].h = n;
        for(i=0;i<K;i++){
            do_it(1,1,n,i);
            //printf("%d %d\n",tree[f].l,tree[f].h);
        }
        int wh = (tree[f].l+tree[f].h)/2;
        int l = wh - tree[f].l;
        int h = tree[f].h - wh;
        printf("Case #%d: %d %d\n",ct++,max(l,h),min(l,h));
    }

	return 0;
}
