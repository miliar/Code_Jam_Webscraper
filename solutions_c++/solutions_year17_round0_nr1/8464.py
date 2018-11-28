#include<bits/stdc++.h>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("out.txt");
    int n, leng;
    vector<int> pank;
    string inp;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> inp >> leng;
        pank.clear();
        int j = 0;
        //___________________________________________
        while ((inp[j] == '+') || (inp[j] == '-'))
        {
            if (inp[j] == '+')
                pank.push_back(1);
            else
                pank.push_back(0);
            j++;
        }
        while (j < leng)
        {
            pank.push_back(1);
            j++;
        }
        int a = 0;
        int res = 0;
        while (a < j - leng + 1)
        {
            if (pank[a] == 0)
            {
                for(int m = a; m < leng + a; m++)
                    pank[m] = (pank[m] + 1) % 2;
                res++;
            }
            a++;
        }
        fout << "Case #" << i + 1 << ": ";
        int alart = 0;
        for (int v = 1; v < leng + 1; v++)
        {
            if (pank[j - v] != 1)
            {
                alart = 1;
            }
        }
        if (alart == 0)
            fout << res << endl;
        else
            fout << "IMPOSSIBLE" << endl;
    }
}
