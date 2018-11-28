#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define LLMAX 1000000000000000010
#define MAX 100005
#define gcd __gcd
#define mod 1000000007
#define pb(n) push_back(n)
#define fr front()
#define vint vector<int>
#define vstring vector<string>
#define vll vector<long long int>
#define pii pair<int,int>
#define forp(i,a,n) for(int i=(a);i<(n);i++)
#define forn(i,a,n) for(int i=(a);i>=(n);i--)
#define mp std::map<string, int>
#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)

int main()
{
    int t,k,cnt,minCnt,sLength;
    bool flag,fl;
    cin>>t;

    for(int z=0;z<t;z++)
    {
    	string s,st;
    	cin>>s>>k;
    	st=s;
    	cnt=0;
    	minCnt=INT_MAX;
    	int prevIndex[sLength];
    	int sLength = s.length();
    	int flipRange = sLength-k+1;
    	//cout<<s<<" "<<st<<endl;
    	for(int i=0; i<sLength; i++)
    	{
    		prevIndex[i] = 0;
    		if(s[i]=='+')
    			st[i]=s[i]=1;
    		else
    			st[i]=s[i]=0;
    	}


    	//cout<<s<<" "<<st<<endl;
    	for(int i=0;i<flipRange;i++)
    	{
    		if(!s[i])
    		{
    			cnt++;
    			for(int j=i;j<i+k;j++)
    				s[j] = 1-s[j];
    		}
    	}
    	for(int i=0;i<sLength;i++)
    	{
    		if(s[i]==0)
    			flag = 0;
    	}
    	//cout<<minCnt<<" "<<cnt<<" "<<fl<<" "<<flag<<endl;
    	//cout<<s<<" "<<st<<endl;
    	//cout<<s.length();
    	if(flag)
    		minCnt = min(minCnt,cnt);
    	cnt=0;
    	fl=1;


    	for(int i=sLength-1;i>k-2;i--)
    	{
    		if(!st[i])
    		{
    			cnt++;
    			for(int j=i;j>i-k;j--)
    			{
    				st[j] = 1-st[j];
    			}
    		}
    	}
    	for(int i=sLength-1;i>=0;i--)
    	{
    		if(!st[i])
    			fl = 0;
    	}
    	//cout<<minCnt<<" "<<cnt<<" "<<fl<<" "<<flag<<endl;
    	if(fl){
    		minCnt = min(minCnt,cnt);
    		cout<<"Case #"<<z+1<<": "<<minCnt<<endl;
    	}
    	else if(flag){
    		cout<<"Case #"<<z+1<<": "<<minCnt<<endl;
    	}
    	else
    		cout<<"Case #"<<z+1<<": IMPOSSIBLE"<<endl;
    }
}

