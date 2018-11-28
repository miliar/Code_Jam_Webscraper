#include<cstdio>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

#define pb push_back
#define mp make_pair

int T,n,k;
double u;
double p[55];
const double eps = 1e-12;

void read_input(){
    cout.precision(17);
    cin >> T;

    for(int t = 0 ; t < T ; ++t){
	cin >> n >> k >> u;

	for(int i = 0 ; i < n; ++i)
	    cin >> p[i];
	p[n] = 1;

	for(int i = 0 ; i < n; ++i){
	    if(u == 0)
		break;

	    sort(p,p+n);

	    if(p[0] == 1)
		break;

	    int j;
	    for(j = 1; j < n && p[j] - p[0] < eps ; ++j);
	    
	    int num = j;

	    if((double)(p[j] - p[0]) * j <= u)
	    {
		u  -= (double)(p[j]-p[0]) * j;
		for(int k = 0; k < j; ++k)
		    p[k] = p[j];
	    }
	    else{
		for(int k = 0 ; k < j; ++k)
		    p[k] += u/j;
		u = 0 ;
	    }
	}

	double res = 0 ;
	for(int i = 0 ; i < n; ++i)
	    res += log(p[i]);

	cout << fixed << "Case #" << t+1 << ": " << exp(res) << endl;
    }
}

int main(){
    read_input();
    return 0;
}
