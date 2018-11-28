#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

int t,n,d;
double res;

void read_input(){
    cin >> t;
    int k,s;

    for(int i = 0 ; i < t ; ++i){
	cin >> d >> n;
	res = -1 ; 

	for(int j = 0 ; j < n; ++j){
	    cin >> k >> s;

	    double t = (double)(d - k)/s;
	    double sp = d/t;

	    if(res < 0 || res > sp)
		res = sp;
	}

	cout.precision(17);
	cout << "Case #" << (i+1) <<": " << res << endl;
    }
}

void calc(){
}

int main(){
    read_input();
    calc();
    return 0;
}
