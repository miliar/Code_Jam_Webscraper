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
#define SMALL 1
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
    int i;
    FOR(test,1,t) {
    	string s;
    	cin>>s;
    	int len=s.length();
    	int pos=len;
    	bool flag=false;
    	FOR(i,1,len-1)
    	{
    		if(s[i]<s[i-1])
    			{
    				flag=true;
    				pos=i;
    				break;
    			}
    	}
    	for(i=pos-1;i>0;i--)
    		if(s[i]==s[i-1])
    			pos--;
    	if(flag) {
    	s[pos-1]--;
    	FOR(i,pos,len-1)
    	s[i]='9';
    	}
    	int start=0;
    	FOR(i,0,len-2)
    	{
    		if(s[i]=='0')
    			start++;
    	}

    	cout<<"Case #"<<test<<": ";
    	FOR(i,start,len-1)
    	cout<<s[i];
    	cout<<"\n";
    }
    
	return 0;
}