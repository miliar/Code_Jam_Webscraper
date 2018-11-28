#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

class SegmentTree {
public:
    struct Node{

        Node(int _left, int _right) {
            pLeft = NULL;
            pRight = NULL;
            left = _left;
            right = _right;
            int mid = (left + right) >> 1;
            ls = mid - left ;
            rs = right - mid;
        }
        int left;
        int right;
        int ls;
        int rs;
        Node* pLeft;
        Node* pRight;
    };

public:
    SegmentTree() {
    }


    std::pair<int, int> get_k_th(int n, int k) {
        std::priority_queue<std::pair<int, int> > pq;
        int cnt = 0;
        int pow = 1;
        while(pow <= k) {
            cnt++;
            pow = pow << 1;
        }
        preorder(1, n, pq, 1, k);
        std::pair<int, int> top;
        for (int i = 1; i <= k; i++) {
            top = pq.top();
//            std::cout<< "i = "<< i << " min = " << top.first <<" max = " << top.second << std::endl;
            pq.pop();
        }
        return top;
    }


private:
    Node* buildTree(int start, int end) {
        if (start > end) {
            return NULL;
        }
        Node* node = new Node(start, end);
        if (start == end) {
            return node;
        }
        node->pLeft = buildTree(start, ((start+end) >> 1) - 1);
        node->pRight = buildTree(1 + ((start + end) >> 1), end);
        return node;
    }

    void preorder(int left, int right, std::priority_queue<std::pair<int, int>>& pq, int cnt, int k) {
        if (left > right || cnt > k) {
            return;
        }
        int mid = (left + right) >> 1;
        int ls = mid - left;
        int rs = right - mid;
        pq.push(std::pair<int, int>(std::min(ls, rs),std::max(ls, rs)));
//        std::cout << left << " " << right << " " << ls <<" "<< rs << std::endl;
        preorder(left, mid - 1, pq, cnt+1, k);
        preorder(mid+1, right, pq, cnt+1, k);
    }
private:
    Node* root;
};
int main(int argc, char *argv[])
{

    freopen("C-small-2-attempt1.in", "r", stdin);
//    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test_case_number;
    scanf("%d", &test_case_number);

    for (size_t test_case = 1; test_case <= test_case_number; test_case++) {
        int n, k;
        scanf("%d %d", &n, &k);
//        std::cout << n << k <<std::endl;

        SegmentTree tree;
        std::pair<int, int> ans = tree.get_k_th(n, k);
        printf("Case #%d: %d %d\n", test_case, ans.second, ans.first);
#if 0
        std::vector<int> values(n+3, 0);
        values[1] = 1;
        values[n+2] = 1;
        std::vector<int> ls(n+3, 0);
        std::vector<int> rs(n+3, 0);
        int ans_ls = 0;
        int ans_rs = 0;
        for (int ind = 1; ind <= k; ind++)
        {
            for (size_t j = 2; j <= n+1; j++) {
                if (values[j-1] == 1) {
                    ls[j] = 0;
                } else {
                    ls[j]  = ls[j-1] + 1;
                }

            }
            for (size_t j = n+1; 2 <= j; j--) {
                if (values[j+1] == 1) {
                    rs[j] = 0;
                } else {
                    rs[j]  = rs[j+1] + 1;
                }
            }

            int max_id = -1;
            int max_ls = -1;
            int max_rs = -1;

            for (size_t j = n+1; 2 <= j  ; j--) {
                int candidata_val_min = std::min(rs[j], ls[j]);
                int candidata_val_max = std::max(rs[j], ls[j]);
                if (values[j] == 1) {
                    continue;
                }
                if (max_rs < candidata_val_min ) {
                    max_id = j;
                    max_rs = candidata_val_min;
                    max_ls = candidata_val_max;
                    ans_rs = candidata_val_max;
                    ans_ls = candidata_val_min;
                    continue;
                }

                if (max_rs == candidata_val_min && max_ls < candidata_val_max) {
                    max_id = j;
                    max_rs = candidata_val_min;
                    max_ls = candidata_val_max;
                    ans_rs = candidata_val_max;
                    ans_ls = candidata_val_min;
                    continue;
                }

                if (max_rs == candidata_val_min && max_ls == candidata_val_max && j < max_id) {
                    max_id = j;
                    max_rs = candidata_val_min;
                    max_ls = candidata_val_max;
                    ans_rs = candidata_val_max;
                    ans_ls = candidata_val_min;
                    continue;
                }

            }


            int next_id = max_id;
            values[next_id] = 1;
        }
        printf("Case #%d: %d %d\n", test_case, ans_rs, ans_ls);
#endif

    }

    return 0;
}
