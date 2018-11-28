//Sinha Saab
//NARUTO Fan



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

int n;
char a[20];

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("B-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int t,tc,i,j;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
    	scanf("%s",a);
    	n=strlen(a);
    	for(i=(n-2);i>=0;i--)
    	{
    		if(a[i]<=a[i+1])
    			continue;
    		for(j=(i+1);j<n;j++)
    			a[j]='9';
    		while(i>=0&&a[i]=='0')
    		{
    			a[i]='9';
    			i--;
    		}
    		a[i]-=1;
    	}
    	printf("Case #%d: ",tc);
    	i=0;
    	while(a[i]=='0')
    		i++;
    	for(;i<n;i++)
    		printf("%c",a[i]);
    	printf("\n");
    }
    return 0;
}