#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
typedef long long ll;

using namespace std;

const string kInputFilename = "input.txt";
const string kOutputFilename = "output.txt";

ifstream in("input.txt");
ofstream out("output.txt");

vector<long> update(vector<long> state){
    long n=state.size()/2;
    long d=state[n-1];
    long dn=state[n+n-1];
    long b=d/2;
    long a=b;
    if (d%2==0){
        a--;
    }
    bool pasta=false;
    bool pastb=false;
    vector<long> sizes,freqs;
    if (n>1){
        for (long i=0;i<(n-1);i++){
            if ((pasta) && (pastb)){
                sizes.push_back(state[i]);
                freqs.push_back(state[n+i]);
            }
            if ((pasta)&&(!pastb)){
                if (state[i]<b){
                    sizes.push_back(state[i]);
                    freqs.push_back(state[n+i]);
                }
                if (state[i]==b){
                    sizes.push_back(state[i]);
                    freqs.push_back(state[n+i]+dn);
                    pastb=true;
                }
                if (state[i]>b){
                    sizes.push_back(b);
                    sizes.push_back(state[i]);
                    freqs.push_back(dn);
                    freqs.push_back(state[n+i]);
                }
            }
            if ((! pasta)&&(! pastb)){
                if (state[i]<a){
                    sizes.push_back(state[i]);
                    freqs.push_back(state[n+i]);
                }
                if (state[i]==a){
                    if (a<b){
                        sizes.push_back(state[i]);
                        freqs.push_back(state[n+i]+dn);
                        pasta=true;
                    }
                    if (a==b){
                        sizes.push_back(state[i]);
                        freqs.push_back(state[n+i]+dn+dn);
                        pasta=true;
                        pastb=true;
                    }
                }
                if (state[i]>a){
                    if (a==b){
                        sizes.push_back(a);
                        sizes.push_back(state[i]);
                        freqs.push_back(dn+dn);
                        freqs.push_back(state[n+i]);
                        pasta=true;
                        pastb=true;
                    }
                    if (a<b){
                        sizes.push_back(a);
                        freqs.push_back(dn);
                        if (b<state[i]){
                            sizes.push_back(b);
                            sizes.push_back(state[i]);
                            freqs.push_back(dn);
                            freqs.push_back(state[n+i]);
                            pastb=true;
                        }
                        if (b==state[i]){
                            sizes.push_back(b);
                            freqs.push_back(state[n+i]+dn);
                            pastb=true;
                        }
                        if (b>state[i]){
                            sizes.push_back(state[i]);
                            freqs.push_back(state[n+i]);
                        }
                    }
                }
            }
        }
        vector<long> neww;
        for (long i=0;i<sizes.size();i++){
            neww.push_back(sizes[i]);
        }
        for (long i=0;i<freqs.size();i++){
            neww.push_back(freqs[i]);
        }
        return(neww);
    }
    else if (n==1){
        vector<long> neww;
        neww.push_back(a);
        neww.push_back(b);
        neww.push_back(state[1]);
        neww.push_back(state[1]);
        return(neww);
    }
}


int main() {
    int T;
    in >> T;
    for (int ti=0;ti<T;ti++){
        long n,k;
        in>>n>>k;
        vector<long> C;
        C.push_back(n);
        C.push_back(1);
        long m=0;
        long t;
        while (k>0){
            long pos=C.size();
            m=C[pos-1];
            t=C[(pos/2)-1];
            k=k-m;
            C=update(C);
        }
        long a,b;
        b=t/2;
        a=b;
        if (t%2==0){
            a--;
        }
        out<<"Case #"<<ti+1<<": "<< b<<" "<<a<<endl;
  }
//vector<long> A;
//for (long i=0;i<2;i++){
//    long a;
//    cin>>a;
//    A.push_back(a);
//}
////for (long i=0;i<2;i++){
////    cout<<A[i]<<" ";
////}
////cout<<endl;
//vector<long> B;
//B=update(A);
//for (int i=0;i<B.size();i++){
//    cout<<B[i]<<" ";
//}
  return(0);
}
