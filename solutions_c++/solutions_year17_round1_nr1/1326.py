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

char a[30][30];

int main()
{
	freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	
//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		int r,c,i,j;
		string s;
		cin>>r>>c;
		char prev_ch;
		for(i=0;i<r;i++){
			cin>>s;
			for(j=0;j<c;j++)
				a[i][j]=s[j];
			prev_ch='?';
			for(j=0;j<c;j++){
				if(a[i][j]=='?')
					a[i][j]=prev_ch;
				else
					prev_ch=a[i][j];
			}
			char prev_ch='?';
			for(j=c-1;j>=0;j--){
				if(a[i][j]=='?')
					a[i][j]=prev_ch;
				else
					prev_ch=a[i][j];
			}
		}
		
		for(j=0;j<c;j++){
			prev_ch='?';
			for(i=0;i<r;i++)
				if(a[i][j]=='?')
					a[i][j]=prev_ch;
				else
					prev_ch=a[i][j];
			prev_ch='?';
			for(i=r-1;i>=0;i--)
				if(a[i][j]=='?')
					a[i][j]=prev_ch;
				else
					prev_ch=a[i][j];
		}
		cout<<endl;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++)
				cout<<a[i][j];
			cout<<endl;
		}
//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}