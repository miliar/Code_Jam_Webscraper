#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define __fail() cout << "IMPOSSIBLE\n"; continue;

string res;
bool fail;
int r, y, b, ry, rb, yb, n;
int i_r, i_y, i_b;
int r_c, y_c, b_c;

class Node;

using NNode = std::shared_ptr<Node>;

class Node {
public:
    Node(char type, NNode next = nullptr) : type(type), next(next) { }

    char type;
    NNode next;
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cout << "Case #" << T + 1 << ": ";
        cin >> n >> r >> ry >> y >> yb >> b >> rb;
        i_r = r;
        i_y = y;
        i_b = b;
        int c_pos = 0;
        if (r > 0) {
            ++c_pos;
        }
        if (y > 0) {
            ++c_pos;
        }
        if (b > 0) {
            ++c_pos;
        }
        if (ry > 0) {
            ++c_pos;
        }
        if (rb > 0) {
            ++c_pos;
        }
        if (yb > 0) {
            ++c_pos;
        }
        if (c_pos < 2) {
            __fail();
        }
        if (c_pos == 2) {
            if (r > 0 && r == y) {
                for (int i = 0; i < r; ++i) {
                    cout << "RY";
                }
                cout << "\n";
                continue;
            }
            if (r > 0 && r == b) {
                for (int i = 0; i < r; ++i) {
                    cout << "RB";
                }
                cout << "\n";
                continue;
            }
            if (r > 0 && r == yb) {
                for (int i = 0; i < r; ++i) {
                    cout << "RG";
                }
                cout << "\n";
                continue;
            }

            if (y > 0 && y == b) {
                for (int i = 0; i < y; ++i) {
                    cout << "YB";
                }
                cout << "\n";
                continue;
            }
            if (y > 0 && y == rb) {
                for (int i = 0; i < y; ++i) {
                    cout << "YV";
                }
                cout << "\n";
                continue;
            }

            if (b > 0 && b == ry) {
                for (int i = 0; i < b; ++i) {
                    cout << "BO";
                }
                cout << "\n";
                continue;
            }
            __fail();
        }


        if (i_r == 0 || i_y == 0 || i_b == 0) {
            r_c = yb;
            r -= yb + 1;
            y_c = rb;
            y -= rb + 1;
            b_c = ry;
            b -= ry + 1;

            if (i_r == 0 && b == y) {
                for (int i = 0; i < y_c; ++i) {
                    cout << "VY";
                }

                for (int i = 0; i < b_c; ++i) {
                    cout << "BO";
                }
                for (int i = 0; i < b + 1; ++i) {
                    cout << "BY";
                }
                cout << "\n";
                continue;
            }

            if (i_y == 0 && b == r) {
                for (int i = 0; i < r_c; ++i) {
                    cout << "GR";
                }
                for (int i = 0; i < b_c; ++i) {
                    cout << "BO";
                }
                for (int i = 0; i < b + 1; ++i) {
                    cout << "BR";
                }
                cout << "\n";
                continue;
            }
            if (i_b == 0 && y == r) {
                for (int i = 0; i < r_c; ++i) {
                    cout << "GR";
                }

                for (int i = 0; i < y_c; ++i) {
                    cout << "YV";
                }
                for (int i = 0; i < y + 1; ++i) {
                    cout << "YR";
                }
                cout << "\n";
                continue;
            }

            __fail();
        }

        if (r < yb + 1 || y < rb + 1 || b < ry + 1) {
            cerr << "1\n";
            __fail();
        }
        r_c = yb;
        r -= yb + 1;
        y_c = rb;
        y -= rb + 1;
        b_c = ry;
        b -= ry + 1;

        NNode fy = make_shared<Node>('Y');
        NNode lr = make_shared<Node>('R', fy);

        NNode fb = make_shared<Node>('B');
        NNode ly = make_shared<Node>('Y', fb);


        NNode fr = make_shared<Node>('R');
        NNode lb = make_shared<Node>('B', fr);

        vector<NNode> rr(1, ly);
        vector<NNode> yy(1, lb);
        vector<NNode> bb(1, lr);
        fail = false;
        while (r > 0 || y > 0 || b > 0) {
            bool can_r = rr.size() > 0;
            bool can_y = yy.size() > 0;
            bool can_b = bb.size() > 0;
            int max_can = 0;
            if (can_r && r > max_can) {
                max_can = r;
            }
            if (can_y && y > max_can) {
                max_can = y;
            }
            if (can_b && b > max_can) {
                max_can = b;
            }

            if (max_can == 0) {
                fail = true;
                break;
            }

            if (can_r && r == max_can) {
                NNode e = move(rr.back());
                rr.pop_back();
                NNode n = make_shared<Node>('R', e->next);
                e->next = n;
                if (e->type == 'Y') {
                    yy.push_back(move(n));
                    bb.push_back(move(e));
                } else {
                    yy.push_back(move(e));
                    bb.push_back(move(n));
                }
                --r;
                continue;
            }
            if (can_y && y == max_can) {
                NNode e = move(yy.back());
                yy.pop_back();
                NNode n = make_shared<Node>('Y', e->next);
                e->next = n;
                if (e->type == 'R') {
                    rr.push_back(move(n));
                    bb.push_back(move(e));
                } else {
                    rr.push_back(move(e));
                    bb.push_back(move(n));
                }
                --y;
                continue;
            }
            if (can_b && b == max_can) {
                NNode e = move(bb.back());
                bb.pop_back();
                NNode n = make_shared<Node>('B', e->next);
                e->next = n;
                if (e->type == 'R') {
                    yy.push_back(move(e));
                    rr.push_back(move(n));
                } else {
                    yy.push_back(move(n));
                    rr.push_back(move(e));
                }
                --b;
                continue;
            }
        }
        if (fail) {
            cerr << "2\n";
            __fail();
        }
        cout << "R";
        for (int i = 0; i < r_c; ++i) {
            cout << "GR";
        }
        lr = lr->next;
        while (lr != nullptr) {
            cout << lr->type;
            lr = lr->next;
        }
        for (int i = 0; i < y_c; ++i) {
            cout << "VY";
        }
        lr = ly->next;
        while (lr != nullptr) {
            cout << lr->type;
            lr = lr->next;
        }

        for (int i = 0; i < b_c; ++i) {
            cout << "OB";
        }
        lr = lb->next;
        while (lr != fr) {
            cout << lr->type;
            lr = lr->next;
        }
        cout << "\n";
    }

    return 0;
}
