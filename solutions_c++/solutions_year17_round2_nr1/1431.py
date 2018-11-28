#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<math.h>
#include<map>
#include<stack>
#include<string.h>
#define STOP system("pause")
#define bits(num) __builtin_popcount(num)
#define CASE int t;scanf("%d",&t);while(t--)
#define ll long long int
#define lu unsigned long long
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
using namespace std;
int main()
{
	freopen("www.in","r",stdin);
	freopen("gcj_1b_a_out11.txt","w",stdout);
	int tno =1;
	CASE{
	    double k,n,d,s;
	    cin>>d>>n;
	    double myti = 0.0;
	    for(int i=0;i<n;i++)
		{
	      cin>>k>>s;
	      double ti = (d-k)/s;
	      myti = max(myti, ti);
	    }
	    double res = (d/myti);
	    printf("Case #%d: %.6f\n",tno++,res );
	  }
    return 0;
}

