#include <bits/stdc++.h>

#define ll long long

using namespace std;

const int INF = INT_MAX/3-100;

struct Cake {

    int r, h;
    bool operator<(const Cake& rhs) const
    {
        return this->r < rhs.r;
    }

    ll sq() const {
        return r*(ll)h;
    }
};

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);

    int TEST;
    cin >> TEST;

    double PI = acos(-1);

    for (int test = 1; test <= TEST; test++) {
        vector<Cake> cakes;
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            Cake c;
            cin >> c.r >> c.h;
            cakes.push_back(c);
        }

        std::sort(cakes.begin(), cakes.end(), [](const Cake &a, const Cake &b) {
            return a.sq() >= b.sq();
        });

/*
        for (int i = 0; i < n; i++) {
            cout << "!!!  " << cakes[i].sq() << endl;
        }
*/
        ll maxRad = 0;
        int maxRadIdx = -1;
        ll bok = 0;
        for (int  i = 0; i < k; i++) {
            bok += cakes[i].sq();
            if (cakes[i].r > maxRad) {
                maxRad = cakes[i].r;
            }
        }

        maxRadIdx = k-1;
        ll ans = bok*2 + maxRad*maxRad;
        for (int i = k; i < n; i++) { 
            if (cakes[i].r > maxRad) {
                maxRad = cakes[i].r;


                bok -= cakes[maxRadIdx].sq();
                bok += cakes[i].sq();
                maxRadIdx = i;

                ll cond = bok*2 + maxRad*maxRad;
                if (cond > ans)
                    ans = cond;
            }
        }

        cout << "Case #" << test << ": ";
        cout << fixed << setprecision(9);
        cout << ans*PI << endl;
    }
}
