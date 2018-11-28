#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size())
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

int main(){
    ifstream be("A-small-attempt0.in");
    ofstream ki("ki");

    int T;
    be>>T;
    for(LL cn=0; cn<T;cn++){
        char c;
        be.get(c);
        unsigned int n=0;
        int l=0;
        while(be.get(c) and (c!=' ')){
            n=n<<1;
            n+=((c=='-')?1:0);
            l++;
            //cout<<n<<'\n';
        }
        int k=0;
        be>>k;
        int flip=(1<<k)-1;

//        cout<<n<<' '<<k<<'\n';

        int v=0;
        int lo=n & ~(n - 1);

        while((1<<(l-k)>=lo) and (lo!=0)){
            n=n^(lo*flip);
            lo=n & ~(n - 1);
            v++;
        }
        cout<<v<<' '<<n<<'\n';

        ki<<"Case #"<<cn+1<<": ";
        if(lo!=0){
            ki<<"IMPOSSIBLE"<<'\n';
        }else{
            ki<<v<<'\n';
        }

    }

    be.close();
    ki.close();
	return 0;
}
