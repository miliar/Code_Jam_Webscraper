#include <string>
#include <fstream>
#include <iostream>
#include <queue>
#include <cmath>

//std::ifstream cin("large_input.txt");
//std::ofstream cout("large_output.txt");

using std::string;
using std::pair;
using std::make_pair;
using std::queue;
using std::ceil;
using std::cout;
using std::cin;

pair<long long int,long long int> lastStall(long long int N,long long int K){
    queue<pair<long long int,long long int> > q;
    q.push(make_pair(0,N-1));
    long long int mid=0;
    pair<long long int,long long int> cur;
//    cout << cur.first << "  "<<cur.second<<"  "<<K<<"\n";
    for(long long int i=K;i>1;){
        cur = q.front();
        q.pop();

        mid=(cur.first+cur.second)/2;

        --i;
//        cout << cur.first << "  "<<cur.second<<"  "<<i<<"\n";
        if(i%2!=0){
                if(mid+1<=cur.second) q.push(make_pair(mid+1,cur.second));
                i=(i+1)/2;
        }else{
            if(cur.first<=mid-1) q.push(make_pair(cur.first,mid-1));
            i/=2;
            }
//            cout << q.front().first << "  "<<q.front().second<<"  "<<i<<"\n";

    }

    cur = q.front();
//    cout << cur.first << "  "<<cur.second<<"\n";
    if((mid=(cur.second-cur.first))%2==0) return make_pair(mid/2,mid/2);
    else return make_pair((mid-1)/2+1,(mid-1)/2);

}

int main() {
    int T;
    long long int K;
    long long int N;
    cin >> T;
    pair<long long int,long long int> p;
    for(int e=1;e<=T;++e){
        cin >> N >> K;
//        cout << N << "  "<<K<<"\n";
        p = lastStall(N,K);
        cout <<"Case #"<<e<<": "<<p.first<<" "<< p.second << "\n";
    }

    return 0;
}




