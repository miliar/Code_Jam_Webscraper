#include <iostream>
#include <fstream>
#include <vector>

#define INFINITY 65535

using namespace std;

bool find(vector<string> pancakes, string pancake)
{
    for(unsigned short i = 0; i < pancakes.size(); ++i)
    {
        if(pancakes[i].compare(pancake) == 0)
        {
            return true;
        }
    }
    return false;
}

void reverse(string &pancake, unsigned short pos, unsigned short K)
{
    for(unsigned short i = pos; i < pos + K; ++i)
    {
        (pancake[i] == '+') ? pancake[i] = '-' : pancake[i] = '+';
    }
}

unsigned short min_flip(vector<string> &pancakes, unsigned short K)
{
    bool test;
    string pancake, tmp;
    unsigned short i, N, p1, p2;
    for(test = true, N = 0, p1 = 0; test; N++)
    {
        for(test = false, p2 = pancakes.size(); p1 < p2; p1++)
        {
            pancake = pancakes[p1];
            if(pancake.find('-') == string::npos)
            {
                return N;
            }
            for(i = 0; i <= pancake.size() - K; ++i)
            {
                tmp = pancake;
                reverse(tmp, i, K);
                if(!find(pancakes, tmp))
                {
                    test = true;
                    pancakes.push_back(tmp);
                }
            }
        }
    }
    return INFINITY;
}

int main()
{
    ifstream file_input("A-small-attempt1.in", ios::in);
    ofstream file_output("A-small-attempt1(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        unsigned short T, K, t, N;
        string S;
        vector<string> pancakes;

        file_input >> T;
        for(t = 1; t <= T; ++t)
        {
            file_input >> S >> K;

            pancakes.clear();
            pancakes.push_back(S);
            cout << "Case #" << t << ": " << S << endl;

            N = min_flip(pancakes, K);
            /*for(unsigned short i = 0; i < pancakes.size(); ++i)
                cout << " " << pancakes[i] << endl;*/
            if(N == INFINITY)
                file_output << "Case #" << t << ": " << "IMPOSSIBLE" << "\n";
            else
                file_output << "Case #" << t << ": " << N << "\n";
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file(s) !" << endl;
    return 0;
}
