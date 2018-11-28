           
//g++ -std=c++11 -Wl,--stack,268435456 test.cpp -o test

#include <iostream>
using std::cin;
using std::cout;
using std::string;
//using std::to_string; //convert number to string
using std::endl;

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

int main()
{
	/*
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    */
	
	freopen("in","r",stdin);
    freopen("out","w",stdout);
	
	int T;cin>>T;
	for(int ttt = 1; ttt <= T; ttt++)
	{
		int N,Q;cin>>N>>Q;
		int E[100] = {0,};
		int S[100] = {0,};
		for(int i=0;i<N;i++)
		{
			cin>>E[i]>>S[i];
		}
		
		int D[100][100]= {0,};
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				cin>>D[i][j];
			}
		}
		
		int Uk,Vk; cin>>Uk>>Vk; Uk--;Vk--;
		
		double CanGoTo[100][100];
		for(int i=0;i<10000;i++)CanGoTo[i/100][i%100] = -1;
		for(int i=0;i<100;i++)CanGoTo[i][i] = 0;
		
		for(int i=0;i<N-1;i++)
		{
			double totalTime = 0;
			int speed = S[i];
			int dist = E[i];
			for(int j=i;j<N-1;j++)
			{
				dist -= D[j][j+1];
				if(dist>=0)
				{
					totalTime = ((double)(E[i] - dist)) / speed;
					CanGoTo[i][j+1] = totalTime;
				}else{
					break;
				}
			}
		}
		

		
		
		double d[100];
		for(int i=0;i<100;i++)d[i] =-1;
		d[0] = 0;
		
		d[1] = CanGoTo[0][1];
		for(int too = 2;too < N;too++)
		{
			for(int from=0;from<too;from++)
			{
				if(CanGoTo[from][too]==-1){
					continue;
				}
				
				if(d[too] == -1)
				{
					d[too] = CanGoTo[from][too] + d[from];
				}else{
					d[too] = min(d[too],CanGoTo[from][too] + d[from]);
				}
			}
		}
		
		
		
		cout<<"Case #"<<ttt<<": ";
		printf("%.9f\n",d[N-1]);
		
	}

	
	

    return 0;
}





        