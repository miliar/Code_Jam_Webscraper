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
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	
//_______________________________________________
	int test_cases,tesT;
	double p[100],pp[100][100];
	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
	double u;
	int i,j,n,k;
	cin>>n>>k>>u;
	for(i=0;i<n;i++){
		cin>>p[i];
	}
	p[n]=1.0;
	sort(p,p+n);
	for(i=n-k;i<n;i++){
		int terms=(i-n+k+1);
		
		if(u/terms+p[i]>p[i+1]){
			u-=terms*(p[i+1]-p[i]);
			for(j=n-k;j<=i;j++)
				p[j]=p[i+1];
		}
		else{
			
			for(j=n-k;j<=i;j++)
				p[j]=p[i]+u/terms;
			break;
		}
	}
	//for(i=0;i<n;i++)
	//	cout<<p[i]<<' ';
	for(i=0;i<100;i++)for(j=0;j<100;j++)pp[i][j]=0;
	pp[0][0]=1.0;
	for(int m=0;m<n;m++){
		for(i=0;i<=m;i++){
			pp[m+1][i]+=pp[m][i]*(1-p[m]);
			pp[m+1][i+1]+=pp[m][i]*p[m];
		}
	}
	double sum=0;
	for(i=k;i<=n;i++)sum+=pp[n][i];
	printf("%.8f",sum);
//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}