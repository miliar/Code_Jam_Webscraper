#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

// std::numeric_limits<T>::max() 

const double PI=3.141592653589793238462643383279502884197169399375105820974944592307816406286;

void main2(){
	int N, K;
	cin>>N >> K;
    vector<unsigned long long> R(N), H(N);
    vector<unsigned long long> RH(N);
    for(int i=0;i<N;i++){
        cin >> R[i] >> H[i];
        RH[i]=R[i]*H[i];
    }

    if(false){
        vector<int> selected(N);
        unsigned long long result=0;
        for(int i=0;i<1<<N;i++){
            int s=0;
            for(int j=0;j<N;j++){
                selected[j]=(i>>j)%2;
                s+=selected[j];
            }
            if(s==K){
                unsigned long long rmax=0;
                unsigned long long r=0;
                for(int j=0;j<N;j++){
                    if(selected[j]){
                        rmax=max(rmax,R[j]);
                        r+=2*R[j]*H[j];
                    }
                }
                r+=rmax*rmax;
                if(r>result){
                    for(int j=0;j<N;j++) cerr<<selected[j] << ' ';
                    cerr<<endl;
                }
                result=max(result,r);
            }
        }
        printf("%.9f",result*PI);
    }else{
        sort(RH.begin(),RH.end());
        unsigned long long sum=0;
        for(int i=N-K;i<N;i++){
            sum+=RH[i];
        }
        unsigned long long threshold = RH[N-K];
        unsigned long long rmax = 0;
        for(int i=0;i<N;i++){
            if(R[i]*H[i] >= threshold)
            rmax=max(R[i],rmax);
        }
        unsigned long long result = rmax*rmax + 2*sum;
        sum-=threshold;
        for(int i=0;i<N;i++){
            if(R[i] > rmax){
                unsigned long long result2 = R[i]*R[i]+2*(R[i]*H[i]+sum);
                result=max(result,result2);
            }
        }
    
        printf("%.9f",result*PI);
    }
}

int main(){
    string core;
    //core="C-small-practice";
    core="A-large";
    //core="test";
    freopen ( (core+".in").c_str(), "r", stdin );
    freopen ( (core+".out").c_str(), "w", stdout );
	int T;
	cin>>T;

	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		cerr <<"Case #"<<t+1<<endl;
		main2();
		cout<<endl;
	}
    
    fclose (stdin);
    fclose (stdout);
}
