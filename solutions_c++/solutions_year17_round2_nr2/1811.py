#include <iostream>
#include <string>

using namespace std;

int initLast(int, int, int, int, int, int);
bool endsMatch(string &);

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        string output;
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        int lastColor = initLast(R, O, Y, G, B, V); // 1 2 3 4 5 6
        for(int j = 0; j < N; ++j)
        {
            switch(lastColor)
            {
            case 1:
                if(G > 0)
                {
                    output += 'G';
                    --G;
                    lastColor = 4;
                }
                else
                {
                    if(Y > B)
                    {
                        output += 'Y';
                        --Y;
                        lastColor = 3;
                    }
                    else
                    {
                        output += 'B';
                        --B;
                        lastColor = 5;
                    }
                }
                break;
            case 2:
                if(B > 0)
                {
                    output += 'B';
                    --B;
                    lastColor = 5;
                }
                break;
            case 3:
                if(V > 0)
                {
                    output += 'V';
                    --V;
                    lastColor = 6;
                }
                else
                {
                    if(R > B)
                    {
                        output += 'R';
                        --R;
                        lastColor = 1;
                    }
                    else
                    {
                        output += 'B';
                        --B;
                        lastColor = 5;
                    }
                }
                break;
            case 4:
                if(R > 0)
                {
                    output += 'R';
                    --R;
                    lastColor = 1;
                }
                break;
            case 5:
                if(O > 0)
                {
                    output += 'O';
                    --O;
                    lastColor = 2;
                }
                else
                {
                    if(R > Y)
                    {
                        output += 'R';
                        --R;
                        lastColor = 1;
                    }
                    else
                    {
                        output += 'Y';
                        --Y;
                        lastColor = 3;
                    }
                }
                break;
            case 6:
                if(Y > 0)
                {
                    output += 'Y';
                    --Y;
                    lastColor = 3;
                }
                break;
            }
        }
        if(output.size() < N || R < 0 || Y < 0 || B < 0 || !endsMatch(output))
            cout << "Case #" << i << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << i << ": " << output << '\n';
    }
    return 0;
}

int initLast(int R, int O, int Y, int G, int B, int V)
{
    if(R > 0)
        return 1;
    if(O > 0)
        return 2;
    if(Y > 0)
        return 3;
    if(G > 0)
        return 4;
    if(B > 0)
        return 5;
    if(V > 0)
        return 6;
    return 0;
}

bool endsMatch(string &output)
{
    if(output.size() == 0)
        return true;
    char e = output[output.size()-1];
    switch(output[0])
    {
    case 'R':
        if(e == 'Y' || e == 'G' || e == 'B')
            return true;
        return false;
    case 'O':
        if(e == 'B')
            return true;
        return false;
    case 'Y':
        if(e == 'R' || e == 'B' || e == 'V')
            return true;
        return false;
    case 'G':
        if(e == 'R')
            return true;
        return false;
    case 'B':
        if(e == 'R' || e == 'O' || e == 'Y')
            return true;
        return false;
    case 'V':
        if(e == 'Y')
            return true;
        return false;
    }
    return false;
}
