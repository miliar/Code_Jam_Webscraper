#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<string>
#include<iomanip>

#define INF 99999999
#define MAXN 1003

using namespace std;

int t;
int n;
double d;

double k[MAXN];
double s[MAXN];

double maks;

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> d >> n;
		
		for(int i = 0; i < n; i++){
			cin >> k[i] >> s[i];	
		}
	/*	maks = (D - k[0])/s[0];
		for(int i = 1; i < n; i++){
			maks = max(maks, (D - k[i]/s[i]));	
		}*/
		maks = d*s[0]/(d - k[0]);
		for(int i = 1; i < n; i++){
			maks = min(maks, d*s[i]/(d - k[i]));	
		}
		
		cout << "Case #"<<test<<": "<<fixed<<setprecision(8)<<maks<<endl;	
	}
	
	cout << endl;
	return 0;
}
