#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

long solve(string N);

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);
    srand(time(NULL));

    if(!file)
        return -1;

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        string N;
        file >> N;
        
        long nb = solve(N);

        output << "Case #" << i+1 << ": " << nb << endl;
    }

    file.close();
    output.close();

    return 0;
}


long solve(string N)
{
    if (N.size() == 1)
        return stol(N);

    for (int i = N.size() - 2 ; i >= 0 ; i--)
    {
        if (N[i] > N[i+1])
        {
            N[i] = N[i] - 1;

            for (int j = i+1 ; j < N.size() ; j++)
                N[j] = '9';
        }
    }

    return stol(N);
}