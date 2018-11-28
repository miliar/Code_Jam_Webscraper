#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void print_result(int case_no, int result)
{
    if(result == -1)
        cout << "Case #" << case_no << ": IMPOSSIBLE" << endl;
    else
        cout << "Case #" << case_no << ": " << result << endl;
}

void solve(string cakes, int K, int case_no)
{
    int count = 0;
    for(int j=0; j<cakes.length(); j++)
    {
        if(cakes[j] == '-')
        {
            count++;
            if(j + K > cakes.length())
            {
                print_result(case_no, -1);
                return;
            }
            for(int m=0; m<K; m++)
                cakes[j + m] = cakes[j + m] == '-' ? '+' : '-';
        }
    }
    print_result(case_no, count);
}

int main()
{
    int T, K;
    cin >> T;

    string cakes;
    int count;

    for(int i=0; i<T; i++)
    {
        count = 0;
        cin >> cakes >> K;
        solve(cakes, K, i+1);
    }
}

