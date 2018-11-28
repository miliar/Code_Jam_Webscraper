#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <queue>

using namespace std;

class Space {
    public:
    long long start;
    long long end;
    Space(long long st, long long nd){
        start = st;
        end = nd;
    }
    bool operator < (const Space& other) const {
        if((end - start - 1)/2 == (other.end - other.start - 1)/2){
            if((end - start)/2 == (other.end - other.start)/2){
                return other.start < start;
            }
            return (end - start)/2 < (other.end - other.start)/2;
        }
        else return (end - start - 1)/2 < (other.end - other.start - 1)/2;
    }
    // ~Space();
};

void bath(long long N, long long K){
    Space temp(0,0);
    priority_queue<Space> pq;
    pq.push(Space(0, N));
    while(K>1){
        K--;
        temp = pq.top();
        pq.pop();
        pq.push(Space(temp.start, (temp.end + temp.start - 1)/2 ));
        pq.push(Space((temp.end + temp.start + 1)/2, temp.end));
        // delete temp;
    }
    temp = pq.top();
    pq.pop();
    cout << (temp.end - temp.start)/2 << " " << (temp.end - temp.start - 1)/2  << "\n";
}

int main(){
    int numIn;
    long long N[100];
    long long K[100];
    cin >> numIn;
    for(int i=0; i<numIn; i++){
        cin >> N[i];
        cin >> K[i];
    }

    for(int i=0; i<numIn; i++){
        cout << "Case #" << i+1 << ": ";
        bath(N[i], K[i]);
    }
}

// int main() {
// priority_queue<int> pqi;
// srand(time(0)); // Seed the random number generator
// for(int i = 0; i < 100; i++)
// pqi.push(rand() % 25);
// while(!pqi.empty()) {
// cout << pqi.top() << ' ';
// pqi.pop();
// }
// }