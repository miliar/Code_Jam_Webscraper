#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
using namespace std;


#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
#define pb(x) push_back(x)
#define modu 1000000007


int main(){
    int t;
    ofstream fout ("A-large.out");
    ifstream fin ("A-large(1).in");
    fin>>t;
    // cin>>t;
    rep(_,t){
        double d,n;

        fin>>d>>n;
        // cin>>d>>n;
        double k, s;
        double timeMax = 0;
        for(int i = 0; i <n; i++){
            fin>>k>>s;
            // cin>>k>>s;
            timeMax = max(timeMax,(d-k)/s);
        }
        double ans = d/timeMax;

        cout<<"Case #"<<_+1<<": ";
        // cout<<"Case #"<<_+1<<": ";
        printf("%.6f\n", ans);
        // fout<<ans<<endl;
        // cout<<ans<<endl;
        

    }

    return 0;
}
