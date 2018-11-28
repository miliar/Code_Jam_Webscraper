#include <bits/stdc++.h>

using namespace std;

int nr[100];

struct val{
    int mn, mx;
} obj[100][100];

int now[100];
double r[100];
double q[100][100];
stack<int> s;

bool cmp(val A, val B) {
    if(A.mn == B.mn) return A.mx < B.mx;
    return A.mn < B.mn;
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);

    int t;
    cin >> t;

    for(int o = 1; o <= t; o ++) {

        int n, p;
        cin >> n >> p;

        for(int i = 1; i <= n; i ++)
            cin >> r[i];

        for(int i = 1; i <= n; i ++) {
            for(int j = 1; j <= p; j ++)
                cin >> q[i][j];
        }

        int k = 0;
        for(int j = 1; j <= p; j ++) {

            for(int i = 1; i <= n; i ++) {
                obj[i][j].mx = (int)(q[i][j] / (90 * r[i] / 100));

                while( !( (double)(obj[i][j].mx * (90 * r[i] / 100)) <= q[i][j] && q[i][j] <= (double)(obj[i][j].mx * (110 * r[i] / 100)) ) && obj[i][j].mx > 0)
                    obj[i][j].mx --;
                obj[i][j].mn = obj[i][j].mx;

                while( (double)((obj[i][j].mn - 1) * (90 * r[i] / 100)) <= q[i][j] && q[i][j] <= (double)((obj[i][j].mn - 1) * (110 * r[i] / 100)) )
                    obj[i][j].mn --;
            }
        }

        for(int i = 1; i <= n; i ++) {
            sort(obj[i] + 1, obj[i] + p + 1, cmp);
            now[i] = 1;
        }

        for(int j = 1; j <= p; j ++) {
            bool ok = true;
            int maxx = -1, poz = 0;
            for(int i = 1; i <= n; i ++) {
                if(maxx < obj[i][now[i]].mn)
                    maxx = obj[i][now[i]].mn, poz = i;
            }
            if(maxx == 0) ok = false, s.push(poz);
            for(int i = 1; i <= n; i ++) {
                if(maxx > obj[i][now[i]].mx) ok = false, s.push(i);
            }

            if(ok) {
                for(int i = 1; i <= n; i ++)
                    now[i] ++;
                k ++;
            }
            else {
                while(!s.empty()) {
                    now[s.top()] ++;
                    if(now[s.top()] > p) j = p + 1;
                    s.pop();
                }
            }

        }
        cout << "Case #" << o <<": " << k << "\n";
    }

    return 0;
}
