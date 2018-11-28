#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;
using ULL = unsigned long long;

struct Interval {
    struct Key {
        ULL m, M, idx;

        Key(){}
        Key(ULL left, ULL right){
            idx = (left+right)/2;

            m = idx - left;
            M = right - idx;
            if( m > M ) swap(m,M);

        }
        bool operator<( const Key & other) const {
            if( m != other.m ){ return m < other.m; }
            if( M != other.M ){ return M < other.M; }
            return idx > other.idx;
        }
    };
    ULL left, right, idx;
    Key key;

    Interval(ULL left, ULL right) : 
        left(left), right(right), idx((left+right)/2), key(left,right)
    {
        //printf("int=(%llu, %llu),key=(%llu,%llu,%llu)\n", left, right,key.m, key.M, key.idx);
    }
    Interval(){}

    bool operator<( const Interval & other) const {
        return key < other.key;
    }

};

pair<ULL,ULL> solve(){
    ULL N, K;
    cin >> N >> K;

    priority_queue<Interval> q {};
    q.push( Interval(1, N) );

    Interval iv;
    for( int k = 1; k <= K; k++){
        iv = std::move(q.top());
        //printf("int=(%llu, %llu),key=(%llu,%llu,%llu)\n", iv.left, iv.right, iv.key.m, iv.key.M, iv.key.idx);
        q.pop();
        if( iv.idx != iv.left  ){ q.push( Interval(iv.left, iv.idx-1) ); }
        if( iv.idx != iv.right ){ q.push( Interval(iv.idx+1, iv.right) ); }
    }

    return {iv.key.M, iv.key.m};
}

int main(){
    int T;
    cin >> T;
    for ( int t = 1; t<=T; t++){
        pair<ULL,ULL> ans = solve();
        printf("Case #%d: %llu %llu\n", t, ans.first, ans.second);
    }
}
