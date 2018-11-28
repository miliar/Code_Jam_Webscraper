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

int main (int argc, char * const argv[]) {
	#ifndef ONLINE_JUDGE
	std::string input_file="B-large.in";
	std::string output_file="out.txt";
	if(!freopen(input_file.c_str(), "r", stdin)) cout<<"Something went wrong with the input file: "<<input_file<<endl;
	//if(!freopen(output_file.c_str(), "w", stdout)) cout<<"Something went wrong with the output file."<<endl;
	#endif
	ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    string s;
    int K;
    REP(case_no,t){

        cin>>s>>K;
        int ans=0,left=0,right=SIZE(s)-1;
        REP(x,SIZE(s))
            if(s[x]=='-'){left=x;break;}
        FORD(x,SIZE(s)-1,0)
            if(s[x]=='-'){right=x;break;}
        while(right-left+1>=K){
            DEBUG(cout<<s<<" left "<<left<<" right "<<right<<endl;)
            if(s[left]=='-'){
                ans++;
                bool found=false;
                int _left=left;
                FOR(i,_left,_left+K-1){
                    if(s[i]=='-') {s[i]='+';if(!found)left++;}
                    else {s[i]='-';found=true;;}
                }
            }
            else if(s[right]=='-'){
                ans++;
                bool found=false;
                int _right=right;
                FORD(i,_right,_right-K+1){
                    if(s[i]=='-') {s[i]='+';if(!found)right--;}
                    else {s[i]='-';found=true;}
                }
            }
            else{
                left++;
                right--;
            }
        }
        DEBUG(cout<<"END left "<<left<<" right "<<right<<endl;)

        cout<<"Case #"<<case_no+1<<": ";
        if(s.find("-")==string::npos)
            cout<<ans;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }


	return 0;
}
