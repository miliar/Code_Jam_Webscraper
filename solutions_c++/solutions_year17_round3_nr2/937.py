#include <bits/stdc++.h>
using namespace std;
#define int long long
#undef int
struct Node {
    int who;
    int l;
    int r;
    Node() {}
    Node(int _who, int _l, int _r)
    {
        who = _who;
        l = _l;
        r = _r;
    }
    int len()
    {
        return r - l;
    }
    bool operator<(const Node n) const
    {
        return l < n.l;
    }
};
int main()
{
#define int long long
    int T;
    cin >> T;
    for (int I = 1; I <= T; I++) {
        int Ans = 0;
        int AC, AJ;
        cin >> AC >> AJ;
        vector<Node> v;
        int sum_AC = 0;
        int sum_AJ = 0;
        for (int i = 0; i < AC; i++) {
            int l, r;
            cin >> l >> r;
            v.push_back(Node(1, l, r));
            sum_AJ += r - l;
        }
        for (int i = 0; i < AJ; i++) {
            int l, r;
            cin >> l >> r;
            v.push_back(Node(0, l, r));
            sum_AC += r - l;
        }
        sort(v.begin(), v.end());
        v.push_back(Node(2, v.back().r, v[0].l + 1440));
        int now = 0;
        auto SZ = v.size();
        for (int i = 0; i < v.size(); i++) {
            if (i == (SZ - 1))
                break;
            auto u = v[i];
            auto ne = v[i + 1];
            if (u.r - u.l > 720)
                Ans += 2;
            if (u.who == 0) {
                
                if (u.who == ne.who && u.len() + ne.len() + (ne.l - u.r) > 720) {
                    Ans += 2;
                }
                if(u.who!=ne.who && u.len()+(ne.l-u.r)>720) Ans+=2;
                if (ne.who == 2 && sum_AC + ne.len() > 720)
                    Ans += 2;
            } else if (u.who == 1) {
                if (u.who == ne.who && u.len() + ne.len() + (ne.l - u.r) > 720) {
                    Ans += 2;
                }
                if(u.who!=ne.who && u.len()+(ne.l-u.r)>720) Ans+=2;
                if (ne.who == 2 && sum_AJ + ne.len() > 720)
                    Ans += 2;

            } else if (u.who == 2) {
                if (u.len() + ne.len() > 720)
                    Ans += 2;
            }
        }

        printf("Case #%lld: %lld\n", I, Ans);
    }
    return 0;
}
