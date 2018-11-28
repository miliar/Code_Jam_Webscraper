
#include<cstdio>
#include<iostream>
#include<stack>
#include<cstring>
#include<cstdlib>
#include<climits>
#include<algorithm>
#include<queue>
#include<vector>
#include<list>
#include<utility>
#include<sstream>
#include<cmath>
#include<set>
#include<map>
 
using namespace std;
 
#define gc getchar_unlocked
#define pc putchar_unlocked
#define loop(a,b,c) for(int a=b;a<c;a++)
#define rev_loop(a,c,b) for(int a=c;a>=b;a--)
#define f first
#define s second
#define mp make_pair
#define l64 long long int
#define u64 unsigned long long 
#define nmax 100009

int arr[nmax];

static inline int input()
{
	register int temp = 0;
    char c;
	while(c<'0'||c>'9')c = gc();
	while(c>='0'&&c<='9')
	{
		temp = (temp<<1) + (temp<<3) + c-'0';
		c = gc();
	}
	return temp;
}

bool jam_func(long long int n)
{
	long long int arr[20],k=0,i,j;
	long long int brr[20],m=0;
	while(n>0)
	{
		arr[k++]=n%10;
		brr[m++]=n%10;
		n/=10;
	}
    sort(arr,arr+k);
    bool flag = true;
    for(i=k-1,j=0;i>=0,j<k;i--,j++)
    {
    	//printf("%lld ",arr[j]);
    	if(arr[i]!=brr[j])
    	{
    		break;
    	}
    }
    if(j==k)
    	return true;
    return false;
}

int main()
{
	int t,d=0;
	scanf("%d",&t);
	while(t--)
	{
		d++;
		long long int a,temp;
		scanf("%lld",&a);
		for(long long int i=a;i>=1;i--)
		{
			if(jam_func(i))
			{
				temp = i;
				break;
			}
		}
		printf("Case #%d: %lld\n",d,temp);
	}
}