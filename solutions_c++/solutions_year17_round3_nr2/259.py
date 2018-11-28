#include <iostream>
#include <fstream>
using namespace std;

const int L = 24*60;
const int INF = 2*L;
bool A[L];
bool B[L];

int DPA[L][L/2+1];
int DPB[L][L/2+1];
int dpb(int n, int t);
int dpa(int n, int t)
{
    if (t < 0 || t > n+1 || A[n])
        return INF;
    int& res = DPA[n][t];
    if (res != -1)
        return res;
    else
    {
        //cerr << "a " << n << " " << t << " -> " << min(dpa(n-1, t-1), dpb(n-1, t-1)+1) << endl;
        return res = min(dpa(n-1, t-1), dpb(n-1, t-1)+1);
    }
}
int dpb(int n, int t)
{
    if (t < 0 || t > n+1 || B[n])
        return INF;
    int& res = DPB[n][t];
    if (res != -1)
        return res;
    else
    {
        //cerr << "b " << n << " " << t << " -> " << min(dpb(n-1, t), dpa(n-1, t)+1) << endl;
        //cin.get();
        return res = min(dpb(n-1, t), dpa(n-1, t)+1);
    }

}

void cleardp(bool a)
{
    for (int i = 0; i < L; i++)
    {
        for (int j = 0; j <= L/2; j++)
        {
            DPA[i][j] = DPB[i][j] = -1;
        }
    }
    if (a)
    {
        DPA[0][0] = INF;
        DPA[0][1] = 0;
        DPB[0][0] = INF;
        DPB[0][1] = INF;
    }
    else
    {
        DPA[0][0] = INF;
        DPA[0][1] = INF;
        DPB[0][0] = 0;
        DPB[0][1] = INF;
    }
}

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        /*int a, b;
        cin >> a >> b;
        if (a == 2 || b == 2)
        {
            int s1, e1, s2, e2;
            cin >> s1 >> e1 >> s2 >> e2;
            int l1 = max(e1, e2)-min(s1,s2);
            int l2 = min(e1,e2)+L-max(s1,s2);
            if (l1 <= 720 || l2 <= 720)
                cout << "Case #" << t+1 << ": 2" << endl;
            else
                cout << "Case #" << t+1 << ": 4" << endl;
        }
        else
        {
            int x;
            for (int i = 0; i < 2*(a+b); i++)
                cin >> x;
            cout << "Case #" << t+1 << ": 2" << endl;
        }*/
        cerr << t << endl;
        int AC, BC;
        cin >> AC >> BC;
        for (int i = 0; i < L; i++)
            A[i] = B[i] = false;
        for(int i = 0; i < AC; i++)
        {
            int s, e;
            cin >> s >> e;
            for (int i = s; i < e; i++)
                A[i] = true;
        }
        for (int i = 0; i < BC; i++)
        {
            int s, e;
            cin >> s >> e;
            for (int i = s; i < e; i++)
                B[i] = true;
        }
        int r = INF;
        if (!A[0])
        {
            cleardp(true);
            r = min(r, dpa(L-1, L/2));
            r = min(r, dpb(L-1, L/2)+1);
        }
        if (!B[0])
        {
            cleardp(false);
            r = min(r, dpa(L-1, L/2)+1);
            r = min(r, dpb(L-1, L/2));
        }

        cout << "Case #" << t+1 << ": " << r << endl;
    }
}
