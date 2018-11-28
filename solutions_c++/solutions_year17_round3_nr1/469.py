           
//g++ -std=c++11 -Wl,--stack,268435456 test.cpp -o test

//fc in1 in2        //file compare
#include <iostream>
using std::cin;
using std::cout;
using std::string;
using std::endl;
// string s;while(getline(cin,s));



#include <algorithm>
using std::sort;
using std::min;
using std::max;
using std::pair;//pair <int,int> data[100];sort(data,data+100);

#include <math.h>
//sqrt(123.123)
//ceil(0.12)=1
//pow(x,2)=x^2

#include<cstdio>
//printf()
// %I64d for long long 

#include <map>
using std::map;

#include <stdlib.h>
//abs(-123);

#include <vector>
using std::vector;

#include <queue>
using std::queue;

#include <deque>
using std::deque;

#include <stack>
using std::stack;

#include <set>
using std::set;
using std::multiset;

/*
long long gcd(long long a, long long b)
{
    //O(log(max(a,b)))
    long long t;
    while(b!=0)
    {
        t=a%b;
        a=b;
        b=t;
    }
    return a;
}
*/



/*
long long C(int x,int y)
{
    if(x<y){
        return 0;
    }
    long long answer=1;
    int i;
    if(y>x-y)
    {
        y=x-y;
    }
    for(i=1;i<=y;i++)
    {
        answer*=(x+1-i);
        answer/=i;
    }
    return answer;
}
*/




/*
//C(x,y) % mod
long long C(long long x,long long y)
{
    long long mod=1000000007;
    if(x<y){
        return 0;
    }
    long long answer=1;
    int i;
    if(y>x-y)
    {
        y=x-y;
    }
    for(i=1;i<=y;i++)
    {
        answer*=(x+1-i);
        answer%=mod;
    }
    for(i=1;i<=y;i++)
    {
        while(answer%i!=0){
            answer+=mod;
        }
        answer/=i;
        answer%=mod;
    }
    return answer%mod;
}


for (i=0; i<1010; i++) {
    c[i][0]=1;
    for (j=1; j<=i; j++) c[i][j]=(c[i-1][j-1]+c[i-1][j])%md;
}
*/

/*
//must return true if first>then second
struct classcomp {
    bool operator() (const int& lhs, const int& rhs) const{
        return lhs>rhs;
    }
};
*/


/*
int t;
string qwe;

vector<string> permutations;
void f(string s){
    if(s.size()==t){
        permutations.push_back(s);
        return;
    }
    int n=s.size();
    
    string x=qwe.substr(n,1);
    
    f(x+s);
    f(s+x);
    for(int i=1;i<n;i++){
        f(s.substr(0,i)+x+s.substr(i));
    }
}
*/
/*
struct Node
{
	int a;
	int b;
	int c;
	Node(int x,int y,int z):a(x),b(y),c(z)
	{
	}	
};
bool comp(Node& x, Node& y)
{
	return x.c<y.c;
}
*/

// index = (index + 1) % n; //index++; if (index >= n) index = 0;
// index = (index + n - 1) % n;// index--; if (index < 0) index = n - 1;
// int ans = (int)((double)d + 0.5);// for rounding to nearest integer


// Common memset settings
//memset(memo, -1, sizeof memo); // initialize DP memoization table with -1
//memset(arr, 0, sizeof arr); // to clear array of integers


#define PI acos(-1.0)
int main()
{	
    freopen("in","r",stdin);
    freopen("out","w",stdout);
	
	int T;
	cin>>T;
	for(int qqq = 1;qqq<=T;qqq++)
	{
		int N,K;cin>>N>>K;
		pair<long long ,long long> data[1001];
		for(int i=0;i<N;i++)
		{
			long long a,b;
			cin>>a>>b;
			data[i].first = -a;
			data[i].second = -2*b*a;
		}
		sort(data,data+N);
		
		long long answer = 0;
		for(int i=0;i+K<=N;i++)
		{
			long long R = -data[i].first;
			long long H = -data[i].second;
			vector<long long> height;
			
			
			for(int j=i+1;j<N;j++)
			{
				height.push_back(data[j].second);
			}
			sort(height.begin(),height.end());
			
			for(int i=0;i<K-1;i++)H-=height[i];
			answer = max(answer,R*R + H);
		}
		double curAnswer = PI*answer;
		printf("Case #%d: %.9f\n",qqq,curAnswer);
	}
	
    return 0;
}





        