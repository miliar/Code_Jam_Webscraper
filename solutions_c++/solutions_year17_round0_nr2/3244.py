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
    ifstream be("B-large.in");
    ofstream ki("ki");

    int T;
    be>>T;
    for(LL i=0; i<T;i++){
        string szam;
        be>>szam;
        int s=0;

        int akt=1;
        int n=szam.length();
        bool b=true;


        while(akt<n and b){
            b=szam[akt-1]<=szam[akt];
            if(b){
                if(szam[akt-1]<szam[akt]){s=akt;}
                akt++;
            }
        }

        ki<<"Case #"<<i+1<<": ";
        if(b){ki<<szam<<'\n';}
        else{
            szam[s]--;
            //for(int  j=s+1;j<n;j++){szam[j]='9';}
            for(int j=((szam[0]=='0') ? 1 : 0);j<n;j++){ki<<((j<s+1)?szam[j]:'9');}
            ki<<'\n';
        }
    }

    be.close();
    ki.close();
	return 0;
}
