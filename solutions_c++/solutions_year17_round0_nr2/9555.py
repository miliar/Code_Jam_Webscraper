// Rakesh Singh Rawat
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<string>
#include<string.h>
#include<limits.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>

using namespace std ;
//================================================================================
#define INF 100000000
#define FOR(i,a,b)  for( int i = int(a) ; i<=int(b) ; i++)					// for
#define LL signed long long int
#define fre 	freopen("0.in","r",stdin);freopen("0.out","w",stdout)
#define print(x) printf("%d\n",x)											//printf
#define printll(x) printf("%lld\n",x)
#define scanll(x) scanf("%lld",&x)
#define scan(x) scanf("%d",&x)												// scanf
#define ln  scanf("\n")														//consume \n
#define SS(a) stringstream ss(a)
#define ii pair<int,int>
#define F first
#define S second
#define abs(x) ((x)>0?(x):-(x))
#define RESET(arr,val) memset(arr, val, sizeof(arr))
#define ret return
#define ITERM(v) for(map<int,int>::iterator it = v.begin() ; it!=v.end() ; it++ )
#define ITERV(v)  for(vector<int>::iterator it = v.begin() ; it!=v.end() ; it++ )
#define VPUSH(v,b) v.push_back(b)												// push_back()
#define VI vector<int>
//=================================================================================

int main()
{
  int t ;
  	cin>>t ;
  	int c = 0 ;
  	while(t--)
  	{
  	 	c++ ;
    	string k ,s;
    	cin>>k ;
    	s = '0'+ k ;
    	int size = s.size()-1;
    	
		for(int i = size-1 ; i>=0;i--)
		{
			if(s[i]>s[i+1]) 
			{
				s[i]-- ;
				for(int j=i+1;j<=size;j++)   s[j] = '9' ;	
			}
		}	
    	cout<<"Case #"<<c<<": " ;
    	int i = 0 ;
		while(s[i]=='0')  i++ ;
		
		for(int j=i ; j<s.size();j++)  cout<<s[j] ;
		cout<<endl ;	
    
     }
  return 0 ;
}

