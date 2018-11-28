#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>

using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 12000


int main()
{
	freopen("b.in","r",stdin);
	//freopen("a.out","w",stdout);
	
//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		string s;
		int j;
		cin>>s;
		for(int i=s.size()-2;i>=0;i--){
			if(s[i]>s[i+1]){
				for(j=i+1;j<s.size();j++)
					s[j]='9';
				s[i]--;
			}
		}
		string ans;
		if(s[0]=='0')
			ans=s.substr(1,s.size()-1);
		else
			ans=s;
		cout<<ans;
//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}