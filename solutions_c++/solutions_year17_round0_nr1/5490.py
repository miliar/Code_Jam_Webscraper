#include <iostream>
#include <fstream>

const unsigned int LTH_S_SMALL = 10;
const unsigned int LTH_S_BIG = 1000;
const unsigned int LTH_S = LTH_S_SMALL;
const int IS_IMPOSSIBLE = -1;


void Input(unsigned int& T, bool**& LstS, unsigned int*& LthS, unsigned int*& LstK)
{
    std::ifstream FileIn("A-small-attempt1.in");
    FileIn >> T;
    LstS = new bool*[T];
    LthS = new unsigned int[T];
    LstK = new unsigned int[T];

    for (unsigned int i = 0 ; i < T ; i++)
    {
        char* U_Str = new char[LTH_S];
        FileIn >> U_Str >> LstK[i];

        unsigned int j = 0;
        while (U_Str[j] != '\0')
        {
            j++;
        }
        LthS[i] = j;

        LstS[i] = new bool[LthS[i]];
        for (unsigned int k = 0 ; k < LthS[i] ; k++)
        {
            LstS[i][k] = (U_Str[k] == '+');
        }

        delete U_Str;
    }

    FileIn.close();
}

void Flip(bool* S, unsigned int Index, unsigned int K)
{
    for (unsigned int i = 0 ; i < K ; i++)
    {
        S[Index + i] = !S[Index + i];
    }
}

int RunGreedy(bool* S, unsigned int LthS, unsigned int K)
{
    int Ret = 0;
    bool* U_S = new bool[LthS];
    for (unsigned int i = 0 ; i < LthS ; i++)
    {
        U_S[i] = S[i];
    }

    for (unsigned int i = 0 ; i <= LthS - K ; i++)
    {
        if (!U_S[i])
        {
            Flip(U_S, i, K);
            Ret++;
        }
    }

    for (unsigned int i = LthS - K + 1 ; i < LthS ; i++)
    {
        if (U_S[i] == false)
        {
            Ret = IS_IMPOSSIBLE;
        }
    }

    delete U_S;
    return Ret;
}

void Solve(unsigned int TestCase, bool* S, unsigned int LthS, unsigned int K)
{
    std::ofstream FileOut("out.out", std::ofstream::app);

    FileOut << "Case #" << TestCase << ": ";

    int RetGreedy = RunGreedy(S, LthS, K);

    if (RetGreedy == IS_IMPOSSIBLE)
    {
        FileOut << "IMPOSSIBLE" << std::endl;
    }
    else
    {
        FileOut << RetGreedy << std::endl;
    }

    FileOut.close();
}


int main()
{
    unsigned int T;
    bool** LstS;
    unsigned int* LthS;
    unsigned int* LstK;

    std::ofstream FileOut("out.out", std::ofstream::out);
    FileOut.clear();
    FileOut.close();

    Input(T, LstS, LthS, LstK);

    for (unsigned int i = 0 ; i < T ; i++)
    {
        Solve(i + 1, LstS[i], LthS[i], LstK[i]);
    }
}
