#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <numeric>
#include <utility>
#include <map>
#include <cmath>
#include <functional>
using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PRINT_OBJECT(obj) for(auto i: obj) cout<<i<<" "; cout<<endl;

#ifndef ONLINE_JUDGE
#define DEBUG(x) x
#else
#define DEBUG(x)
#endif
bool is_ok(LL num){
    while(num>=10){
        LL last=num%10;
        LL second_last=(num%100)/10;
        if(second_last>last) return false;
        num/=10;
    }
    return true;
}
int main (int argc, char * const argv[]) {
	#ifndef ONLINE_JUDGE
	std::string input_file="B-small-attempt0.in";
	std::string output_file="out.txt";
	if(!freopen(input_file.c_str(), "r", stdin)) cout<<"Something went wrong with the input file: "<<input_file<<endl;
	if(!freopen(output_file.c_str(), "w", stdout)) cout<<"Something went wrong with the output file."<<endl;
	#endif
	ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    REP(test_no,t){
        LL N;
        cin>>N;
        LL ans=0;
        FOR(num,1,N){
            if(is_ok(num))ans=num;
        }
        cout<<"Case #"<<test_no+1<<": "<<ans<<endl;
    }


	return 0;
}
