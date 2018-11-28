#include <iostream>
#include <string>

using namespace std;
string sr;
void reverse(int a)
{
    if(sr[a] == '+')
        sr[a] = '-';
    else
        sr[a] = '+';    
}
void flip(int m,int n)
{
    int x = m;
    for( ; x < m + n ; x++)
        reverse(x);
}
int count(int x,int n)
{
    int val;
    for (int i = x; i < x + n; i++)
    {
        if(sr[i] == '+')
            val++;
    }
    return val;
}
int main()
{
    int test; cin >> test;
    for (int ti = 0; ti < test; ti++)
    {
        cin >> sr; int k; cin >> k;
        int i = 0; int steps = 0; int len = sr.length();
        for( ; i < len - k ; i++ )
        {
            if(sr[i] == '-')
            {
                flip(i,k); steps++;
            }
        }
        string temp = sr;
        int num = count(len-k,k);
        cout << "Case #" << ti+1 << ": ";
        if( num == 0 )
        {
            cout << steps + 1 << endl; continue;
        }
        else if( num == k )
        {
            cout << steps << endl; continue;
        }
        cout << "IMPOSSIBLE" << endl;
    }
}