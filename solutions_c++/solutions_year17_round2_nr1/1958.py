#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <iomanip>
using namespace std;
#define forn(i,n) for(int i=0;i<n;i++)
#define forn1(i,n) for(int i=1;i<=n;i++)
#define mp make_pair
#define pb push_back
typedef long long ll;
int t,n;
double ks[1001];
double ss[1001];
int main(){
	cout<<setprecision(9);
	cin>>t;
	forn(i,t){
		double d;
		cin>>d>>n;
		double best=-1.0;
		forn(j,n){
			cin>>ks[j]>>ss[j];
		}
		double tt=0.0;
		for(int j=n-1;j>=0;j--){
			tt=max(tt,(d-ks[j])/ss[j]);
			// cout<<tt<<endl;
		}
		
		cout<<"Case #"<<i+1<<": "<<d/tt<<endl;

	}
}