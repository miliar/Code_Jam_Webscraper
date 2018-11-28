           
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
		int N,R,O,Y,G,B,V;
		cin>>N>>R>>O>>Y>>G>>B>>V;
		
		if( (B<O+1 && O>0) || (R<G+1 && G>0) ||(Y<V+1 && V>0) )
		{
			cout<<"Case #"<<ttt<<": ";
			if(B+O ==N)
			{
				for(int i=0;i<B;i++){
					cout<<"BO";
				}
			}else if(R+G==N){
				for(int i=0;i<R;i++){
					cout<<"RG";
				}
			}else if(Y+V==N){
				for(int i=0;i<Y;i++){
					cout<<"YV";
				}
			}
			else{
				cout<<"IMPOSSIBLE";
			}
			cout<<endl;
			continue;
		}
		string answerO="";
		string answerG="";
		string answerV="";
		
		int flagO=0;
		int flagG=0;
		int flagV=0;
		if(O>0)
		{
			B-= O;
			flagO = 1;
			for(int i=0;i<O;i++)answerO+="BO";
			answerO+="B";
			N-=2*O;
		}
		if(G>0)
		{
			R-= G;
			flagG = 1;
			for(int i=0;i<G;i++)answerG+="RG";
			answerG+="R";
			N-=2*G;
		}
		if(V>0)
		{
			Y-= V;
			flagV = 1;
			for(int i=0;i<V;i++)answerV+="YV";
			answerV+="Y";
			N-=2*V;
		}
		
		if(R*2>N || Y*2>N || B*2>N)
		{
			cout<<"Case #"<<ttt<<": IMPOSSIBLE"<<endl;
			continue;
		}
		
		pair<int,string> data[3];
		data[0] = {R,"R"};
		data[1] = {Y,"Y"};
		data[2] = {B,"B"};
		sort(data,data+3);
		vector<string> odd;
		vector<string> even;
		int cnt2 = data[2].first;
		int cnt1 = data[1].first;
		int cnt0 = data[0].first;
		for(int i=0;i<cnt2;i++)
		{
			even.push_back(data[2].second);
		}
		for(int i=0;i<cnt1;i++)
		{
			int next = i*2+cnt2*2;
			if(next>=N){
				odd.push_back(data[1].second);
			}else{
				even.push_back(data[1].second);
			}
		}
		for(int i=0;i<cnt0;i++)
		{
			odd.push_back(data[0].second);
		}
		cout<<"Case #"<<ttt<<": ";
		for(int i=0;i<N;i++)
		{
			string next;
			if(i%2){
				next = odd[i/2];
			}else{
				next = even[i/2];			
			}
			
			if(next == "B" && flagO==1)
			{
				next = answerO;
				flagO=0;
			}else if(next == "R" && flagG==1){
				next = answerG;
				flagG=0;
			}else if(next == "Y" && flagV==1){
				next = answerV;
				flagV=0;
			}
			cout<<next;
		}
		
		printf("\n");
	}

	
	

    return 0;
}





        