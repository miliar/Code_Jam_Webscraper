#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;


void solve(int t)
{

    ull n,k,a,b;
    cin >> n >> k;
    cout <<"Case #" << t << ": ";
    /*if( k > (n+1)/2){
        cout << 0 << " " << 0 << endl;
        return ;
    }*/
    priority_queue<ull> PQ;
    PQ.push(n);
    for(int i=0;i<k;i++)
    {
      ull num = PQ.top();
      PQ.pop();
      a = num/2;
      b = num-num/2-1;
      PQ.push(a);
      PQ.push(b);
    }

    cout << a <<" " << b << endl;

}


int main(void)
{
    int T;
    cin >> T;

    for(int tc = 1; tc<= T; tc++)
        solve(tc);
    return 0;
}
