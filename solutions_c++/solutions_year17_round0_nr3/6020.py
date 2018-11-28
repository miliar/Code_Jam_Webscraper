#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;
    for(int i = 0 ; i<n ; i++){
        priority_queue<long> g;
        long a;
        long b;
        long A;
        long B;
        cin >> a;
        cin >> b;
        g.push(a);
        for (int j=0;j<b;j++){
            long k = g.top();
            g.pop();
            A = k/2;
            B = (k-1)/2;
            g.push(A);
            g.push(B);

        }

        cout << "Case #" << i+1 << ": " << A << " " << B << endl;
    }
    return 0;
}

/*for n in range(int(raw_input())):
    m = raw_input().split(" ")
    r = Q.PriorityQueue()
    r.put(int(m[0]))
    for i in range(int(m[1])):
        k = r.get()
        print k
        r.put(int(k/2))
        r.put(int((k-1)/2))
    A = r.get()
    B = r.get()
    print "Case #"+ str(n+1)+ ": "+str(B)+" "+str(A)
*/