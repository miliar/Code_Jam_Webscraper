#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:100000000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

int findmini(int x,int s){
	int res=(x*10)/(11*s);
	if((x*10)%(11*s)==0) return res;
	return res+1;
}
int findmaxi(int x,int s){
	int res=(x*10)/(9*s);
	return res;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int Tcas;cin>>Tcas;
	FR(cas,Tcas){
		printf("Case #%d: ",cas+1);
		int n,p;
		cin>>n>>p;
		vector<int> ingredients;
		FR(i,n) {
			int x;cin>>x;
			ingredients.push_back(x);
		}
		int mini[100][100]={0};
		int maxi[100][100]={0};
		CLR(mini,0);
		CLR(maxi,0);
		int totMini=1<<30;
		int totMaxi=-(1<<30);
		FR(i,n){
			vector<int> temp;
			FR(j,p) {int x;cin>>x;temp.push_back(x);}
			sort(ALL(temp));
			FR(j,p){
				mini[i][j]=findmini(temp[j],ingredients[i]);
				maxi[i][j]=findmaxi(temp[j],ingredients[i]);
				if(mini[i][j]>maxi[i][j]) {mini[i][j]=maxi[i][j]=-1;continue;}
				totMini = min(totMini,mini[i][j]);
				totMaxi = max(totMaxi,maxi[i][j]);
			}
		}
		totMini=max(1,totMini);
		int sum=0;
		FOR(k,totMini,totMaxi+1){
			int cur=p;
			FR(i,n){
				int temp=0;
				FR(j,p) if(k>=mini[i][j] && k<=maxi[i][j]) temp++;
				cur=min(cur,temp);
			}
			sum+=cur;
			FR(i,n){
				int temp=0;
				FR(j,p) {
					if(temp==cur) break;
					if(k>=mini[i][j] && k<=maxi[i][j]) temp++;
					mini[i][j]=maxi[i][j]=-1;
				}
			}
		}
	
		cout<<sum<<endl;
	}
}