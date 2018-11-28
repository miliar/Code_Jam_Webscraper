#include<bits/stdc++.h>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("out.txt");
    ifstream fin;
    fin.open("inp.txt");
    int n;
    vector<int> digits;
    string inp;
    fin >> n;
    for (int i = 0; i < n; i++)
    {
        fin >> inp;
        digits.clear();
        int j = 0;
        //___________________________________________
        while ((inp[j] >= '0') && (inp[j] <= '9'))
        {
            digits.push_back(inp[j] - '0');
            j++;
        }
        if (j <= 1)
        {
            fout << "Case #" << i + 1 << ": ";
            fout << digits[0] << endl;
        }
        else
        {
            for (int k = 0; k < j; k++)
            {
                int r = 1;
                int alart = 0;
                while (r < j)
                {
                    if (digits[r] < digits[r - 1])
                    {
                        if (alart == 0)
                        {
                            digits[r - 1]--;
                            digits[r] = 9;
                            alart++;
                        }
                        else
                        {
                            digits[r] = 9;
                        }
                    }
                    r++;
                }
            }
            int alrt2 = 0;
            if (digits[0] == 0)
            {
                alrt2 = 1;
                digits.erase(digits.begin());
            }
            fout << "Case #" << i + 1 << ": ";
            for (int u = 0; u < j - alrt2; u++)
            {
                fout << digits[u];
            }
            fout << endl;
        }
    }
    return 0;
}
