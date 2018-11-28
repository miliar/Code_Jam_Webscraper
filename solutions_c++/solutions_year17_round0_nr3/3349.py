#include <iostream>
#include <string>
#include <utility>
#include <set>
using namespace std;

int N, K;

typedef pair< int, pair<int,int> > node;

void solve2() {
    set<node> bathroom;
    bathroom.insert(make_pair(-N, make_pair(0,N+1)));

    int mini, maxi;
    for(int k=0;k<K;++k) {
        node top = *bathroom.begin();
        bathroom.erase(bathroom.begin());
        int size = -top.first;
        int leftmost = top.second.first;
        int rightmost = top.second.second;
        int pos = leftmost+(size-1)/2+1;
        //cerr << size << " " << leftmost << " " << rightmost << " " << pos << endl;
        int L = pos-leftmost-1;
        int R = rightmost-pos-1;
        mini = min(L,R);
        maxi = max(L,R);

        bathroom.insert(make_pair(-L,make_pair(leftmost,pos)));
        bathroom.insert(make_pair(-R,make_pair(pos,rightmost)));
    }

    cout << maxi << " " << mini << endl;

}

int main() {
    int ncase;
    cin >> ncase;
    for(int caseno=1;caseno<=ncase;++caseno) {
        cin >> N >> K;
        cout << "Case #" << caseno << ": ";
        solve2();
    }

    return 0;
}

