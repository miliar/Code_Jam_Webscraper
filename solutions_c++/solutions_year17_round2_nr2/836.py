#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;
typedef pair <ll, ll> pll;
typedef vector <pii> vii;
typedef vector <double> vd;
 
#define SQR(x) ((x) * (x))
#define CUBE(x) ((x) * (x) * (x))
#define MP(a, b) make_pair((a), (b))
#define TASK "rmq"
#define MOD 1000000007LL
#define X first
#define Y second
#define EPS 1e-10
#define TESTING3
#define LAT 26
#define CYR 33
#define N 1000004
#define INF 1000000000
#define PI (acos(-1.0L))
#define double long double
#define MULTI
 
void solution();
char cch(int n);
 
stack <clock_t> times;
 
void start_t()
{
    times.push(clock());
}
 
void stop_t(string out)
{
    clock_t now = clock();
    clock_t past = times.top();
    times.pop();
    double delta = now - past;
    cout << out << ": " << fixed << delta / (double)CLOCKS_PER_SEC << endl;
}
 
int main()
{
    //ios::sync_with_stdio(false);
#ifdef _HOME_
    freopen("input.txt", "r", stdin);
    start_t();
#else
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
#endif // _HOME_
#ifdef MULTI
    int n;
    //scanf("%ld", &n);
    cin >> n;
    for(int i = 0;i < n;i++)
    {
        cout << "Case #" << i + 1 << ": ";
#endif
    solution();
    }
#ifdef _HOME_
    stop_t("Total time");
#endif // _HOME_
    return 0;
}
 
void solution()
{
    int n;
    cin >> n;
    int a[6];
    for(int i = 0;i < 6;i++)
        cin >> a[i];
    string s[3];
    for(int i = 1;i < 6;i+= 2)
    {
        if((a[i] == a[(i + 3) % 6]) && (a[i]))
        {
            for(int j = 0;j < 6;j++)
                if((i != j) && (j != ((i + 3) % 6)))
                    if(a[j])
                    {
                        cout << "IMPOSSIBLE" << endl;
                        return;
                    }
            for(;a[i];a[i]--, cout << cch(i) << cch((i + 3) % 6));
            cout << endl;
            return;
        }
        if(a[i] > a[(i + 3) % 6])
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        s[(i + 3) % 6 / 2] = "";
        s[(i + 3) % 6 / 2]+= cch((i + 3) % 6);
        a[(i + 3) % 6]-= a[i];
        for(;a[i];a[i]--, s[(i + 3) % 6 / 2]+= cch(i), s[(i + 3) % 6 / 2]+= cch((i + 3) % 6));
    }
    int b[3];
    for(int i = 0;i < 6;i+= 2)
        b[i / 2] = a[i];
    for(int i = 0;i < 3;i++)
        if(b[i] > b[(i + 1) % 3] + b[(i + 2) % 3])
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    if((b[0] >= b[1]) && (b[0] >= b[2]))
    {
        for(;b[0] < b[1] + b[2];b[0]--, b[1]--, b[2]--)
        {
            cout << s[0];
            s[0] = "R";
            cout << s[1];
            s[1] = "Y";
            cout << s[2];
            s[2] = "B";
        }
        for(;b[0];b[0]--)
        {
            cout << s[0];
            s[0] = "R";
            if(b[1])
            {
                cout << s[1];
                s[1] = "Y";
                b[1]--;
            }
            else
            {
                cout << s[2];
                s[2] = "B";
                b[2]--;
            }
        }
        cout << endl;
        return;
    }
    if((b[1] >= b[0]) && (b[1] >= b[2]))
    {
        for(;b[1] < b[0] + b[2];b[0]--, b[1]--, b[2]--)
        {
            cout << s[1];
            s[1] = "Y";
            cout << s[0];
            s[0] = "R";
            cout << s[2];
            s[2] = "B";
        }
        for(;b[1];b[1]--)
        {
            cout << s[1];
            s[1] = "Y";
            if(b[0])
            {
                cout << s[0];
                s[0] = "R";
                b[0]--;
            }
            else
            {
                cout << s[2];
                s[2] = "B";
                b[2]--;
            }
        }
        cout << endl;
        return;
    }
    if((b[2] >= b[0]) && (b[2] >= b[1]))
    {
        for(;b[2] < b[1] + b[0];b[0]--, b[1]--, b[2]--)
        {
            cout << s[2];
            s[2] = "B";
            cout << s[1];
            s[1] = "Y";
            cout << s[0];
            s[0] = "R";
        }
        for(;b[2];b[2]--)
        {
            cout << s[2];
            s[2] = "B";
            if(b[0])
            {
                cout << s[0];
                s[0] = "R";
                b[0]--;
            }
            else
            {
                cout << s[1];
                s[1] = "Y";
                b[1]--;
            }
        }
        cout << endl;
        return;
    }
    cout << "FAILED!!!!!!!!!!!" << endl;
}

char cch(int n)
{
    switch(n)
    {
        case 0:return 'R';
        case 1:return 'O';
        case 2:return 'Y';
        case 3:return 'G';
        case 4:return 'B';
        case 5:return 'V';
    }
    
}