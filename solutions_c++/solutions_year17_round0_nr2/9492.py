#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isTidy(long long int n)
{
    int prec = n%10;
    n /= 10;
    while (n > 0)
    {
        int attuale = n%10;
        if (prec < attuale)
            return false;
        prec = attuale;
        n /= 10;
    }
    return true;
}

vector<int> converti(long long int n)
{
    vector<int> s;
    while (n>0)
    {
        s.push_back(n%10);
        n/=10;
    }
    reverse(s.begin(),s.end());
    return s;
}

vector<int> tidyfy(vector<int> s)
{
    for (int i = s.size()-1; i>0; i--)
    {
        if (s.at(i) < s.at(i-1))
        {
            s.at(i - 1)--;
            for (int j=i; j<s.size(); j++)
                s.at(j) = 9;
        }
    }
    return s;
}

int main()
{
    int T;
    long long int N;
    cin >> T;
    for (int test = 1; test <= T; test++)
    {
        cin >> N;
        vector<int> v = converti(N);
        vector<int> s = tidyfy(v);
        int i = 0;
        while(s.at(i) == 0) i++;
        cout << "Case #" << test << ": ";
        for (;i<s.size();i++)
            cout << s.at(i);
        cout << endl;
    }
    return 0;
}
