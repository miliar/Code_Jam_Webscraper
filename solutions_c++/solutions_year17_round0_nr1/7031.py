/* ***********************************************
Author :111qqz
Created Time :2017年04月08日 星期六 20时13分42秒
File Name :code/gcj2017/quaA.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define PB push_back
#define fst first
#define sec second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define ms(a,x) memset(a,x,sizeof(a))
typedef long long LL;
#define pi pair < int ,int >
#define MP make_pair

using namespace std;
const double eps = 1E-8;
const int dx4[4]={1,0,0,-1};
const int dy4[4]={0,-1,1,0};
const int inf = 0x3f3f3f3f;
const int N=1E3+7;
char st[N];
int sum[N];
int a[N],f[N]; //f[i]表示区间 f[i,i+l-1]是否需要翻转
int k;
int len;
void pr(int * a)
{
    for ( int i = 1; i <= len ; i++ ) printf("%d ",a[i]);
    printf("\n");
}
int main()
{
	#ifndef  ONLINE_JUDGE 
	
    freopen("outtt.txt","w",stdout);
	freopen("code/in.txt","r",stdin);
  #endif
	int T;
	cin>>T;
	int cas = 0 ;
	while (T--)
	{
	    scanf("%s %d",st,&k);
	    len = strlen(st);
	    sum[0] = 0 ;
	    ms(a,0);
	    ms(f,0);
	    ms(sum,0);
	    int l,r;
	    int cnt = 0;
	    for ( int i = 0 ; i < len ; i++)
	    {
		if (st[i]=='+') a[i+1] = 1;
		else a[i+1] = 0 ;
	    }
//	    pr(a);
	    for ( int i = 1 ; i <= len-k+1 ; i++)
	    {
		r = i-1;
		l = i-k;
		l = max(0,l);

		int cur = sum[r]-sum[l];
		if (cur%2) a[i] = 1 - a[i];
		if (a[i]==0)
		{
		    a[i] = 1;
	//	    cout<<"rol:"<<i<<endl;
		    f[i] = 1;
		    cnt++;
		}

//		pr(a);
		sum[i] = sum[i-1] + f[i];
	    }
	    bool ok = true;
//	 cout<<"sum:"<<endl;   pr(sum);
	    for ( int i = len-k+2 ; i <= len ; i++)
	    {
		sum[i] = sum[i-1]; //忘记了 T T 
		r = i-1;
		l = i-k;
		l = max(0,l);
		int cur = sum[r] - sum[l];
	//	cout<<"i:"<<i<<" cur:"<<cur<<endl;
		if (cur%2) a[i] = 1 - a[i];
		if (a[i]==0)
		{
		    ok = false;
		    break;
		}
		
	    }
//	    pr(a);
	    if (ok)
	    {
		printf("Case #%d: %d\n",++cas,cnt);
	    }
	    else
	    {
		printf("Case #%d: IMPOSSIBLE\n",++cas);
	    }
	}

  #ifndef ONLINE_JUDGE  
  fclose(stdin);
  #endif
    return 0;
}
