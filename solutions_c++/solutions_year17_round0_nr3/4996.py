#include <iostream>
#include <queue>
#include <fstream>

using namespace std;

int main()
{
    long long T;
    ifstream infile;
    ofstream outfile;
    infile.open("data.in");
    outfile.open("data.out");
    infile >> T;
    long long N, K;
    long long a,b,curr;
    for(int i = 0; i < T; i++) {
        infile >> N >> K;
        priority_queue<int> spaces;
        spaces.push(N);
        for(int j = 1; j < K; j++) {
            curr = spaces.top();
            curr -= 1;
            spaces.pop();
            a = curr / 2 + curr % 2;
            b = curr / 2;
            spaces.push(a);
            spaces.push(b);
        }

        curr = spaces.top();
        curr -= 1;
        spaces.pop();
        a = curr / 2 + curr % 2;
        b = curr / 2;
        outfile <<"Case #" << i + 1 << ": ";
        outfile << a << " " << b << endl;
    }
    return 0;
}
