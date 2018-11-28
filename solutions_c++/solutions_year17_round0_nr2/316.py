#include <bits/stdc++.h>
#define loop(i, a, n) for(int i = a; i < n; i++)
#define inf 10
#define cin in
#define cout out
using namespace std;

ifstream in("in.in");
ofstream out("out.txt");

void prep()
{
    static int t = 1;
    cout << "Case #" << t++ << ": ";
}

void to_arr(const string& s, vector<int>& arr)
{
    for (auto& x : s) arr.push_back(x - '0');
}

void func()
{
    bool b = true, first = true;
    string s; cin >> s;
    vector<int> arr;
    to_arr(s, arr);
    arr.push_back(inf);
    int i, next;

    for (i = next = 0; b && i < arr.size() - 1; i++, first = false)
    {
        while (arr[next] == arr[i]) next++;

        if (arr[next] < arr[i])
        {
            if (!first || arr[i] > 1) cout << arr[i] - 1;
            b = false;
        }
        else cout << arr[i];
    }

    while (i++ < arr.size() - 1) cout << 9; cout << endl;
}

int main()
{
    int t; cin >> t;
    while(t--) prep(), func();
    return 0;
}
