#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long int LL;

class Node{
public:
    Node(){}
    Node(LL _num, LL _size): num(_num), size(_size){};
    bool operator < (const Node &n) const{
        return num < n.num;
    }

    LL num;
    LL size;
};

int main(void){
    int tt;
    LL nn, kk;
    scanf("%d", &tt);
    for(int tc = 1; tc <= tt; tc++){
        scanf("%lld%lld", &nn, &kk);
        Node *node1 = new Node(nn, 1);
        Node *node2 = new Node(0, 0);
        Node *node1Next, *node2Next;
        LL cnt = 0;
        while(cnt < kk){
            if(cnt + node1->size + node2->size >= kk){
                break;
            }
            cnt += node1->size + node2->size;

            if(node1->num % 2){
                node1Next = new Node(node1->num / 2, node1->size * 2 + node2->size);
                node2Next = new Node(node1->num / 2 - 1, node2->size);
            }else{
                node1Next = new Node(node1->num / 2, node1->size);
                node2Next = new Node(node1->num / 2 - 1, node1->size + node2->size * 2);
            }
            delete node1;
            delete node2;
            node1 = node1Next;
            node2 = node2Next;
        }

        LL maxLen = (cnt + node1->size >= kk)? node1->num: node2->num;
        printf("Case #%d: ", tc);
        if(maxLen % 2){
            printf("%lld %lld\n", maxLen / 2, maxLen / 2);
        }else{
            printf("%lld %lld\n", maxLen / 2, maxLen / 2 - 1);
        }
        delete node1;
        delete node2;
    }
    return 0;
}
