#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>
#include<climits>
#include<vector>
#include<stack>
#include<set>
#include<queue>
#include<map>
#include<math.h>
using namespace std;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define sint(i) scanf("%d",&i)
#define ss(s) scanf("%s",s)
#define pii pair<int,int>
#define mp(i,j) make_pair(i,j)
#define ll long long
#define MAX 1000000000
#define MOD 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pb(i) push_back(i);
#define tr(v,it) for(it=v.begin();it!=v.end();it++)
#define LARGE 1
int main()
{
	#if DEBUG
	freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif
    #if SMALL
	freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    #endif
    #if LARGE
	freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    #endif
    int test,t;
    cin>>t;
    int i,j;
    FOR(test,1,t) {
    	string s;
    	int k;
    	cin>>s>>k;
    	int len=s.length();
    	int flip=0;
    	FOR(i,0,len-k) {
    		if(s[i]=='-') {
    			flip++;
    			FOR(j,i,i+k-1)
    			{
    				if(s[j]=='+')
    					s[j]='-';
    				else
    					s[j]='+';
    			} 
    		}
    	}
    	bool flag=true;
    	FOR(i,max(len-k+1,0),len-1) {
    		if(s[i]=='-') {
    			flag=false;
    		}
    	}
    	cout<<"Case #"<<test<<": ";
    	if(flag)
    		cout<<flip<<"\n";
    	else
    		cout<<"IMPOSSIBLE"<<"\n";
    }
    
	return 0;
}