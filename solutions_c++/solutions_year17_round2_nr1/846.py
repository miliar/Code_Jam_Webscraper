#include<iostream>
#include<string>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
using namespace std;

#define fs first
#define sd second
#define mk make_pair

typedef pair<double,double> pii;

double maxSpeed(vector<pii> &h, int n, int d){
	float M = 0;
	for(int i=n-1;i>=0;i--){
		if(h[i].fs<d){
			double aux = (double(d)-h[i].fs)/h[i].sd;
			M = aux>M?aux:M;
		}
	}
	return M;
}

int main(){
	int T;
	int d, n, k, s;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		cin >> d >> n;
		vector<pii> h(n);
		for(int i=0;i<n;i++){
			cin >> k >> s;
			h[i]=mk(k,s);
		}
		sort(h.begin(),h.end());
		double M = maxSpeed(h,n,d);
		if(M==0) M=1;
// 		cout << M << endl;
		cout.precision(6);
		cout << fixed << double(d)/M << endl;
	}
	return 0;

}
