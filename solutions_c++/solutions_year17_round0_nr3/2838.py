#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

struct _p
{
    long long l, k;
};

long long n, k;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    long long i, t, j;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        long long ansmx = 0, ansmn = 0;
        vector<_p> now;
        cin >> n >> k;
        now.push_back({n, 1});
        while (!now.empty())
        {
            long long curl = (now.back()).l, curn = (now.back()).k;
            now.pop_back();
            k -= curn;
            curl--;
            if (k <= 0)
            {
                ansmn = curl/2;
                ansmx = curl - ansmn;
                break;
            }
            if (curl == 0)
                continue;
            long long l1 = curl/2;
            long long l2 = curl - l1;
            if (l1 != 0)
            {
                bool check = false;
                for (j = 0; j < now.size(); j++)
                    if (now[j].l == l1)
                    {
                        check = true;
                        now[j].k += curn;
                        break;
                    }
                if (!check)
                {
                    now.push_back({l1, curn});
                    for (j = (int)now.size() - 2; j >= 0 && now[j].l > now[j+1].l; j--)
                        swap(now[j], now[j+1]);
                }
            }
            if (l2 != 0)
            {
                bool check = false;
                for (j = 0; j < now.size(); j++)
                    if (now[j].l == l2)
                    {
                        check = true;
                        now[j].k += curn;
                        break;
                    }
                if (!check)
                {
                    now.push_back({l2, curn});
                    for (j = (int)now.size() - 2; j >= 0 && now[j].l > now[j+1].l; j--)
                        swap(now[j], now[j+1]);
                }
            }
        }
        cout << "Case #" << i+1 << ": " << ansmx << " " << ansmn << endl;
    }
    return 0;
}
