#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define MOD 1000000007
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define range(a, b, c) (a>=b && a<c)
#define stlfor(a, b) for(auto a=b.begin(); a!=b.end(); a++)
#define rstlfor(a, b) for(auto a=b.rbegin(); a!=b.rend(); a++)
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
using namespace std;
using namespace __gnu_pbds;
typedef pair<int, int> pii;
typedef priority_queue<pii, vector<pii>, greater<pii>> min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

int main()
{
    fio;
    int t;
    cin >> t;
    for(int tc=1; tc<=t; tc++)
    {
        long long x;
        cin >> x;
        int len = 0;
        vector<int> num;
        for(long i=x; i; i /= 10)
        {
            len++;
            num.pb(i % 10);
        }
        for(int i=0; i<(len >> 1); i++)
            swap(num[i], num[len - i - 1]);
        int fd = len;
        for(int i=1; i<len; i++)
        {
            if(num[i] < num[i-1])
            {
                fd = i-1;
                while(fd and num[fd] == num[fd-1])
                    fd--;
                break;
            }
        }
        cout << "Case #" << tc << ": ";
        if(fd == len)
        {
            for(int i=0; i<len; i++)
                cout << num[i];
        }
        else if(num[fd] == 1)
        {
            for(int i=1; i<len; i++)
                cout << 9;
        }
        else
        {
            for(int i=0; i<fd; i++)
                cout << num[i];
            cout << num[fd] - 1;
            for(int i=fd+1; i<len; i++)
                cout << 9;
        }
        cout << endl;
    }
    return 0;
}