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

LL get_max_element(multiset<LL>& fragments){
    multiset<LL>::iterator last=fragments.end();
    --last;
    auto val=*last;
    fragments.erase(last);
    return val;
}
int main (int argc, char * const argv[]) {
	#ifndef ONLINE_JUDGE
	std::string input_file="C-small-2-attempt0.in";
	std::string output_file="out.txt";
	if(!freopen(input_file.c_str(), "r", stdin)) cout<<"Something went wrong with the input file: "<<input_file<<endl;
	if(!freopen(output_file.c_str(), "w", stdout)) cout<<"Something went wrong with the output file."<<endl;
	#endif
	ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    REP(test_no,t){
        multiset<LL> fragments;
        LL K,N,left,right;
        cin>>N>>K;
        fragments.insert(N);
        REP(client_no,K){
            auto val=get_max_element(fragments);
            if(val%2==0){
                left=val/2-1;
                right=val/2;
            }
            else{
                left=(val-1)/2;
                right=(val-1)/2;
            }
            fragments.insert(left);
            fragments.insert(right);
        }
        cout<<"Case #"<<test_no+1<<": "<<max(left,right)<<" "<<min(left,right)<<endl;
    }


	return 0;
}
