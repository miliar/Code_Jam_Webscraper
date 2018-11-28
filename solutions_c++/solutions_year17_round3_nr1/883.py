#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
const double PI = acos(-1.0);
const double e = exp(1.0);
#define ll __int64
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
#define inf 0x7fffffff
using namespace std;
/*
一堆订单  k个煎饼
有n个,n>=k,  每个煎饼是圆柱体，  又不同的r 和h
从n个中选k个，按r从大到小堆起来

是暴漏在外面的面积最大

t
n k
ri  hi
...
rn hn


n=1000

我们想想n*n的dp

我们假设dp[i][j] :以i结尾的长度为j 的最大面积
  dp[i-1][j]
   假设现在以 i 结尾，那么 加上 i-1 罩住的面积 - （i-1的顶面，侧面） + i的顶面侧面，-i
.....
顶面积是固定的。。。 就是最大的r的面积
我们能改变的只有侧面积。 即我们要使 h 最高
 */

struct node{
	double h,r;
}f[1005];
bool cmp1(node a,node b){
	return a.r>b.r;
}
bool cmp2(node a,node b){
	return a.h*a.r>b.h*b.r;
}
int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int n,k;
    for(int cas=1;cas<=t;cas++){
    	printf("Case #%d: ",cas);
    	scanf("%d %d",&n,&k);
    	for(int i=1;i<=n;i++){
    		scanf("%lf %lf",&f[i].r,&f[i].h);
    	}
    	double ans=0;

    	for(int i=1;i<=n-k+1;i++){
    		sort(f+1,f+n+1,cmp1);
    		double cnt=0;
    		// 假设以i 为最底下
    		cnt+=PI*f[i].r*f[i].r;
    		sort(f+i+1,f+n+1,cmp2);
    		for(int j=i;j<=i+k-1;j++)
    			cnt+=2*PI*f[j].r*f[j].h;
    		ans=max(ans,cnt);
    	}
    	printf("%.10f\n",ans);
    }
    return 0;
}
