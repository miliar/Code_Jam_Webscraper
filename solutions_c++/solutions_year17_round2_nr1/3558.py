#include <cstdio>
#include <iostream>
#include <utility>
#include <algorithm>
#include <set>
using namespace std;


int main(){
    int T,N,D,c=0,pos;
    double t,ans,temp,temp2,mintime;
    double td,ts;
    cin >> T;
    while(c++<T){
        set<pair<int,int> > K;
        cin >> D >> N;
        for(int i=0;i<N;i++){
            cin >>td >> ts;
            K.insert(make_pair(td,ts));
        }
        t=0;
        while(K.size()>1){
            auto a = K.begin();
            auto rem = K.end();
            while(next(a,1)!=K.end() && a->second <= next(a,1)->second) a = next(a,1);
            if(next(a,1)!=K.end()){
                double s1 = next(a,1)->first + next(a,1)->second*t;
                double s2 = a->first + a->second*t;
                mintime = (double)(s1 - s2)/(double)(a->second - next(a,1)->second);
                rem = a;
                a = next(a,1);
            }
            while(next(a,1)!=K.end()){
                if(a->second > next(a,1)->second){
                    double s1 = next(a,1)->first + next(a,1)->second*t;
                    double s2 = a->first + a->second*t;
                    temp = (double)(s1 - s2)/(double)(a->second - next(a,1)->second);
                    if(temp < mintime ){
                        mintime = temp;
                        rem = a;
                    }
                }
                a = next(a,1);
            }
            temp2 = (double)(D - K.begin()->first - K.begin()->second*t)/(double)K.begin()->second;
            if(temp2 <= mintime || rem == K.end()){
                t+=temp2;
                break;
            }
            else if(rem!=K.end()){
              //  cout << 'y';
                t+=mintime;
                K.erase(rem);
            }
        }
        if(K.size()==1){
            t += (double)(D - K.begin()->first-K.begin()->second*t)/(double)K.begin()->second;
//            cout << K.begin()->first << ' ' << K.begin()->second << ' ';
//            cout << t <<endl;
        }
        ans = D/t;
        printf("Case #%d: %.6f\n",c,ans);
    }



    return 0;
}
