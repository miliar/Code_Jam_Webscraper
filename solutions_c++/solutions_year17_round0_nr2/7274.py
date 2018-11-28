#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;


void int_to_vector(long long a, vector<int>& v)
{
    while(a)
    {
        v.push_back(a % 10);
        a /= 10;
    }
    reverse(v.begin(), v.end());
}

void vector_to_int(long long& a, vector<int> const& v)
{
    a = 0;
    for (int i = 0; i < v.size(); ++i)
    {
        a = a * 10 + v[i];
    }
}

bool check_a(long long& a)
{
    vector<int> v;
    int_to_vector(a, v);
    bool check = true;
    for (int i = 0; check && i + 1 < v.size(); ++i)
    {
        if (v[i] > v[i + 1])
        {
            check = false;
            for (int j = i + 1; j < v.size(); j++)
            {
                v[j] = 0;
            }
        }
    }

    if (check)
    {
        return true;
    }

    vector_to_int(a, v);
    a--;

}

void solution()
{
    long long a;
    vector<int> v;
    cin >> a;
    while(!check_a(a));
    cout << a << '\n';
}

int main(int argc, char *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        stringstream ss;
        ss << (i+1);
        cout << "Case #" << ss.str() << ": ";
        solution();
        cout << "\n";
    }

    return 0;
}
 