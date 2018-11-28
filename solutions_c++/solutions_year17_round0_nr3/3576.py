#include <iostream>
#include <queue>
using namespace std;
int main(int argc, char const *argv[]) {

    int num;
    cin >> num;
    for (int numruns = 0; numruns < num; ++numruns) {
        int n,k;
        cin >> n >> k;
        priority_queue<int> q;
        q.push(n);
        for(int x=0;x<k-1;x++) {
            int temp = q.top();
            q.pop();
            if (temp > 2) {
                q.push((temp-1)/2);
                q.push(temp/2);
            } else if (temp == 2) {
                q.push(1);
            }
        }
        int out = q.top();
        cout << "Case #" << numruns+1 << ": " << out/2 << " " << (out-1)/2 << endl;
    }
    return 0;
}