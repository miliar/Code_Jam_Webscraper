#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string flip(string sides, unsigned int start, int K);
string generateTest(size_t length, int K, int nb);
int solve(string sides, int K);

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);
    srand(time(NULL));

    if(!file)
        return -1;

    /*for (int i = 0 ; i < 1000 ; i++)
    {
        size_t l = rand() % 1000 + 1;
        int K = rand() % l + 1;
        int iter = rand() % (l/K + 1) + 1;
        string test = generateTest(l, K, iter);
        int nb = solve(test, K);

        cout << iter << ", " << nb << endl;

        if (nb > iter || nb == -1)
            cout << "Error" << endl;
    }*/

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        string S;
        int K;

        file >> S >> K;
        
        int nb = solve(S, K);

        if(nb == -1)
            output << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else
            output << "Case #" << i+1 << ": " << nb << endl;
    }

    file.close();
    output.close();

    return 0;
}

string flip(string sides, unsigned int start, int K)
{
    string out = sides;

    for (int i = start ; i < start + K ; i++)
    {
        out[i] = (out[i] == '+') ? '-' : '+';
    }

    return out;
}

string generateTest(size_t length, int K, int nb)
{
    string test(length, '+');

    for (int i = 0 ; i < nb ; i++)
    {
        int start = rand() % (length - K + 1);
        test = flip(test, start, K);
    }

    return test;
}

int solve(string sides, int K)
{
    int nb = 0;

    size_t size = sides.size();
    int i = 0;
    for (i = 0 ; i <= size - K ; i++)
    {
        if (sides[i] == '-')
        {
            sides = flip(sides, i, K);
            nb++;
        }
    }

    if (sides.find('-', i) != string::npos)
        return -1;
    else
        return nb;
}

