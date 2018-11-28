#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

ifstream f("B-large.in");

bool isTidy(int n)
{
    int x = 11;
    while (n)
    {
        if(n % 10 > x)
            return false;
        x = n % 10;
        n = n / 10;
    }
    return true;
}

int expected(int n)
{
    while(!isTidy(n))
        --n;
    return n;
}

void one_tidy()
{
    char c;
    vector<char> result;
    int i = 1, aux;

    f.get(c);
    result.push_back(c);

    while(f.get(c) && c != '\n')
    {
        if(c < result[i - 1])
        {
            result.push_back('9');
            while(f.get(c) && c != '\n')
                result.push_back('9');
            f.putback(c);
            int j = i - 1;
            aux = result[j];
            while(j > 0 && result[j - 1] == aux)
            {
                result[j] = '9';
                --j;
            }

            --result[j];

        }
        else
        {
            result.push_back(c);
            ++i;
        }
    }

    i = 0;
    while(result[i] == '0')
        ++i;
    if(i > result.size())
        cout << '0';
    for (; i < result.size(); ++i)
        cout << result[i];
    cout << endl;
}

vector<char> print_solution()
{
    int n;
    f >> n; f.get();
    for(int i = 1; i <= n; ++i)
    {
        cout << "Case #" << i << ": ";
        one_tidy();
    }
}

int main()
{
    //cout<<expected(2220);
    vector<char> result;
    print_solution();

    f.close();
}














