#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cstdio>
#include<stdlib.h>
#include<sstream>
#include<list>
#include<math.h>
#include<map>
#include<set>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<vector>
#include<algorithm>
#include <queue>
#include<string>
#include<cstring>
#include <deque>
#include<stack>
using namespace std;


#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define PB push_back
#define PI acos(-1.0)
#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
long long GCDFast(long long a,long long b){   while(b)b^=a^=b^=a%=b;  return a;   }
#define SET(a) memset(a,-1,sizeof(a))
#define ALL_BITS ((1 << 31) - 1)
#define NEG_BITS(mask) (mask ^= ALL_BITS)
#define TEST_BIT(mask, i) (mask & (1 << i))
#define ON_BIT(mask, i) (mask |= (1 << i))
#define OFF_BIT(mask, i) (mask &= NEG_BITS(1 << i))
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define MOD 1000000007
#define MX 100010
#define pii pair<int,int>
#define LL long long
// UP, RIGHT, DOWN, LEFT, UPPER-RIGHT, LOWER-RIGHT, LOWER-LEFT, UPPER-LEFT
int dx[8] = {-1, 0, 1, 0, -1, 1,  1, -1};
int dy[8] = { 0, 1, 0,-1,  1, 1, -1, -1};

long long GCD(long long b, long long a)
{
	if(a == 0)
		return b;
	return GCD(a, b%a);
}
long long getLCM(long long a,long long b){
	long long c=a/GCD(a,b);
	return b*c;
}
map<LL,int>mymap;
map<LL,int>::iterator it;
vector<LL>results;

int main() {
	freopen ("d:/Codejam/A-large.in","r",stdin);
	freopen ("d:/Codejam/output.txt","w",stdout);
	LL n,i,j,k,temp,m;
	LL x,y,z,sum,length,ans,test,l,w,num;
	string str, str1;
	
	int X[10005],test_case=0;
	i=1;
	cin>>test;
	while(test--){
		cin>>str;
		cin>>k;
		printf("Case #%d: ",++test_case);
		n = str.size();
		x = 0;
		for(i=0;i<n;i++){
			if(str[i] == '-'){
				if(i+k>n)
					break;
				x++;
				for(j=i,l=0; l<k && j<n ;l++,j++){
				if(str[j] == '-')
					str[j] = '+';
				else
					str[j] = '-';
				}

			}
		}
		int flag = 1;
		for(i=0 ;i < n;i++){
			if(str[i] == '-'){
				flag = 0;
			break;
			}
		}
		if(flag)
			cout<<x<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
	
	return 0;
}