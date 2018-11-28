#include <iostream>
#include <fstream>

using namespace std;

void bathroom_stalls(unsigned long long &N, unsigned long long &K)
{
    if(N == K)
    {
        N = 0;
        K = 0;
        return;
    }

    unsigned long long LS, RS, i, j;
    bool left, right, empty_rooms[N+2];
    for(i = 0; i < N + 2; ++i) empty_rooms[i] = true;
    empty_rooms[0] = false; // first guard
    empty_rooms[N+1] = false; // last guard

    for(j = N, RS = 0; K != 0; j--)
    {
        for(i = 1, LS = 0; i < N + 2 && K != 0; ++i)
        {
            if(empty_rooms[i]) LS++;
            else
            {
                if(LS >= j)
                {
                    RS = i - 1 - LS / 2;
                    empty_rooms[RS] = false;
                    i = 1;
                    K--;
                }
                LS = 0;
            }
        }
    }

    for(i = RS, j = 1, LS = 0, RS = 0, left = true, right = true; i >= j || i + j < N + 2; ++j)
    {
        if(i >= j)
        {
            if(left && empty_rooms[i - j]) LS++;
            else left = false;
        }
        if(i + j < N + 2)
        {
            if(right && empty_rooms[i + j]) RS++;
            else right = false;
        }
    }

    if(LS > RS)
    {
        N = LS;
        K = RS;
    }
    else
    {
        N = RS;
        K = LS;
    }
}

int main()
{
    ifstream file_input("C-small-1-attempt2.in", ios::in);
    ofstream file_output("C-small-1-attempt2.out", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        unsigned short T, t;
        unsigned long long N, K;

        file_input >> T;
        for(t = 1; t <= T; ++t)
        {
            file_input >> N >> K;

            cout << "Case #" << t << ": " << N << " " << K << endl;
            bathroom_stalls(N, K);

            file_output << "Case #" << t << ": " << N << " " << K << "\n";
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file(s) !" << endl;
    return 0;
}
