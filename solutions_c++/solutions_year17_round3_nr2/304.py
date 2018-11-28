#include <cstdio>
#include <vector>

#define N 500

using namespace std;

struct Activity {
    int start, end;
    char who;
};

struct Compare {
    bool operator() (const Activity& a, const Activity& b) {
        return a.start < b.start;
    }
} cmp;

vector<Activity> v;
vector<int> gc, gj;

void solve(int case_no) {
    int ac, aj, fc, fj, c, d, j, k, gap, ans;

    v.clear();
    gc.clear();
    gj.clear();

    ans = 0;
    fc = fj = 720;

    scanf("%d%d", &ac, &aj);
    for (int i = 0; i < ac; i++) {
        scanf("%d%d", &c, &d);
        v.push_back((Activity) {c, d, 'C'});
        fj -= d - c;
    }
    for (int i = 0; i < aj; i++) {
        scanf("%d%d", &j, &k);
        v.push_back((Activity) {j, k, 'J'});
        fc -= k - j;
    }

    sort(v.begin(), v.end(), cmp);
    for (int i = 0; i < v.size(); i++) {
        int j = (i + 1) % (ac + aj);
        if (v[i].who == v[j].who) {
            ans += 2;
            gap = v[j].start - v[i].end;
            if (gap < 0)
                gap += 24 * 60;
            if (v[i].who == 'C')
                gj.push_back(gap);
            else
                gc.push_back(gap);
        }
        else
            ans++;
    }

    sort(gc.begin(), gc.end());
    sort(gj.begin(), gj.end());

    for (int i = 0; i < gc.size(); i++)
        if (fc >= gc[i]) {
            ans -= 2;
            fc -= gc[i];
        }


    for (int i = 0; i < gj.size(); i++)
        if (fj >= gj[i]) {
            ans -= 2;
            fj -= gj[i];
        }

    if (ac + aj == 1)
        ans = 2;

    printf("Case #%d: %d\n", case_no, ans);
}

int main(int argc, char** argv) {
    int case_no, t;

    scanf("%d", &t);
    for (case_no = 1; case_no <= t; case_no++)
        solve(case_no);

    return 0;
}
