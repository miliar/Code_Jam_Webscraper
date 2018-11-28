/* ***********************************************
Author :111qqz
Created Time :2017年04月09日 星期日 00时41分55秒
File Name :code/gcj2017/quaB.cpp
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
const double epsoutB = 1E-8;
const int dx4[4]={1,0,0,-1};
const int dy4[4]={0,-1,1,0};
const int inf = 0x3f3f3f3f;
char st[24];
int a[24];
int len;
void pr(int *arr)
{
    for ( int i = 1 ; i <= len ; i++) printf("%d ",arr[i]);
    printf("\n");
}
    
int main()
{
	#ifndef  ONLINE_JUDGE 
	freopen("code/in.txt","r",stdin);
	freopen("outBL.txt","w",stdout);
  #endif
	int T;
	int cas = 0 ;
	cin>>T;
	while(T--)
	{
	    scanf("%s",st);
	    len = strlen(st);
	    ms(a,0);
	    for ( int i = len-1 ; i >= 0 ; i--)
	    {
		int val = st[i]-'0';
		a[i+1] = val;
	    }
//	    pr(a);
	    bool sad = false;
	    for ( int i = 1 ; i <= len-1 ; i++)
	    {
		if (sad)
		{
		    a[i] = 9;
		    continue;
		}
		if (a[i+1]<a[i])
		{
		    a[i]--;
		    a[i+1] = 9;
		    int cur = i-1 ;
		    while (cur>=1&&a[cur]>a[cur+1])
		    {
			a[cur+1] = 9;
			a[cur]--;
			cur--;
		    }

		    sad = true;
		}
	    }
	    if (sad) a[len] = 9;
	    printf("Case #%d: ",++cas);
	    bool zero = false;
	    for ( int i = 1 ; i <= len ; i++)
	    {
		if (a[i]!=0) zero = true;
		if (zero||a[i]!=0) printf("%d",a[i]);
	    }
	    printf("\n");
		
 
	}


  #ifndef ONLINE_JUDGE  
  fclose(stdin);
  #endif
    return 0;
}
