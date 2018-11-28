           
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
//#define PI acos(-1.0)



int main()
{	
    freopen("in","r",stdin);
    freopen("out","w",stdout);
		
	int T;
	cin>>T;
	for(int qqq = 1;qqq<=T;qqq++)
	{
		int AC,AJ;cin>>AC>>AJ;
		
		int data[1440] = {0,};
		vector<  pair<pair<int,int>, int> > points; 
		int sum1=0;
		int sum2=0;
		for(int i=0;i<AC;i++)
		{
			int a,b;
			cin>>a>>b;b--;
			for(int j=a;j<=b;j++)
			{
				data[j] = 2;
				sum2++;
			}
			pair<int,int> x = {a,b};
			points.push_back({x,2});
		}
		for(int i=0;i<AJ;i++)
		{
			int a,b;
			cin>>a>>b;b--;
			for(int j=a;j<=b;j++)
			{
				data[j] = 1;
				sum1++;
			}
			pair<int,int> x = {a,b};
			points.push_back({x,1});
		}
		
		sort(points.begin(),points.end());
		int len = points.size();
		
		vector< int > first;
		vector< int > second;
		vector< int > both;
		
		for(int i=0;i<len-1;i++)
		{
			if(points[i].second != points[i+1].second)
			{
				both.push_back(points[i+1].first.first - points[i].first.second - 1);
			}else if(points[i].second == 1){
				first.push_back(points[i+1].first.first - points[i].first.second - 1);
			}else {
				second.push_back(points[i+1].first.first - points[i].first.second - 1);
			}
		}
		
		if(points[len-1].second != points[0].second)
		{
			both.push_back(1439 - points[len-1].first.second + points[0].first.first);
		}else if(points[len-1].second == 1){
			first.push_back(1439 - points[len-1].first.second + points[0].first.first);
		}else {
			second.push_back(1439 - points[len-1].first.second + points[0].first.first);
		}
		
		sort(first.begin(),first.end());
		sort(second.begin(),second.end());
		sort(both.begin(),both.end());
		
		int sumFirst = 0;for(int i=0;i<first.size();i++)sumFirst+=first[i];
		int sumSecond = 0;for(int i=0;i<second.size();i++)sumSecond+=second[i];
		int sumBoth = 0;for(int i=0;i<both.size();i++)sumBoth+=both[i];
		int answer = both.size();
		
		
		if(sum1+sumFirst+sumBoth<720)
		{
			int sum = sum1+sumFirst+sumBoth;
			for(int i = second.size()-1;i>=0;i--)
			{
				answer+=2;
				sum += second[i];
				if(sum>=720)break;
			}
		}else if(sum2+sumSecond+sumBoth<720)
		{
			int sum = sum2+sumSecond+sumBoth;
			for(int i = first.size()-1;i>=0;i--)
			{
				answer+=2;
				sum += first[i];
				if(sum>=720)break;
			}
		}		
		
		
		printf("Case #%d: %d\n",qqq,answer);
		
		//cout<<1<<sum1<<" "<<sumFirst<<" "<<sumBoth<<endl;
		//cout<<2<<sum2<<" "<<sumSecond<<" "<<sumBoth<<endl;
		

	}
	
    return 0;
}





        