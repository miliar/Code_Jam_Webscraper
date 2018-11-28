#include <bits/stdc++.h>

using namespace std;
#define ll long long
template<class T> void p(vector<T>& a){ for(int i = 0;i < a.size();i++) cout << a[i] << " "; cout << endl; }
#define vi vector<int>
#define vl vector<ll>
#define vb vector<bool>
#define f(i,a,b) for(i = a;i < b;i++)
#define rf(i,a,b) for(i = a;i >= b;i--)

int main(){
	int t_,t;
	cin >> t;
	f(t_,0,t){
		int n,d,i,k,s;
		cin >> d >> n;
		long double max_time = -1;
		f(i,0,n){
			cin >> k >> s;
			long double cur_time = (long double)(d - k)/s;
			if(max_time < cur_time) max_time = cur_time;
		}
		long double speed = (long double)d * (long double)(1/max_time);
		//cout << max_time << " " << d << " ";
		cout << "Case #" << t_ + 1 << ": ";
		printf("%.6Lf\n", speed); 
	}
	return 0;
}
