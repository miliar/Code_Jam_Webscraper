#include <stdio.h>
#include <string.h>
#define lld long long
#include <map>
using namespace std;


struct Node {
    lld value;
    lld count;
    Node(lld _value = 0, lld _count = 0): value(_value), count(_count) {}
};

class Heap {
public:
    map<lld, lld> data;

    Heap() {
    }

    void insert(Node v) {
        lld value = -v.value;
        if (data.find(value) != data.end()) {
            data[value] += v.count;
        } else {
            data[value] = v.count;
        }
    }

    Node pop() {
        lld value = -data.begin()->first;
        lld count = data.begin()->second;
        data.erase(data.begin());
        return Node(value, count);
    }
};

int main() {
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++) {
        lld k, n;
        scanf("%lld%lld", &n, &k);

        Heap heap;
        lld ans = 0;
        heap.insert(Node(n, 1));
        for (;;) {
            Node v = heap.pop();
            if (v.count < k) {
                k -= v.count;
                heap.insert(Node(v.value / 2, v.count));
                heap.insert(Node((v.value - 1) / 2, v.count));
            } else {
                ans = v.value;
                break;
            }
        }

        printf("Case #%d: ", t);
        printf("%lld %lld\n", ans / 2, (ans - 1) / 2);
    }
}

